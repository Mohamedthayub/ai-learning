with open('./write/student.txt','r') as file:
    content = file.read()
    print(content)
# Python automatically closes the file when the with block finishes, even if an exception occurs.