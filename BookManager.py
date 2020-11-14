import itertools
from Book import Book

class BookManager():

    id_iter = itertools.count(1)

    def __init__(self):
        self.books = {}
        self.cart = {}
        
    
    def listBooks(self, args = None):
        if (bool(self.books)): 
            for value in self.books.values():
                value.print_book()
        else:
            print("No books available")
	        

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

    def searchBook(self, args):
        print('a7')
        print(args)
        #next((x for x in test_list if x.value == value), None)
    
    def addBook(self, bookname, bookprice, bookauthor):
        id = next(self.id_iter)
        book = Book(bookname, bookprice, bookauthor, id)
        self.books.update({id : book})

    def deleteBook(self, bookId):
        print('a9')
        bookid = bookId[0]
        self.books.pop(bookid)

        print(bookid)

    def notAFun(self, args = None):          
        print('This function is not a correct one') 

        