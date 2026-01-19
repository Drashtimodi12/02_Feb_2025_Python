from abc import abstractmethod,ABC

class Account(ABC):

    balance = 0
    @abstractmethod
    def deposite(self):
        pass

    def checkBalance(self):
        print("current balance is : ",self.balance)

class SavingAccount(Account):

    def deposite(self,amt):
        self.balance+=amt

class LoanAccount(Account):

    def deposite(self,amount):
        self.balance-=amount

s = SavingAccount()
s.checkBalance()
s.deposite(5000)
s.deposite(8000)
s.checkBalance()
print("*********************")
l = LoanAccount()
l.balance=10000
l.checkBalance()
l.deposite(5000)
l.checkBalance()
