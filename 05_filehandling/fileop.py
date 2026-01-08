# f = open("05_filehandling/demo.txt","a") #file object
# also path this time its absolute path
# data=f.readline()#for single file line
# # data=f.read()#for complete file
# print(data)
# # print(type(data))

# data=f.readline()
# print(data)

# f.write("\n new append text after overwrite \n using write")

# also creating new txt file
# f = open("05_filehandling/sample.txt","a+")

# f.write("456")
# print(f.read())
# f.close()
# import os
# os.remove("05_filehandling/demo.txt")

data=True
line=1
word="python"
with open("05_filehandling/sample.txt","r") as f:
    while data:
        data=f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
            break
        print(data)
        line+=1
