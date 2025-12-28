# A classical if/else problems

# working of maybe your phone password
username=input("enter username :")
password=input("enter password :")

if(username=="himanshu" and password=="3104"):
    print("welcome Himanshu")
elif(username!="himanshu"):
    print("wrong username")
else:
    print("wrong password")

# To check the number is multiple of number(lets say 6)
num=int(input("Enter your number:"))
if(num%6==0):
    print("number is a multiple of 6")
else:
    print("not a multiple of 6")
# for number 5 or 7(if multiple of anyone)
if num%5==0 or num%7==0:
    print("number is a multiple of 5 or 7")
else:
    print("not a multiple of any")
# for number 5 and 9(both multiple included)
if(num%5==0 and num%7==0):
    print("number divisible by both")
else:
    print("multiple of any one")


# classical odd/even
NUM=int(input("enter the number:"))
if(NUM%2==0):
    print("number is even")
else:
    print("number is odd")