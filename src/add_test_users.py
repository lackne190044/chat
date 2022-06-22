import json
import os
from Classes.User import User

filepath = os.path.join(os.getcwd(), 'users.json')

users = [
    ['user1', 'Kennwort1'],
    ['user2', 'Kennwort1'],
    ['user3', 'Kennwort1'],
    ['tmp', 'Kennwort1'],
    ['tmp2', 'Kennwort1']
]

data = []

for i in users:
    tmp = User(i[0])
    tmp.hashpwd(i[1])
    data.append({ 'username': tmp._username, 'password': tmp._hashpwd.decode('utf8') })

with open(filepath, 'w') as file:
    json.dump(data, file, indent=3)
