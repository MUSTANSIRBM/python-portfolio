import datetime
class Account:
    def __init__(self,name,pin,balance):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []
    def deposit(self, amount):
            # No if statement needed!
            self.balance += amount
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M")
            self.history.append(f'{timestamp} Deposited ${amount}')
            return True

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

            # You forgot to add the history log here!
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M")
            self.history.append(f'{timestamp} Withdrew ${amount}')

            return True
        else:
            return False
class ATM:
    def __init__(self):
        self.accounts = {}
        self.load_data()
    def create_account(self,name, pin, balance):
        a = Account(name, pin, balance)
        self.accounts[name] = a
        self.save_data()

    def login(self, name, pin):
        if name in self.accounts:
            acc = self.accounts[name]
            if acc.pin == pin:
                return acc
            else:
                print("Wrong PIN")
                return None
        else:
            print("User not found")
            return None
    def save_data(self):
        with open('ATMv2.txt' , 'w') as f:
            for acc in self.accounts.values():
                history_string = '|'.join(acc.history)
                f.write(f'{acc.name},{acc.pin},{acc.balance},{history_string}\n')
    def load_data(self):
        try:
            with open('ATMv2.txt' , 'r') as f:
                for line in f:
                    name,pin,balance,history_str = line.split(',')
                    loaded_acc = Account(name, pin, float(balance))
                    if history_str:
                        loaded_acc.history = history_str.split('|')
                    else:
                        loaded_acc.history = []
                    self.accounts[name] = loaded_acc
        except FileNotFoundError:
            pass


atm = ATM()
user = atm.login("Mustansir", "1234")

if user:
    print(f"Welcome {user.name}")
    print(f"Current Balance: ${user.balance}")

    user.deposit(500)
    user.withdraw(200)

    print("\n--- Transaction Log ---")
    for log in user.history:
        print(log)

    atm.save_data()  # Save the new transactions!
