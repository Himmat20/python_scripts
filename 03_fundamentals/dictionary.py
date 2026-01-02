# dictionary 
# it is a type of immutable unordered datatype
# key:value pairs
# declaring a dictionary
my_dict={
    "name":"himanshu",
    "class":4,
    "subjects":["gs","math","english"],
}
print(type(my_dict))
print(my_dict)
# here keys are unique value

# methods in dictionaries

# 1.keys()->returns all keys
print(my_dict.keys())

# also we caonvert it into list as
k_s=list(my_dict.keys())
print(type(k_s))
print(k_s)


# 2.values()->returns all values
print(my_dict.values())

# 3.items()-> returns (key,value)
print(my_dict.items())

# 4.get(value)->return value according key
print(my_dict.get("name"))

# 5.update(new_item)-> to add new value in the list
my_dict.update({"s_name":"bhardwaj"})
print(my_dict)

# loop on dict
for key,value in my_dict.items():
    print(key,value)
