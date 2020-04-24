class Myclass:
    def __init__(self,name="",phone="",**kwargs):
        
        self.name=name
        
    def show(self):
        print('{}'.format(self.name))
    

class InheritMyclass(Myclass):
    def __init__(self,name='',phone='',**kwargs):
        super().__init__(**kwargs)
        self.phone=phone
    def show2(self,):
        print('{}'.format(self.phone))




obj1=Myclass('feisal',708897463)
obj2=InheritMyclass()
obj1.show()