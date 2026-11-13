# number = [1,2,3,4,5]
# # print(number)

# double = []

# for num in number:
#     double.append(num * 2)

# print(double)

number = [1,2,3,4,5]

doubleNum = list(map(lambda number : number * 2,number))

print(doubleNum)


evenNumbers = list(filter(lambda number: number % 2 == 0, number))
print(evenNumbers)

sumOfAllNumbers = reduce(lambda a, b : a + b, number)
