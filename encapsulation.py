class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def show_balance(self):
        print("Owner:",self.owner)
        print("Balance:",self.__balance)

account1=BankAccount("Ravi",5000)
account1.show_balance()
        




#program2
class BankAccount:
    def __init__(self,owner,balance):
        self.owner= owner
        self._account_type="Savings"
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance -= amount
            print("Withdrawl successful")
        else:
            print("insufficient balance or invalid amount")
    def show_balance(self):
        print("Balance:",self.__balance)
account= BankAccount("John",1000)
print("Owner:",account.owner)
print("Account type:",account._account_type)
account.deposit(500)
account.withdraw(300)
account.show_balance()
