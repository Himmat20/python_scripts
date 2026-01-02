# here we are going to perform a basic linear search on a list
l=[4,5,3,6,7,9,2,8,1]

# basic code
b=9
idx=0
for val in l:
    if(val==b):
        print(f"{b}found at index:{idx}")
        break
    idx+=1

# inside a function
def linear_search(l,a):
    index=0
    for val in l:
        if(val==a):
            print(f"{a} found at index {index}")
        index+=1

a=int(input("enter the number to search in list:"))
linear_search(l,a)

# also creating a list from user input itself
# starting easy
element=input("enter the value to insert in list:")
lst=element.split()
print(lst)

# pythonic way
lest=list(map(int,input("enter the elements ").split()))
print(lest)