class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.books=[self]
        self.b_books=[]
    def borrow_book(self):
        for book in self.books:
            if book not in self.b_books:
                self.b_books.append(book)
                print('you borrowed %s ' %self)
    def return_book(self):
         self.b_books.remove(self)
         print('you returned %s ' % self)

    def check_if_available(self):
        for  self in self.books:
            if self in self.b_books:
                print('The Book %s is not available ' %self)
                return False
        print('The book %s is Available' %self)
        return True
    def __repr__(self):
        return '%s,%s' %(self.title,self.author)

class Shelve:
    def __init__(self,category=''):
        self.my_books=[]
        self.category=category
    def add_book(self,book):
        self.my_books.append(book)
        print('Your Book %s has been added'%self)

    def borrow_books(self,mytitle):
        for b in self.my_books:
              if mytitle==b.title:
                 b.borrow_book() 
              else:
                  print('book doesnt exist')
            

    def return_books(self,book):
        for book in self.my_books:
            book.return_book()
    
    def check_availability(self,book):
        for book in self.my_books:
            if book.check_if_available():
                print('The Book is available')
            else:
                print('The Book is not available')
    def __repr__(self):
        return 'category:%s,%s' %(self.category,self.my_books)

        

if __name__=="__main__":
 shelve1=Shelve('Fiction')
 Book1=Book('runner','by fei')
 shelve1.add_book(Book1)
 Book1.borrow_book()
 Book1.check_if_available()
 Book1.return_book()
 Book1.check_if_available()
