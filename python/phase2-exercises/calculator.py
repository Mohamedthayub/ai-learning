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

number1 = int(input("Enter the number :"))
number2 = int(input("Enter the number2 :"))
operator = input("What do you want to do ? ")

def validateNumber(num1,num2):
    if(not num1 or not num2):
        print("Please enter number for validation")
        return False
    if(num1 < 1 or num2 < 1):
        print("Please enter valid number for calculation")
        return False
    # if(operator != '+' or operator != '-' or operator != '*' or operator != '/'):
    #     print("Please enter valid operator for calculation")
    #     return False
    return True
if(operator == "+"):
    isValid = validateNumber(number1,number2)
    if(isValid):
        print(add(number1,number2))
elif(operator == "-"):
    isValid = validateNumber(number1,number2)
    if(isValid):
        print(sub(number1,number2))

elif(operator == "*"):
    isValid = validateNumber(number1,number2)
    if(isValid):
        print(multi(number1,number2))
    
elif(operator == "/"):
    isValid = validateNumber(number1,number2)
    if(isValid):
        print(divition(number1,number2))
else:
    print("Invalid Operator")