# find the second largest element in the array

arr = [1,2,3,4,5]
largest = arr[0]
for element in  arr:
    if(element > largest):
        largest = element

Slargest = -1
for element in arr:
    if(element != largest and  element < largest):
        Slargest = element

print(Slargest)

