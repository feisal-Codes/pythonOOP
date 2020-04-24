class Contact:
    last_id=0
    def __init__(self,name='',p_number=0,email=''):
        self.name=name.title()
        self.p_number=p_number
        self.email=email.title()
        Contact.last_id+=1
        self.id=Contact.last_id
    def __repr__(self):
        return 'Name: %s   PhoneNumber:  %s E-mail Address:  %s'%(self.name,str(self.p_number),self.email)


class ContactManager(Contact):
    def __init__(self,name='',p_number=0,email=''):
        Contact.__init__(self,name,p_number,email)
        self.contactList=[self]
    def addContact(self,name,p_number,email):
          for self in self.contactList:
            if self not in self.contactList:
             self.contactList.append(Contact(name,p_number,email))
    def deleteContact(self):
        self.contactList.remove(self)
    def updateContact(self,nname,np_number,nemail):
        if self in self.contactList:
            self.name=nname
            self.p_number=np_number
            self.email=nemail
    def searchContact(self,id):
        for self in self.contactList:
            if str(id)==str(self.id):
                return self
        return 'Contact Does Not Exist'

class PhoneBook:
    def __init__(self,*args):
        self.phonebook=list(args)
    def addContacts(self,contact):
        self.phonebook.append(contact)
    def deleteContacts(self,contact):
        for c in self.phonebook:
            if c==contact:
                contact.deleteContact()
        self.phonebook.remove(contact)
    def searchContacts(self,contact):
        for c in self.phonebook:
            if c ==contact:
                return c
        return 'contact is not in phoneBook'
    def showcontacts(self):
        for contact in self.phonebook:
            print(contact)
         
if __name__=="__main__":
    fei=ContactManager('Feisal',708897463,'faz@gmail.com')
    #print(c1.name,c1.id)
    marwa=ContactManager('Marwa',742345678,'mar@gmail.com')
    hafsa=ContactManager('Hafsa',702345566,'haf@gmail.com')
    
    malo=ContactManager()
    malo.updateContact('Malo',723445677,'Malo@gmail.com')
    myphonebook=PhoneBook(fei,marwa,hafsa,malo)
   #myphonebook.showcontacts()
   #print(myphonebook.searchContacts(c4))



























        
