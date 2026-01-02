# sets
# collection of unique elements
# working is similar to math sets
s={1,2,3,4,5,6}
print(type(s))
# also
my_set={1,2,2,2,3,4,5}
print(my_set) #and
print(len(my_set))

# for empty set
empty_set=set()
print(type(empty_set))

# methods in set

# 1.add(val)->adds a value
s.add(8)
print(s)

# 2.remove(val)->removes a value
s.remove(8)
print(s)

# 3.pop()->removes random value
s.pop()
print(s)

# 4.clear()->empty the set
s.clear()
print(s)

set_1={2,3,4,5,6}
set_2={4,6,8,7}

# 5.union(set)->return union of two set
print(set_1.union(set_2))

# 6.intersection(set)->returns intersection of two set
print(set_1.intersection(set_2))