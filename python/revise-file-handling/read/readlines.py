# readlines function use to read multi lines then it will give it as list

file = open('test.txt','r')

names = file.readlines()

print(names)


file.close()

