print("strings")
# sequence of characters

word="Himanshu" 
word_1="bhardwaj"
# for length of string
print(len(word))

# concatenation
print(word+" "+word_1)

# index start with 0

# loops in strings
for ch in word:
    print(ch)

# indexing
# string[index_start:index_end]
# slicing
# making a substring
# print(word[0:8])
# print(word[:])
# print(word[4:])
# print(word[:4])

# string formatting

# 1.format function
a=45
b=54
sum=a+b
print("sum of a and b is ",sum)

#index based formatting by default the values are 0,1,2 and so on

print("sum of {} and {} is {}".format(a,b,sum))  
print("sum of {1} and {0} is {2}".format(a,b,sum))

# value based formatting
#here value are put inside the function directly  
print("sum of {a} and {b} ".format(a=43,b=57))

# 2.f-strings
# currently used formatting
print(f"difference of {b} and {a} is {b-a}")