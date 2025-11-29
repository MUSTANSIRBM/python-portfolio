class Credential:
    def __init__(self,website,username,password):
        self.website = website
        self.username = username
        self.password = password
    def __str__(self):
        return f'{self.website} - user: {self.username}'
class Vault:
    def __init__(self):
        self.logins = []
        self.load_data()
    def add_login(self,website, username, password):
        Cred = Credential(website,username,password)
        self.logins.append(Cred)
        self.save_data()
    def get_password(self,website):
        for login in self.logins:
            if login.website == website:
                print(f'Found Password for [{login.website}] is: [{login.password}]')
                return
        else:
            print(f'No password found for [{website}]')
    def save_data(self):
        with open('password_manager.txt' ,'w') as f:
            for p in self.logins:
                 f.write(f'{p.website},{p.username},{p.password}\n')
    def load_data(self):
        try:
            with open('password_manager.txt','r') as f:
                for p in f:
                    p = p.strip()
                    website,username,password = p.split(',')
                    loaded = Credential(website, username, password)
                    self.logins.append(loaded)
        except FileNotFoundError:
            pass
my_vault = Vault()
my_vault.add_login("Instagram", "mustansir_01", "secret123")
my_vault.add_login("Google", "mustansir@gmail", "pass555")
print("\n--- Hacking Attempt ---")
for login in my_vault.logins:
    print(login)

print("\n--- Retrieval ---")
my_vault.get_password("Instagram")
my_vault.get_password("Facebook")

