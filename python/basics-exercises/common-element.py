arr = [1,2,3,4]
arr2 = [5,6,1,2]
common = []
for element in arr2:
    if(element in arr):
        common.append(element)


print("The common elements :",common)
