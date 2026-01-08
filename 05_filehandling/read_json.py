import json

# py_obj={
#     "name":"renu",
#     "subject":"aiml"
# }

# json_str=json.dumps(py_obj)

# print(type(json_str),json_str)

# json_str='{"name":"himmat"}'

# py_obj=json.loads(json_str)
# print(type(py_obj),py_obj)

d={
    "name":"naman",
    "age":20,
    "isTeacher":True
}

with open("05_filehandling/data.json","w") as f:
    # py_obj = json.load(f)
    # print(py_obj) 
    json.dump(d,f,indent=4,sort_keys=True)
