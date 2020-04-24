class Wrapper:
    def __init__(self,object):
        self.wrapped=object
    def __getattr__(self,attrname):
     #   print('trace:'+ attrname)
         return getattr(self.wrapped,attrname)

x =Wrapper([1,2,3,4])
print(x.wrapped)
x.append(5)
print(x.wrapped)
y=Wrapper({'a':4,'b':5})
print(list(y.keys()))
