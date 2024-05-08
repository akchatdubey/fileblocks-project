# Importing require libraries
from flask import Flask, render_template, flash, redirect, request, session, logging, url_for, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from database import User, Chain, File, open_db, save, getAll
from bc import Blockchain, Block
from datetime import datetime
# Now create flask application object

app = Flask(__name__)
app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
app.config['NOT_ALLOWED_EXTENSIONS'] = {'exe', 'sh', 'php', 'js', 'html', 'css', 'py', 'java', 'jar'}
app.config['UPLOAD_PATH']='static/uploads'

bc = Blockchain()
# run this on a new machine to create a new blockchain

# block = bc.get_latest_block()
# # store in blockchain
# save(Chain(
#     timestamp = block.timestamp,
#     path = block.filepath,
#     hash = block.hash,
#     prev_hash = block.previous_hash,
#     username = block.user,
#     user_id = block.userId,
#     file_id = block.fileId,
# ))
    
@app.route('/')
def home():
    return render_template('index.html')

# User Registration Api End Point
@app.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = generate_password_hash(form.password.data)
        db = open_db()
        new_user = User(
            username = form.username.data, 
            email = form.email.data, 
            password = hashed_password )
        user = db.query(User).filter_by(email = form.email.data).first()
        if user:
            flash('Email address already exists', 'danger')
            return redirect(url_for('register'))
        if db.query(User).filter_by(username = form.username.data).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        save(new_user)
        flash('You have successfully registered', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)


# Login API endpoint implementation
@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate:
        db = open_db()
        user = db.query(User).filter_by(email = form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                flash('You have successfully logged in.', "success")
                session['logged_in'] = True
                session['email'] = user.email 
                session['username'] = user.username
                session['id'] = user.id
                return redirect(url_for('home'))
            else:
                flash('Username or Password Incorrect', "Danger")
                return redirect(url_for('login'))
    return render_template('login.html', form = form)

@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/upload')
def index():
    return render_template('upload.html')

@app.route('/upload',methods =['POST'])
def upload_file():
    if 'logged_in' not in session or session['logged_in'] == False:
        flash('Please login to upload file', 'danger')
        return redirect(url_for('login'))
    db = open_db()
    user = db.query(User).filter_by(email = session['email']).first()
    print(user.username)
    last_block = db.query(Chain).all()[-1]
    # return f'current hash: {last_block.hash} previous hash: {last_block.prev_hash}'
    uploaded_file = request.files.get('myfile')
    filename = secure_filename(uploaded_file.filename)
    if uploaded_file.filename !='':
        file_ext= os.path.splitext(filename)[1]
        if file_ext in app.config['NOT_ALLOWED_EXTENSIONS']:
            flash('Invalid file extension', 'danger')
            return redirect(url_for('index'))
        path = os.path.join(app.config['UPLOAD_PATH'],filename)
        uploaded_file.save(path)
        file = File(
            name = filename,
            path = path,
            user_id = user.id
        )
        db.add(file)
        # create a block and add to blockchain in database after retrieving previous block
        latest_file = db.query(File).filter_by(user_id = user.id).all()[-1]
        new_block = Block(
            index= last_block.id + 1,
            timestamp = last_block.timestamp,
            userid= user.id,
            fileid= latest_file.id,
            user = user.username,
            filepath = path,
            previous_hash = last_block.hash
        )
       
        bc.add_block(
            new_block
        )
        # add new block to database

        chain_entry = Chain(
            timestamp = datetime.now(),
            path = path,
            hash = new_block.hash,
            prev_hash = new_block.previous_hash,
            username = user.username,
            user_id = user.id,
            file_id = latest_file.id
        )
        db.add(chain_entry)
        db.commit()
        db.close()
        flash('File uploaded successfully to Blockchain', 'success')
    return redirect(url_for('index')) 


# list all files from blockchain
@app.route('/chain/list', methods = ['GET', 'POST'])
def chain_list():
    db = open_db()
    chain = getAll(Chain)[1:]
    return render_template('chain_list.html', bc = chain)

@app.route('/bc/list')
def file_list():
    return render_template('file_lists.html')
    
# my files
@app.route('/bc/myfiles')
def my_files():
    if 'logged_in' not in session or session['logged_in'] == False:
        flash('Please login to view files', 'danger')
        return redirect(url_for('login'))
    db = open_db()
    user = db.query(User).filter_by(email = session['email']).first()
    chain = db.query(Chain).filter_by(user_id = user.id).all()
    files = []
    for c in chain:
        file = db.query(File).filter_by(id = c.file_id).first()
        files.append(file)
    
    return render_template('my_files.html', files = files, bc = chain)

# download file
@app.route('/bc/download/<int:id>')
def download_file(id):
    print(f'current url: {request.url}')
    if 'logged_in' not in session or session['logged_in'] == False:
        flash('Please login to download file', 'danger')
        return redirect(url_for('login'))
    db = open_db()
    chain = db.query(Chain).filter_by(file_id = id).first()
    # check ownership
    user = db.query(User).filter_by(email = session['email']).first()
    if chain.user_id != user.id:
        flash('You are not authorized to download this file', 'danger')
        return redirect(url_for('my_files'))
    print('file:', chain.path)
    dir = os.path.dirname(chain.path)
    filename = os.path.basename(chain.path)
    print('filename:', filename)
    return send_from_directory(dir, filename, as_attachment=True)
    

if __name__ == '__main__':
    app.run(debug=True)
