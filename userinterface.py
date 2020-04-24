from pizzashop import PizzaShop
import sys


while True:
 print("Welcome To HappyEats Pizza Shop")
 print(
        """
     HappyEats Menu
     1. Menu
     2. Order Pizza
     3. Quit
     
    """
    )
 action=input('Enter An Option')
 if action=='2':
     scene = PizzaShop()
     name=input('Customers Name: ')
     quantity=int(input('Enter Quantity '))
     price=int(input('Enter Price of Type Pizza '))
     print('\n\tReceipt')
     scene.order(name,quantity,price)
     print('t.h.a.n.k.......y.o.u.................................................................................................')
     print('........................................................................................................................')
 elif action=='1':
     print(
        """
     size:      price(sh):
     Large      1000
     Medium     800
     Mini       500
     
    """
    )
 elif action=='3':
     sys.exit(0)
 else:
     print('Enter A Valid Choice')