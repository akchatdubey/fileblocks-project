from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)


class Chain(Base):
    __tablename__ = 'chain'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    path = Column(String(255), nullable=False)
    hash = Column(String(255), nullable=False)
    prev_hash = Column(String(255), nullable=False)
    username = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    file_id = Column(Integer, ForeignKey('files.id'))

    def __repr__(self):
        return f'<Chain {self.id}>'

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    path = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)


# utils 
def open_db():
    engine = create_engine('sqlite:///blockchain.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def save(obj):
    session = open_db()
    session.add(obj)
    session.commit()
    session.close()

def getAll(table):
    session = open_db()
    data = session.query(table).all()
    session.close()
    return data




