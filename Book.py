import itertools

class Book():

    id_iter = itertools.count()

    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
        self.id = next(self.id_iter)

