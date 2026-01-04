# constructor
class student:
    def __init__(self,name,year):#parameterized constructor
        self.name=name
        self.year=year
    def getname(self):
        return self.name
    def getyear(self):
        return self.year
        

stu_1=student("himanshu",4)
stu_2=student("aditya",2)
print(stu_1.getname())
print(stu_2.getyear())

# type of constructor are 2
# default and parameterized constructor
# class student: 
#      def__init__(self):  #default constructor
#          print("object is constructed...")
