class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"\nProduct ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        print(f"\nProduct ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        print(f"\nProduct ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Specs: {self.specs}GHZ")
        print(f"Price: ${self.price}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        print(f"\nProduct ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Price: ${self.price}")

# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()
my_device = Electronic("123", "Iphone", 1000.00, 3.4)
my_device.display_info()
my_clothes = Clothing("123", "Shirt", 15.99, "Medium")
my_clothes.display_info()
my_product = Product("123", "Blender", 49.99)
my_product.display_info()