# special conditions to use in loop 
# 1.break ->to terminate the loop after a certain condition is meet
# 2.continue ->to skip a specific iteration inside a loop

# break 
i=1
while(i<10):
    if(i%7==0):
        break
    print(i)
    i+=1
print("outside loop")

# inside a table to print it upto 5 only
num=5
i=1
while(i<10):
    print(i*num)
    i=i+1
    if(i%6==0):
        break
print("upto 5 only")

# program to take input expect %7==0
while True:       #infinite loop
    num=int(input("enter your number:"))
    if(num%7==0):
        break
    print(num)

# continue
# wap to print numbers b/w 1 to 10 expect multiple of 3
i=1
while(i<=10):
    if(i%3==0):
        i+=1
        continue
    print(i)
    i+=1

# skip even numbers b\w 1 to 20
i=1
while(i<=20):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

    # parallel approach

i=0
while(i<20):
    i+=1
    if(i%2==0):
        continue
    print(i)
