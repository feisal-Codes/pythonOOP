
#from __future__ import print_function

from employee1 import PizzaRobot,Server


class Customer:
    NumbPizzaOrdered=0
    Totalsells=0
    def __init__(self,name):
        self.name=name
        self.quantity=0
        self.price=0
    def orders(self,server,quantity):
        #print(self.name,"orders from Employee",server.name)
        self.quantity=quantity
        Customer.NumbPizzaOrdered+=self.quantity
    def pays(self,server,price):
        #print(self.name,"pays item to Employee ",server.name)
        self.price=price*self.quantity
        Customer.Totalsells+=self.price
        Customer.receipt(self,server)
    def receipt(self,server):
        
        print('Customer Name: {}\nQuantity ordered: {} \nAmount Paid: {}'.format(self.name,self.quantity,self.price))
        print('You were served by {}'.format(server.name))
class Oven: 
    def bake(self):
        #print("oven bakes")
        pass
class PizzaShop:
    total_sells=0
    def __init__(self):
        self.server=Server('Abdi')
        self.chef= PizzaRobot('Robochef')
        self.oven=Oven()
    def order(self,name,quantity=1,price=200):
        self.customer=Customer(name)
        self.customer.orders(self.server,quantity)
        self.chef.work()
        self.oven.bake()
        self.customer.pays(self.server,price)
    def calculatesells(self):
        return Customer.Totalsells 
    def receipts(self,name=''):
        self.customer.receipt(name)

if __name__=="__main__":
    scene = PizzaShop()
    scene.order('Ibrahim',5,500)
    #print(scene.calculatesells())
    #scene.receipts()
    print("...........")
    scene.order('Ahmed',1,1000)
    #print(Customer.NumbPizzaOrdered)
    #print(scene.calculatesells())
    print('................')
    scene.order('Feisal',4,500)
    print('......................')
    #scene.receipts()
    print('Total Pizza: ' ,Customer.NumbPizzaOrdered,'Total Sells: ',Customer.Totalsells)
