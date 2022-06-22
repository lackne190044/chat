# creates 3 groups, owned by 3 users with one member each
from cgi import test
from Classes.User import User
from Classes.Message import Message
from Classes.Group import Group
import json

user1 = User('user1')
user2 = User('user2')
user3 = User('user3')
tmp = User('tmp')
tmp2 = User('tmp2')

user1user2 = Group('user1user2', user1)
user1user2.addUser(user2._username)

user2user3 = Group('user2user3', user2)
user2user3.addUser(user3._username)

user3user1 = Group('user3user1', user3)
user3user1.addUser(user1._username)

testGroup = Group('tmpGroup', tmp)
testGroup.addUser(tmp2._username)

groups = [ user1user2, user2user3, user3user1, testGroup ]

for i in groups:
    i.addMessage(Message(i._owner, 'Hello there.'))
    i.addMessage(Message(i._usernames[0], 'Hello there too.'))
    with open(f'./Groups/{i._name}.json', 'w') as file:
        json.dump(i.json, file, indent=3)
