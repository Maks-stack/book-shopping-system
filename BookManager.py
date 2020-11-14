import itertools

class BookManager():

    id_iter = itertools.count()

    def __init__(self):
        books = {}
        cart = {}


    def listBooks(args = None):
        print("asd")

    def addToCart(bookId):
        print('a2')

    def listCart(args = None):
        print('a3')

    def clearCart(args = None):
        self.cart = {}

    def editCart(bookId):
        print('a5')

    def checkout(args = None):
        print('a6')

    def searchBook(option, info):
        print('a7')
        #next((x for x in test_list if x.value == value), None)

    def addBook(args):
        self.id = next(self.id_iter)
        book = Book(bookName, bookPrice, bookAuthor, self.id)
        self.books.append(book)

    def deleteBook(bookId):
        print('a9')

        