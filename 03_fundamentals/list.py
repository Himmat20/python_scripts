# list ->mutable datatypes
# sequence of values

l=[1,2,3,4,5,6,7,"abc","95"]
marks=[94,93,95,96,66,54]
print(type(l))
print(len(marks))
marks[5]=99
print(marks)

# slicing and indexing 
print(l[:])
print(l[2:6])
# works same as strings but list is mutable datatype

# list methods
# 1.append->to add element at last of the list
l.append(99)
print(l)

# 2.insert(idx,val)->to insert value at a specific index
marks.insert(1,91)
print(marks)

# 3.sort->to arrange the list in increasing or decreasing order
marks.sort()
print(marks)
# also in dec order
marks.sort(reverse=True)
print(marks)

# 4.reverse to completely reversed the list irrespective the order
l.reverse()
print(l)
