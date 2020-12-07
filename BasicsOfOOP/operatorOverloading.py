class Complex:
    def __init__(self,real=0 ,imag=0):
        self.real=real
        self.imag=imag

    def __add__(self,other): #overloading '+' operator
        temp=(self.real + other.real, self.imag+other.imag)
        return temp

    def __sub__(self,other): #overloading '+' operator
        temp=(self.real - other.real, self.imag - other.imag)
        return temp


obj1=complex(3,7)
obj2=complex(2,5)

obj3=obj1+obj2
obj4=obj1-obj2


print('real of obj3: ',obj3.real)
print('imaginary of obj3: ',obj3.imag)
print('real of obj4: ',obj4.real)
print('real of obj4: ',obj4.imag)

 