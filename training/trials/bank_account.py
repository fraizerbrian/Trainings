# creating a bank account
class Account:

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner:{self.owner}, Balance:{self.balance}"

    def deposit(self,dep_amnt):
        self.balance = self.balance + dep_amnt
        print("Deposit Successful")

    def withdrawal(self, withdrawal_amnt):
        if self.balance >= withdrawal_amnt:
            self.balance = self.balance - withdrawal_amnt
            print("withdrawal Successful")
        else:
            print("Withdrawal Unsuccessful. Low Balance!")


acct1 = Account('Jose',100) # 1 instantiating class
print(acct1) # 2 print the object
acct1.owner # 3 show the account owner attribute
acct1.balance # 4 show the account balance attribute
acct1.deposit(50) # 5 make a series of deposits and withdrawals
acct1.withdrawal(75)
acct1.withdrawal(500) # 6 make a withdrawal that exceeds the available balance
