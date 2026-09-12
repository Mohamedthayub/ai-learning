def isUser(name,age):
    if(name == "thayub"):
        result  = "yes this user name is thayub"

    if(age > 18):
        result2 = "yes this user age is greater than 18"

    return name, age

res1, res2  = isUser("thayub",20)

print(res1)
print(res2)

customer = {}
customer["name"] = "thayub"
print(customer)