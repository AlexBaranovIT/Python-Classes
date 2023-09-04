class BankAccount:
    def __init__(self, account_holder):
        self.fullname = account_holder
        self.balance = 0

    def deposit(self):
        amount = int(input('How much money you want to deposit? '))
        self.balance += amount

    def withdraw(self):
        amount = int(input('How much money you want to withdraw? '))
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal of ${amount:.2f} successful.')
        else:
            print('Insufficient funds.')

    def get_info(self ):
        info = f'Your name is: {self.fullname}\nYour balance is: ${self.balance:.2f}'
        print(info)


my_acc = BankAccount('Alex')

my_acc.deposit()

my_acc.withdraw()

my_acc.get_info()
