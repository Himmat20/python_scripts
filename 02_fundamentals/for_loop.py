# for loop
# for sequential traversal
# in string
string="hello_python" 
for ch in string:
    print(ch)
# in integers
for i in range(5):
    print(i)

# # printing table
num=int(input("enter your number:"))
for i in range(1,11):
    print(num,"times",i,"is",num*i)

# in strings
word="artificial intelligence"
count=0
for ch in word:
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        count+=1
print("number of vowel in word is :",count)

# problem
word="himanshu bhardwaj"
for ch in word:
    if "j" in word:
        print("wrong word")
        break
    else:
        print(ch)

print("j" in word)#in keyword

# wap to print sum of n natural number
num = int(input("enter your number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum)