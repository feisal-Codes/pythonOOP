
class ContactList(list):
    def search(self,name):
        matching_contact=[]
        for contact in  self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact 

class Contact:
    all_contacts = ContactList()

    def __init__(self,name,email):
        self.name=name
        self.email=email
        Contact.all_contacts.append(self)
    
class Supplier(Contact):
    def order(self,order):
        print( f" {order} order to  {self.name}")

class Friends(Contact):
    def __init__(self,name,email,phone):
        super().__init__(name,email)
        self.phone=phone



c1=Contact('feisal','faz@gmail.com')
s1=Supplier('fei','fei@gmail.com')
s2=Supplier('fe','fe@gmail.com')
s2.order('10 sacks of rice')
s3=Friends('fei','faz@gmail.com',+254708897463)

