import itertools
from Book import Book

class BookManager():

    id_iter = itertools.count()

    def __init__(self):
        self.books = {}
        self.cart = {}   
    
    def listBooks(self, args = None):
        for key, value in self.books.items():
	        print("ID: " + str(value.id) + "Title:" + value.title + "Price" +  str(value.price) + "Author: " + value.author)

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
    
    def addBook(self, bookname, bookprice, bookauthor):
        print("adding book")
        self.id = next(self.id_iter)
        book = Book(bookname, bookprice, bookauthor, id)
        self.books.update({id: book})

    def deleteBook(bookId):
        print('a9')

    def notAFun(self, args = None):          
        print('This function is not a correct one') 

        