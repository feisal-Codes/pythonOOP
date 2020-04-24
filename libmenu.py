
import sys
from library import Book,Shelve 

class Menus:
 """Display a menu and respond to choices when run."""

 def __init__(self):
        self.shelve = Shelve()
        self.choices = {
            "1": self.borrow_bookss,
        
            "3": self.add_books,
    
            "5": self.quit,
        }


 def display_menu(self):
    print(
        """
     Notebook Menu
     1. Borrow Book
     2. Return Book
     3. Add Book
     4. Check if book is available
     5. Quit
    """
    )


 def run(self):
    """Display the menu and respond to choices."""
    while True:
        self.display_menu()
        choice = input("enter an option")
        action = self.choices.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))


 def add_books(self):
     book=input('Enter Books Title and Author')
     self.shelve.add_book(book)
     
 def borrow_bookss(self):
     t=input('Enter book title')
     self.shelve.borrow_books(t)

 def quit(self):
    print("Thank you for using The LIbrary today.")
    sys.exit(0)



#if __name__ == "__main__":
    #Menus().run()