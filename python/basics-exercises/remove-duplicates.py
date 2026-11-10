arr = [1,1,2,2,3,4,5,6,7];

frequency = {};
for number in arr:
    frequency[number] = frequency.get(number,0) + 1;

unique = [];
for num in frequency:
    unique.append(num)

print(unique)

# remove duplicates from the array 

