from BookManager import BookManager


def main():
    ''' In the main, the user is asked which commands he wants to use and the relevant functions are called '''

    book_manager = BookManager()
    functions = {
        "listBooks": book_manager.listBooks,
        "listCart": book_manager.listCart,
        "addToCart": book_manager.addToCart,
        "clearCart": book_manager.clearCart,
        "editCart": book_manager.editCart,
        "checkout": book_manager.checkout,
        "searchBook": book_manager.searchBook,
        "addBook": book_manager.addBook,
        "deleteBook": book_manager.deleteBook
    }

    inp = input('What command do you want to execute?\n')

    while (inp != "quit"):
        diff_inp = inp.split()
        func = functions.get(diff_inp[0], book_manager.notAFun)

        diff_inp.pop(0)    # delete the name of the function from the list so that only the options remain

        func(diff_inp)

        inp = input('\nWhat command do you want to execute?\n')

main()