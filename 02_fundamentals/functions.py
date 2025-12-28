# functions are a set of reusable code blocks that can be used again and again in a program
# there are two types of function inbuilt and user defined 

# inbuilt functions
# print(),range()...

# user defined code blocks
def hello():# function defination
    print("hello python")
hello() #function call

# function to calculate sum of two variables
def sum(a,b):#parameters a,b
    sum=a+b
    return sum
print(sum(54,45))#argument

# function to calculate average of two variables
def average(a,b,c):
    average=(a+b+c)/3
    return average
num_1=int(input("enter number:"))
num_2=int(input("enter number:"))
num_3=int(input("enter number:"))
print(average(num_1,num_2,num_3))