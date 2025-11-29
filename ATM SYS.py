class Account:
    def __init__(self,name,pin):
        self.transaction_history = []
        self.name = name
        self.pin = pin
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
        self.transaction_history.append(f'Deposited ${amount}')
    def withdraw(self,amount,entered_pin):
        if entered_pin != self.pin:
            print('Wrong PIN')
            return False
        if amount > self.balance:
            print('Insufficient Funds')
            return False
        else:
            self.balance -= amount
            self.transaction_history.append(f'Withdrew ${amount}')
            print('Withdrawal Successful!')
            return True
    def check_history(self):
        for history in self.transaction_history:
            print(history)

class Bank:
    def __init__(self):

        self.accounts = {}
    def create_account(self,name,pin):
        new =Account(name,pin)
        self.accounts[name] =new
        print(f'Account created for {name}')
        self.save_data()
    def login(self,name,entered_pin):
        if name  not in self.accounts:
            print('User Not Found')
            return None
        user_pin = self.accounts[name]
        if user_pin.pin == entered_pin:
            return user_pin
        else:
            print("Wrong Pin")
            return None
    def save_data(self):
        with open('bank_data.txt','w') as f:
            for acc in self.accounts.values():
                f.write(f'{acc.name},{acc.pin},{acc.balance}\n')

my_bank = Bank()

my_bank.create_account("Mustansir", 1234)
my_bank.create_account("Alice", 5555)

user = my_bank.login("Mustansir", 9999)

user = my_bank.login("Mustansir", 1234)

if user:
    user.deposit(500)
    user.check_history()
