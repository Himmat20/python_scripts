class student:
    college_name="jims" #class attribute
    pi=3.1

    def __init__(self,name,subject,cgpa):
        self.name=name     #instance
        self.subject=subject
        self.cgpa=cgpa
        self.pi=3.14
    
stu_1=student("himanshu","python",9.1)

print(stu_1.name)
print(stu_1.college_name)

print(stu_1.pi)
print(student.pi)