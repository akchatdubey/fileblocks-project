import hashlib
import datetime as date

class Block:
    def __init__(self, index, timestamp, fileid, userid, user, filepath, previous_hash="", hash=None):
        self.index = index
        self.timestamp = timestamp
        self.fileId = fileid
        self.userId = userid
        self.user = user
        self.filepath = filepath
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        print('Block created')

    def calculate_hash(self):
        print('Calculating hash')
        hash_string = str(self.index) + str(self.timestamp) + self.filepath + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()
    

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(
            index = 0,
            timestamp = date.datetime.now(),
            fileid = 0,
            userid = 0,
            user = "Genesis",
            filepath = "genesis"
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        if new_block.previous_hash == "":
            new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    
if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.add_block(
        Block(
            index = 1,
            timestamp = date.datetime.now(),
            fileid = 1,
            userid = 1,
            user= "Akshat",
            filepath = "path/to/file1"
        )
    )
    blockchain.add_block(
        Block(
            index = 2,
            timestamp = date.datetime.now(),
            fileid = 2,
            userid = 2,
            user = "Vikas",
            filepath = "path/to/file2"
        )
    )

    blockchain.add_block(
        Block(
            index = 3,
            timestamp = date.datetime.now(),
            fileid = 3,
            userid = 3,
            user = "Rahul",
            filepath = "path/to/file3"
        )
    )


    for block in blockchain.chain:
        print("Index: ", block.index)
        print("Timestamp: ", block.timestamp)
        print("Previous Hash: ", block.previous_hash)
        print("Hash: ", block.hash)
        print("File ID: ", block.fileId)
        print("User ID: ", block.userId)
        print("File Path: ", block.filepath)
        print()