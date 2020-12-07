
from abc import ABC ,abstractmethod
import enum
import datetime
class BookFormat(enum.Enum):
    hardCover,paperBack,audioBook,ebook,newsPaper,magazine,journal= 1,2,3,4,5,6,7

 
class BookStatus(enum.Enum):
    available, reserved ,loan ,lost =1,2,3,4
class ReservationStatus(enum.Enum):
    waiting, pending ,cancelled , none = 1,2,3,4
class AccountStatus(enum.Enum):
    active ,closed , cancelled ,blacklisted ,none = 1,2,3,4,5
class Address:
    def __init__(self, streetadress,city,state,zipcode,country):
        self.__streetadress= streetadress
        self.__city=city
        self.__state=state
        self.__zipcode=zipcode
        self.__country=country
class Person(ABC):
    def __init__(self,name,address,email,phone):
        self.__name=name
        self.__address=address
        self.__email=email
        self.__phone=phone
class Constants:
    __max_books_issued_to_a_user= 5
    __max_lendind_days= 10
#####################
#account , member and librarian 
#these classes rep various people that interact with our system 

class Account(ABC):
    def __init__(self, id ,password, person ,status = AccountStatus.active):
        self.__id= id 
        self.__password=password
        self.__person=person
        self.__status = status
    def resetPassword(self):
        None

class Librarian(Account):

    def __init__(self,id ,password,person,status=AccountStatus.active):
        super().__init__(id ,password,person,status)
    def addBookItem(self,bookitem):
        None
    def blockMember(self,member):
        None
    def unBlockMember(self,member):
        None
class Member(Account):

    def __init__(self,id ,password,person,status=AccountStatus.active):
        super().__init__(id ,password,person,status)
        self.__dateOfMembership=datetime.date.today()
        self.__totalBooksCheckedOut=0
    def getTotalBooksCheckedOut(self):
        return self.__totalBooksCheckedOut



























        














