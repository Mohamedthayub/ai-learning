# def removeDuplicates(arr):
#     for

arr = [1,2,3,4,5,1,]
# names = ["one","two","three","four"]

temp = []
for i  in range(0,len(arr)- 1):
    if(arr[i] != arr[i+1]):
        temp.append(arr[i])


print(temp)