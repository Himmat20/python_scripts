# A problem
# given a list of tuples with info(name,subject)
# .list all unique corses
# .list students enrolled in english
# .create dictionary(student,setof course)

info=[
    ("alice","math"),("alice","science"),("bob","math"),("charlie","english"),
    ("bob","science"),("charlie","math"),("alice","english")
]

ans_1=set() # as a set
ans_2=[] # as a list
ans_3={} # as a dict

# for val in info:
#     ans_1.add(val[1])
#     # if(val[1]=="english"):
#         # ans_2.append(val[0])

for name,subject in info:
    
    ans_1.add(subject)

    if(subject=="english"):
        ans_2.append(name)
    
    if(ans_3.get(name)==None):
        ans_3.update({name: set()})
        ans_3[name].add(subject)
    else:
        ans_3[name].add(subject)


print(f"list of all unique courses in the list are:{list(ans_1)}")
print(f"list of students enrolled in english are:{ans_2}")
print(f"dictionary of students and course{ans_3}")