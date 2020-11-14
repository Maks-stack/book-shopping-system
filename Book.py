class Book():

    def __init__(self, title, price, author, ID):
        self.title = title
        self.price = price
        self.author = author
        self.id = ID

    def print_book(self):
        print("ID: " + self.id + " - Title: " + self.title + " - Price: " + self.price + " - Author: " + self.author)

    def print_book_in_cart(self, quantity):
        print("ID: " + self.id + " - Title: " + self.title + " - Price: " + self.price + " - Author: " + self.author + " - Quantity: " + quantity)
