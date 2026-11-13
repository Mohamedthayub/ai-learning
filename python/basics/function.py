# def sayName(name):
#     return name

# result = sayName("Thayub")

# print(result)


# def add(num1,num2):
#     return num1 + num2

# print(add(10,1))


# def sub(num1,num2):
#     return num1 - num2

# result = sub(10,10)

# print(result)



# def test(name = "Test"):
#     return name

# print(test());

# -------------------------------------

# keyword arguments and position arguamets


# def calculate_total(*args):
#     total = 0
#     for price  in args:
#         total += price

#     return total
# result = calculate_total(100,200,300)
# print(result)


# keyword arguments;



# def createUser(**user):
#     for key,value in user.items():
#         print(key, ":" , value);


# createUser(name = "Thayub",age = 20,city= "TRN", role = "Backend Eng")
# print(result)

# def example(*args,**kwargs):
#     print("Positional arguments :",args)
#     print("Keyword arguments :",kwargs)

# example(10,20,30, name ="Thayub",age = 21)


# returning  multiple values in python

# def calculate(a,b):
#     addition = a + b
#     subtraction = a - b
#     multiplication = a * b

#     return addition,subtraction,multiplication

# result = calculate(10,5)

# print(result)


# lambda function


# square  = lambda number : number * number
# print(square(5))
# print(square)


# add two number using lambda function
# add = lambda a ,b : a + b
# print(add(10,10))

# isOdd = lambda num : num % 2 == 0  



# scoping in python 


# def greet():
#     message = "Hello Thayub"
#     print(message)

# greet()

# print(message)

count = 0
def increase():
    global count
    count = count + 1
    return count

print(increase())