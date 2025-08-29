# f = open("practice.txt","w")
# f.write("Hi eveeryone\n")
# f.write("we are learning file i/o \n")
# f.write("using Java \n")
# f.write("i like programing in Java\n")
# f.close()


# new ques
# f = open("practice.txt","r+")
# data = f.read()
# new_data = data.replace("Java", "python")
# print(new_data)
# f.write(new_data)


# searching element in file
f = open("practice.txt","r")
data = f.read()
if(data.find("learning")):
    print("found")
else:
    print("not found")
