try:
    with open('./write/student.txt','r') as file:
        content = file.read()
        print(content)


except FileNotFoundError:
    print("File does not exist")


except PermissionError:
    print("You don't have permission to access this file")

except OSError as error:
    print("File operation failed")