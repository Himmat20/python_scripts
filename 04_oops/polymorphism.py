# polymorphism
# mutiple functions but same name
# eg-> + for concatenation and addition of int

# 1.function overriding
class Employee():
    def get_designation(self):#function
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):#function
        print("designation = Teacher")

t1= Teacher()

t1.get_designation() #same function exist in parent but is overwrite by child class

# 2.Duck typing
# same function but diffent work

class Student():
    def get_info(self): #function
        print("student")

class Account():
    def get_info(self): #function
        print("accountant")

s1=Student()
s1.get_info()

a1=Account()
a1.get_info()
