# number1 = 10
# number2 = 0

# result = number1 / number2
# print(result)

# try:
#     number = int(input("Enter the number 1 :"))
#     number2 = int(input("Enter the number 2 :"))
#     result =  number / number2
#     print(result)


# except ZeroDivisionError:
#     print("Cannot Divide by Zero")

# except ValueError:
#     print("Please enter valid numbers")



# try:
#     number  = int(input("Enter the number"))

# except ValueError:
#     print("Invalid number")
# else:
#     print("your number is :",number)

# finally:
#     print("Program completed")


try:
    file = open('Users.txt','r')
    print(file.read())

except FileNotFoundError: # if the file not found we will raise the error
    print("File not found")

finally:
    print("Program completed")