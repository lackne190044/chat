import json
from re import A
from Classes.User import User
from Classes.Group import Group
from Classes.Message import Message
from CommandHandlers.GroupCommandHandler import GroupCommandHandler as GCH
from time import sleep

test_user = User('testUser')
another_user = User('Philipp')
test_group = Group('testGroup', test_user)

test_message = Message(test_user, "Hello Philipp")
sleep(0.5)
another_message = Message(another_user, "Hello there, how are you doing?")

test_gch = GCH(test_group, test_user)
test_gch.add_user(another_user)
test_gch.add_message(test_message)
test_gch.add_message(another_message)
test_group = test_gch.get_group()
del test_gch

another_gch = GCH(test_group, another_user)
another_gch.add_message(another_message)
test_group = another_gch.get_group()
del another_gch

data = test_group.json

with open(f'{test_group._name}.json', 'w') as file:
    json.dump(data, file, indent=3)