from __future__ import print_function

class Employee:
    def __init__(self,name,salary=0):
        self.name=name
        self.salary=salary
    def giveRaise(self,percent):
        self.salary= int(self.salary + (self.salary * percent))
    def work(self):
        print(self.name,"does stuff")
    def __repr__(self):
        return "Employee: name={}, salary={}".format(self.name,self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,15000)
    def work(self):
        print(self.name, "Makes Food")
class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,20000)
    def work(self):
        print(self.name,"Interfaces with Customer")

class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)
    def work(self):
        #print(self.name,'makes pizza')
        pass
if __name__=="__main__":
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob); print()
    # Make a robot named bob
    # Run inherited __repr__
    # Run type-specific action
    # Give bob a 20% raise
    for klass in Employee, Chef, Server, PizzaRobot:
       obj = klass(klass.__name__)
       obj.work()
