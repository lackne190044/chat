import json
import os
import sys
import bcrypt
from User import User
from getpass import getpass

users = []

if os.path.exists('users.json'):
    with open('users.json', 'r') as file:
        user_data = json.load(file)
        for i in user_data:
            tmp_user = User(i['username'])
            tmp_user._hashpwd = i['password']
            users.append(tmp_user)
else:
    user_data = []

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

    tmp_user = User(username)
    tmp_user.hashpwd(getpass('What is your Password: '))

    users.append(tmp_user)
    add(user_data, { 'username': username, 'password': tmp_user._hashpwd.decode('utf8') })

elif arguments[0] == 'check':
    print(check(user_data, arguments[1], arguments[2]))

with open('users.json', 'w') as file:
    print('changed')
    json.dump(user_data, file, indent=2)
print('end')
