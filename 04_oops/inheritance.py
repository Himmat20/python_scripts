# inheritance
# reusing attribute and methods from a parent class(base class)

# parent class
class employee:
    start_time="9am"
    end_time="5pm"
    # also
    def changetime(self,new_endtime):
        self.end_time=new_endtime

# child class
class teacher(employee):
    def __init__(self,subject):
        self.subject=subject
# child class
class admin(employee):
    def __init__(self,role):
        self.role=role

# object
t1=teacher("python")
t1.changetime("3pm")
e1=admin("cashier")


# acessing parent class property in child class
# print(t1.subject,t1.start_time,t1.end_time)
# print(e1.role,e1.start_time,e1.end_time)

# types of encapsulation
# 1.single level inheritance
# 2.multilevel inheritance
# 3.multiple inheritance

# single level inheritance

class one:
    name="alpha"
    time="1830 hour"

class beeta(one):
    def __init__(self,designation):
        self.designation=designation

b1=beeta("officer")

print(b1.designation,b1.name,b1.time)

# multilevel innheritance

class Employe:
    st_time="8 am"
    end_time="5 pm"

class Adminstaff(Employe):
    def __init__(self,role):
        self.role=role

class Accountant(Adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary

ab=Accountant(25_000,"CA")
print(ab.role,ab.salary,ab.st_time,ab.end_time)

# mutiple level inheritance
class Principle:
    def __init__(self,salary):
        self.salary=salary

class Teacher:
    def __init__(self,subject):
        self.subject=subject

class VP(Principle,Teacher):
    def __init__(self,salary,subject,name):
        super().__init__(salary)                #here we cannot use two super function 
        # super().__init__(subject)              #also while calling the constructor of child self is required with subject
        Teacher.__init__(self,subject)
        self.name=name

vice=VP(23_000,"python","himanshu")
print(vice.name,vice.salary,vice.subject)