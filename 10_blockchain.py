import datetime as dt
class Transaction:
    def __init__(self,q,s,p):
        self.__quantity = q
        self.__symbol = s
        self.__price = p
        self.__ts = dt.datetime.now()
    def get_trade(self):
        return self.__quantity, self.__symbol, self.__price
    def get_dollars(self):
        return self.__price * self.__quantity

class Block:
    def __init__(self,seq_id):
        self.__transactions = []
        self.__seq_id = seq_id
        self.__ts = dt.datetime.now()
        self.__status = 'UNCOMMITTED'
    def add_transaction(self,q,s,p):
        t = Transaction(q,s,p)
        self.__transactions.append(t)
    def display_all(self):
        for t in self.__transactions:
            print(t)
    def get_size(self):
        return len(self.__transactions)
    def set_status(self,s):
        self.__status = s
    def get_seq_id(self):
        return self.__seq_id

class Blockchain:
    def __init__(self,n):
        self.__name = n
        self.__blocks = []
        self.__current_seq_id = 0
        self.__current_block = Block(self.__current_seq_id)
    def get_id_current_block(self):
        return self.__current_block.get_seq_id()
    def add_transaction(self,q,s,p):
        print('Adding transaction')
        if self.__current_block.get_size() >= 10:
            self.__current_block.set_status('COMMMITTED')
            self.__blocks.append(self.__current_block)
            self.__current_seq_id = self.__current_seq_id + 1
            self.__current_block = Block(self.__current_seq_id)
            print('New block created')
        self.__current_block.add_transaction(q,s,p)   
    def display_blocks(self):
        for b in self.__blocks:
            print(b.get_seq_id())

b = Blockchain('mainnet')
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
b.add_transaction(100,'ibm',100.33)
print(b.get_id_current_block())




'''
print(b.get_id_current_block())
print(dt.datetime.now())



'''
