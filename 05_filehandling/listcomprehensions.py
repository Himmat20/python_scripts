# squares=[]
# for i in range(6):
#     squares.append(i*i)
# print(squares)

sq=[i*i for i in range(6) if i%2!=0]
print(sq)

nums=[-2,-3,5,6,3,-1,2,4]
nums=[0 if val<0 else val for val in nums]
print(nums)

words=["hello","himanshu"]
words=[val.upper() for val in words]
print(words)