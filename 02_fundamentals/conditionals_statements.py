# conditionals statements that control the workflow of data
# types of cs->if,elif and else
# program to check if a person can vote
age=int(input("enter your age: "))
if age>18:
    print("Eligible to vote")
else:
    print("! Eligible to vote")

# program for traffic lights
color=input("enter your color:")

if color=="RED":
    print("stop")
elif color=="YELLOW":
    print("look")
elif color=="GREEN":
    print("go")
else:
    print("invalid color")

# program for age bracket
AGE=int(input("Enter your age:"))
if(AGE>0 and AGE<=12):
    print("young one")
elif(AGE>=13 and AGE<=19):
    print("teenage")
else:
    print("adult")