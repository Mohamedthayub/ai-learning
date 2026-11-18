import math
def calculateAvg(*numbers):
    length = len(numbers)
    sum = 0
    for num  in numbers:
        sum = sum + num
    return math.floor(sum / length)
print(calculateAvg(12,12,21,10,20))

# find the average of given tuple 

