import math
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multi(num1,num2):
    return num1 * num2

def divition(num1,num2):
    result = math.floor(num1 / num2)
    return result

number1 = input("Enter the number :")
number2 = input("Enter the number2 :")
command  = input("What do you want to do ? ")

def validateNumber(num1,num2,command):
    if(not num1 or not num2 ):
        return "Please provide number for calculation"
    if(not command):
        return "Please provide calculation symbol"
    if(command != "+" or command != "-" or command != "*" or command != "/"):
        return "Please provide correct command for calculation"
    return ""


if(command == "+"):
    result = validateNumber(number1,number2,command)
    if(result != ""):
        print(result)
    else:
        add(number1,number2)
elif(command == "-"):
    result = validateNumber(number1,number2,command)
    if(result != ""):
        print(result)
    else:
        sub(number1,number2)

elif(command == "*"):
    result = validateNumber(number1,number2,command)
    if(result != ""):
        print(result)
    else:
        multi(number1,number2)
elif(command == "/"):
    result = validateNumber(number1,number2,command)
    if(result != ""):
        print(result)
    else:
        divition(number1,number2)

