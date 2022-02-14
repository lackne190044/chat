import json
import os
import sys
import bcrypt
from getpass import getpass

if os.path.exists('users.json'):
    with open('users.json', 'r') as file:
        data = json.load(file)
else:
    data = []

def get_hash(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

def check(_data, username, password):
   for i in _data:
       if i['username'] == username:
           return check_password(password, bytes(i['password'].encode()))

def add(_data, to_append):
    _data.append(to_append)

arguments = sys.argv[1:]
if arguments[0] == 'add':
    username = input('What is your username: ')
    hashed = get_hash(getpass('What is your Password: ')).decode('utf8').replace("'", '"')
    add(data, { 'username': username, 'password': hashed })
elif arguments[0] == 'check':
    print(check(data, arguments[1], arguments[2]))

with open('users.json', 'w') as file:
    json.dump(data, file, indent=2)
