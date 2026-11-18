import json


# user = {
#     "name":"Mohamed",
#     "age":23,
#     "role":"Backend Developer"
# }

# json_data = json.dumps(user) # this dumps method will convert the dictionary to json

# print(json_data)

json_data  = '{"name": "Mohamed", "age": 23}'

user = json.loads(json_data)

print(user)