frequency = {}

arr = [1,2,3,4,5,1,1,3,3,4,4]

for number in arr:
    frequency[number] = frequency.get(number,0) +1


for key,value in frequency.items():
    print(key,value)