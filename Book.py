import itertools

class Book():

    id_iter = itertools.count()

    def __init__(self, title, price, author, ID):
        self.title = title
        self.price = price
        self.author = author
        self.id = ID

    def print_book():
        print("ID: " + self.id + " - Title: " + self.title + " - Price: " + self.price + " - Author: " + self.author)

