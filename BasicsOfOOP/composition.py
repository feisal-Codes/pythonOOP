"""

composition is the practise of accessing other
class objects in your class

the class which creates the object is known as the owner 
and is responsible for the life time of the object

"""
class Student:
    def __init__(self,name=None,regNo=None,year=0):
        self.name=name
        self.regNo=regNo
        self.year=year


    def printDetails(self):
        print('Student Name ',self.name ,'', 'Student RegNo ',self.regNo,' class of: ',self.year)
class Lecturer:
    def __init__(self,name=None,id=0):
        self.name=name
        self.id=id
    def printDetails(self):
        print(self.name,'',self.id)
class BSIT:
    def __init__(self,name,year):
        self.name=name
        self.year=year     
        self.__students=[]
    def addStudent(self,student):
        self.__students.append(student)
    def searchStudent(self,Id):
        for student in self.__students:
            if student.regNo==Id:
                return 'Name: ' +  student.name, ' RegNo: '+ student.regNo,  'Adm Year: '+ str(student.year)
    def getStudents(self,year):
          for student in self.__students:
              if student.year==year:
                print('Name:'+ student.name, 'RegNo: '+ student.regNo,  'Adm Year: '+ str(student.year))
    def printDetails(self):
        #self.student.printDetails()
        #self.lecture.printDetails()
        #print(self.__students)
        for n in self.__students:
            n.printDetails()
class Faculty():
    def __init__(self,name):
        self.name=name
        self.mem=[]

    def addClasses(self,mem):
        self.mem.append(mem)
    def getClasses(self):
        for i in self.mem:
            print(i.name)
            i.getStudents(i.year)
            
stu=[Student('Abdi Mohamed','a11',2016),
Student('Abdi Gedi','a12',2016),
Student('Feisal Mohamed','a13',2016),
Student('Yussuf Mohamed','a14',2016)]

stu1=[Student('Adk Mohamed','a15',2017),
Student('yuss Gedi','a19',2017),
Student('Fei Mohamed','a18',2017),
Student('Yu Mohamed','a16',2017)]

bs16=BSIT('Class of 2016',2016)

for student in stu:
    bs16.addStudent(student)
#bs16.printDetails()

print('..............................................')

bs17=BSIT('Class of 2017',2017)


for student in stu1:
    bs17.addStudent(student)
#bs17.printDetails()
print('..............................................')

    

#print(bs17.getStudents(2017))

faculty=Faculty('IT')
faculty.addClasses(bs17)
faculty.addClasses(bs16)

print(faculty.getClasses())


