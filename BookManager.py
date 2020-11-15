import itertools
import shlex
from Book import Book

class BookManager():

    id_iter = itertools.count(1)

    password = "password"

    def __init__(self):

        self.books = {}
        self.cart = {}

    def listBooks(self, args = None):
        if (bool(self.books)): 
            for value in self.books.values():
                value.print_book()
        else:
            print("No books available")
	        


    def addToCart(self, bookId):
        '''check if the book exists in self.books.
           check if the book already is in the cart. If it is in the cart the quantity + 1. If not create the entry in the dict with quantity 1'''

        bookId = bookId[0]

        if bookId in self.books:
            if bookId in self.cart:
                self.cart[bookId]['quantity'] += 1
            else:
                self.cart[bookId] = {'book': self.books[bookId], 'quantity': 1}
        else:
            print('The ID is not correct')


    def listCart(self, args = None):
        for value in self.cart.values():
            value['book'].print_book_in_cart(str(value['quantity']))


    def clearCart(self, args = None):
        self.cart = {}


    def editCart(self, bookId):
        bookId = bookId[0]

        if bookId in self.cart:
            self.cart[bookId]['quantity'] -= 1
            if self.cart[bookId]['quantity'] == 0:
                del self.cart[bookId]

            self.listCart()
        else:
            print('The ID is not correct')


    def checkout(self, args = None):
        total = 0

        if bool(self.cart):
            for value in self.cart.values():
                price = int(value['book'].price) * value['quantity']
                total += price

                value['book'].print_book_in_cart(str(value['quantity']))
                print('The price for this is ' + str(price) + ' EUR\n')

            print('The total price of the cart is ' + str(total) + ' EUR')

            trans = input('\nDo you want to pay now: ')

            if trans == 'yes':
                self.clearCart()

        else:
            print('There are no books in the cart')


    def searchBook(self, args):
        searchType = args[0]
        
        if(searchType == "-i"):
            searchId = args[1]
            self.books.get(searchItem).print_book()
           
        if(searchType == "-n"):
            args.pop(0)
            searchTerm = ' '.join(args)
            foundBooks = [x for x in self.books.values() if x.title == searchTerm]

            for book in foundBooks:
                book.print_book()
            
    def addBook(self, args):

        lists = ' '.join(args)
        info = shlex.split(lists)
        author = ""
        
        password = input('Please Enter Password: ')
        if(password == "password"):
            self.id = str(next(self.id_iter))
        
            if len(info) == 3:
                author = info[2]

            book = Book(info[0], info[1], author, self.id)    
            self.books[self.id] = book
            self.listBooks()
        else:
            print("Wrong password")

    def deleteBook(self, bookId):
        password = input('Please Enter Password: ')
        if(password == "password"):
            bookid = bookId[0]
            if bookid in self.books:
                print("Deleting Book: " + self.books.get(bookid).title)
                self.books.pop(bookid)
                self.listBooks()
            else: 
                print("Book not found")
        else:
            print("Wrong password")
    
    def notAFun(self, args = None): 
        print('This function is not a correct one')       