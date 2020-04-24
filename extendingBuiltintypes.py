class Mylist(list):
    def search(self,name):
        matching=[]
        for x in self:
            if name in  x.name:
                matching.append(x)
        return matching

class Contact:
    contact_list=Mylist()

    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
        Contact.contact_list.append(self)
class MyContact:
    MYcontact_list=Mylist()

    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
        MyContact.MYcontact_list.append(self)

c1=Contact('feisal',708897463)
c2=Contact('abdi',8888888)
c1=MyContact('Yahya',708897463)
c2=MyContact('Sadiq',8888888)

print([c.name for c in  MyContact.MYcontact_list.search('Yahya')])
print([c.name for c in Contact.contact_list.search('abdi')])
