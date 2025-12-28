# using condition inside condition
username=input("enter your name:")
password=input("enter your password:")

if(username=="himanshu" and password=="3104"):
    print("welcome himanshu")
else:
    if(username!="himanshu"):
        print("wrong username")
    else:
        print("wrong password")
    # here instead of using two different
    # condition we combine them