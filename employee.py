from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
        #print("This is person's init")
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):

        self.pay = int(self.pay * (1 + percent))

    #def __repr__(self):
        #return '[Person: %s, %s]'%(self.name,self.pay)
        #return AttrDisplay.__repr__(self)
class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,'mgr',pay)
    def giveRaise(self,percent,bonus =.10):
        Person.giveRaise(self,percent+bonus)
class Department:
    def __init__(self,*args):
        self.members=list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
if __name__=="__main__":
    abdi=Person('Abdi Ibrahim')
    fei=Person('feisal mohamed',job='dev',pay=100000)
    marwa=Manager('Marwa Mohamed',50000)
    tom=Person('Tom Brady',job='dev',pay=10000)
    abdi.pay=10000
    abdi.giveRaise(.10)

    development = Department(abdi, fei,tom)
    development.addMember(marwa)
    development.giveRaises(.10)
    development.showAll()










