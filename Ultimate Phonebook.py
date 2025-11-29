class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f'{self.name} | Phone: {self.phone} | Email: {self.email}'
class PhoneBook:
    def __init__(self):
        self.contacts = []
        self.load_data()
    def add_contact(self, name, phone, email):
        contact = Contact(name,phone,email)
        self.contacts.append(contact)
        self.save_data()
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print('contact not Found')
    def show_all(self):
        for con in self.contacts:
            print(con)
    def save_data(self):
        with open('contacts.txt','w') as f:
            for n in self.contacts:
                line  = f'{n.name},{n.phone},{n.email}\n'
                f.write(line)

    def load_data(self):
        try:
            with open('contacts.txt','r') as f:
                for line in f:
                    line = line.strip()
                    if not line:continue
                    name,phone,email = line.split(',')
                    loaded_contact = Contact(name, phone, email)
                    self.contacts.append(loaded_contact)

        except FileNotFoundError:
            print('Starting new phonebook.')
# 1. Initialize
my_book = PhoneBook()

# 2. Add People
my_book.add_contact("Mustansir", "9636929753", "mum2524086@sicsr.ac.in")
my_book.add_contact("Aman", "7487069882", "mam2524078@sicsr.ac.in")

# 3. Show All
print("\n--- All Contacts ---")
my_book.show_all()

# 4. Search
print("\n--- Searching ---")
my_book.search_contact("Aman") # Should find her
my_book.search_contact("Bob")   # Should say not found

# 5. CHECK FILE 'contacts.txt'
