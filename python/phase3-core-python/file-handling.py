# file = open("users.txt","w")
# file.write("Mohamed\n")
# file.write("Mohideen\n")

# here we create a file called users.txt add the content like Mohamed,Mohideen,Thayub


# file = open('users.txt','r')

# content = file.read()

# print(content)

# file.close()

# here we read the file show the file content



with open ("users.txt","r") as file:
    content = file.read()
    print(content)

# in this  with methods we dont need to manually close the file

