# program to print factorial of a number using function

# function defination
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

# user input
num=int(input("enter the number:"))

# function call/invoke
ans=cal_fact(num)

# result
print("factorial of",num,"is:",ans)