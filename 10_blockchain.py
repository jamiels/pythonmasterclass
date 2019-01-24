import datetime as dt
import uuid
import hashlib
class Transaction:
    def __init__(self,f,t,v):
        self.__from = f
        self.__to = t
        self.__value = v
        self.__ts = dt.datetime.now()
        content = str(uuid.uuid4()) + str(self.__from) + str(self.__to) + str(self.__value) + str(self.__ts)
        self.__tx_hash = hashlib.sha256(str(content).encode('utf-8')).hexdigest()
    def get_hash(self):
        return self.__tx_hash
    def display_tx(self):
        print(self.__from,self.__to,self.__value)

class Block:
    def __init__(self,seq_id,prev_hash):
        self.__transactions = []
        self.__seq_id = seq_id
        self.__ts = dt.datetime.now()
        self.__status = 'UNCOMMITTED'
        self.__uuid = uuid.uuid4()
        self.__prev_block_hash = prev_hash
        self.__block_hash = None
    def add_transaction(self,f,t,v):
        tx = Transaction(f,t,v)
        self.__transactions.append(tx)
    def display_all(self):
        for t in self.__transactions:
            t.display_tx()
    def get_size(self):
        return len(self.__transactions)
    def set_status(self,s):
        self.__status = s
    def get_seq_id(self):
        return self.__seq_id
    def gen_simple_merkle_root(self):
        content = ''
        for tx in self.__transactions:
            content = content + tx.get_hash()
        return hashlib.sha256(str(content).encode('utf-8')).hexdigest()
    def gen_block_hash(self):
        content = str(self.__ts) + str(self.__seq_id) + str(self.__uuid) + str(self.gen_simple_merkle_root())
        self.__block_hash = hashlib.sha256(str(content).encode('utf-8')).hexdigest()
        return self.__block_hash
    def display_block_info(self):
        print('Block id:',self.__seq_id,'Block hash:',self.__block_hash,'Previous hash:',self.__prev_block_hash)

class Blockchain:
    def __init__(self,n):
        self.__name = n
        self.__blocks = []
        self.__current_seq_id = 0
        self.__current_block = Block(self.__current_seq_id,None)
    def get_id_current_block(self):
        return self.__current_block.get_seq_id()
    def add_transaction(self,f,t,v):
        print('Adding transaction')
        if self.__current_block.get_size() >= 10:
            self.__current_block.set_status('COMMMITTED')
            curr_block_hash = self.__current_block.gen_block_hash()
            self.__blocks.append(self.__current_block)
            self.__current_seq_id = self.__current_seq_id + 1
            self.__current_block = Block(self.__current_seq_id,curr_block_hash)
            print('New block created')
        self.__current_block.add_transaction(f,t,v)   
    def display_blocks(self):
        for b in self.__blocks:
            print(b.display_block_info())
        self.__current_block.display_block_info()

class Account:
    self.__address = '' #hash(publickey )
    self.__balance = 0

    def increment(amount):
        self.__balance = self.__balance + amount
    


class Node:
    self


b = Blockchain('mainnet')
for n in range(0,150):
    b.add_transaction('john','linda',100.33)

# RichardBux
b.display_blocks()




'''
print(b.get_id_current_block())
print(dt.datetime.now())



'''
