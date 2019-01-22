class Transaction:
    def __init__(self,q,s,p):
        self.__quantity = q
        self.__symbol = s
        self.__price = p
    def get_trade(self):
        return self.__quantity, self.__symbol, self.__price
    def get_dollars(self):
        return self.__price * self.__quantity

class Block:
    def __init__(self):
        self.__transactions = []
    def add_transaction(self,q,s,p):
        t = Transaction(q,s,p)
        self.__transactions.append(t)
    def display_all(self):
        for t in self.__transactions:
            print(t)

b = Block()
b.add_transaction(100,'IBM',100.33)

b.display_all()


