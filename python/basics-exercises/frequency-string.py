str = "hello"
frequency = {}

for s in str:
    frequency[s] = frequency.get(s,0) + 1

print(frequency)