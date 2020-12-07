class Country:
    def __init__(self,name=None,population=0):
        self.name=name
        self.population=population
    def printDetails(self):
        print('Country name: ',self.name)
        print('Country Population: ',self.population)

class Person:
    def __init__(self,name,country,pop=0):
        self.name=name 
        self.country=country
        self.pop=pop
        country.population+=self.pop
    
    def printDetails(self):
        print('Person name: ',self.name)
        self.country.printDetails()

c= Country('kenya',1500)
p= Person('feisal',c,1)
p.printDetails()


print('......')
c.printDetails()
del p # even after we delete the person object , country object lives
print('......')
c.printDetails()