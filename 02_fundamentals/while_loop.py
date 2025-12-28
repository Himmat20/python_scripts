# while loop

# program to use while to print hello five 5 times
count=0 #iterator
while(count<5):  #condition
    print("hello_python")
    count+=1  #incriminator

# program to print number from 1 to 5
n=int(input("enter the number:"))
i=1
while(i<n+1):
    print(i)
    i+=1

# to reverse print the number from 5 to 1
n=int(input("enter your number:"))
i=n
while(i>0):
    print(i)
    i-=1; 

# table
num=int(input("enter your number:"))
i=1
while(i<=10):
    print(num,"times",i,"is",i*num)
    i+=1

# reverse table
num=int(input("enter your number:"))
i=10
while(i>0):
    print(num,"times",i,"is",i*num)
    i-=1
