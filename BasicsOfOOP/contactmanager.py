import datetime
import pickle 
import json

class Contact:
    __contactList=[]
    def __init__(self,name,phoneNumber,location, email):
        self.name=name
        self.phoneNumber=phoneNumber
        self.location= location
        self.email=email
        self.date= datetime.date.today()
        Contact.__contactList.append(self)

    def searchContact(self):
        if self in Contact.__contactList:
            return self
        else:
            print('Contact Does not exist')

    def AddContact(self):
                return  Contact.__contactList.append(self)


    def deleteContact(self):
        if self in Contact.__contactList:
            Contact.__contactList.remove(self)                        

    def __str__(self):
        return('Contact Name: ' + self.name  +  ' Phone Number: ' + 
        str(self.phoneNumber) + ' E-mail: ' + self.email +' Location: '+ self.location) 
    
class PhoneBook(Contact):
    def __init__(self,name):
        self.name=name
        self.phonebooklist=[]
        
    def addContactTophonebook(self,contact):
        self.phonebooklist.append(contact)

  

    def getPhoneBookList(self):
        for contact in self.phonebooklist:
            print(contact)


    def updateContact(self,contactt):
        
        
            #or contact in self.phonebooklist:
            if contactt in self.phonebooklist:
                print(' what would you like to update ')
                choice=int(input('1:Name 2:PhoneNumber 3:Email 4:location 5:Update all fields'))
                if choice== 1 :
                    name=input('Enter New name')
                    contactt.name= name
                    
                elif choice== 2 :
                    n=input('Enter New PhoneNumber')
                    contactt.phoneNumber= n
                    
                elif choice== 3 :
                    name=input('Enter New Email')
                    contactt.email= name
                    
                elif choice==4:
                     name=input('Enter New Location')
                     contactt.location= name
                     
                elif choice==5:
                    name=input('Enter New name')
                    contactt.name= name
                    n=input('Enter New PhoneNumber')
                    contactt.phoneNumber= n
                    name=input('Enter New Email')
                    contactt.email= name
                    name=input('Enter New Location')
                    contactt.location= name
                    return contactt
                    

            else:
                print('Contact does not exist')
    
    def storeContact(self):
        filename='/home/fesal/Desktop/pythonpractise /OOPPython/BasicsOfOOP/contact.txt'
        with open (filename,'wb') as outfile:
            pickle.dump(self.phonebooklist,outfile)
    def deleteContact(self,contact):
        if contact in self.phonebooklist:
            contact.deleteContact()
            self.phonebooklist.remove(contact)
        else:
            print('Contact does not exist')
 
c1=Contact('feisal',+2540708897463,'wajir','feisal@gmail.com')
c2=Contact('feis',+2540708897463,'mandera','feisal@gmail.com')
c3=Contact('fsal',+2540708897463,'garisa','feisal@gmail.com')
friends=PhoneBook("friends' PhoneBook")
for contact in (c1,c2,c3):
  friends.addContactTophonebook(contact)

friends.getPhoneBookList()
print(c3.searchContact())


friends.storeContact()



























