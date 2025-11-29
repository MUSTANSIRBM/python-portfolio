class product:

    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    def __str__(self):
        return f'[{self.name}] - $[{self.price}] (Stock: {self.stock}))'

class Store:
    def __init__(self):
        self.products = []
        self.load_data()
    def add_product(self,name, price, stock):
        inventory =product(name, price, stock)
        self.products.append(inventory)
        self.save_data()
    def sell_product(self,name, quantity):
        for p in self.products:
            if p in self.products:
                if p.name == name:
                    if p.stock >= quantity:
                        p.stock -= quantity
                        print(f'Sold! Total: ${p.price * quantity }')
                        self.save_data()
            else:
                print("Out of stock!")
            return
    def save_data(self):
        with open('product_list.txt', 'w') as f:
            for p  in self.products:
                f.write(f'{p.name},{p.price},{p.stock}\n')
    def load_data(self):
        try:
            with open('product_list.txt','r') as f:
                for line in f:
                    line = line.strip()
                    name,price,stock = line.split(',')
                    prices = float(price)
                    stocks = int(stock)
                    loaded_product = product(name, prices, stocks)
                    self.products.append(loaded_product)
        except FileNotFoundError:
            print("No inventory file found. Starting fresh store!")
shop = Store()
shop.add_product("Laptop", 1000.0, 10)
shop.add_product("Mouse", 20.5, 50)

shop.sell_product("Laptop", 2)  # Should work, remaining stock 8
shop.sell_product("Mouse", 100) # Should fail (Not enough stock)

# CHECK FILE 'inventory.txt'
