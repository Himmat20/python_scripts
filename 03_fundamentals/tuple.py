# tuple immutable datatype
# we cannot change the values once created
tup=(1,2,3,4)
print(type(tup))

# also for single value
tup_1=(1,)#not just (1) <-integer not tuple
print(type(tup_1))

# slicing and indexing same as list
print(tup[:])
print(tup[2:3])

# loops
# to sum all values of tuple
sum=0
for val in tup:
    sum+=val
print(f"sum of all element is {sum}")

# tuple methods
# 1.index(val)->return 1st occurence of the element
print(tup.index(4))

# 2.count(val)->return the number of times the number appear in tuple
tpl=(1,2,3,1,2,3,1,2,2,2,1,4)
print(tpl.count(2))