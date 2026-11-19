class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        # print("Account created 1000 deposited successfully")

    def get_balance(self):
        return f"account balance is {self.__balance}"

    def deposit(self,amount):
        if(amount <= 0):
            print("Invalid Amount")
            return

        self.__balance += amount

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return 

        if amount > self.__balance:
            print("Insufficient balance")
            return 

        self.__balance -= amount
account = BankAccount(1000)
print(account.get_balance())
account.deposit(1000)
print(account.get_balance())
account.withdraw(1000)
print(account.get_balance())