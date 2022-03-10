# creates 3 groups, owned by 3 users with one member each
from Classes.User import User
from Classes.Message import Message
from Classes.Group import Group
import json

pat = User('pat')
luk = User('luk')
heli = User('heli')

patluk = Group('patluk', pat)
patluk.addUser(luk._username)

lukheli = Group('lukheli', luk)
lukheli.addUser(heli._username)

helipat = Group('helipat', heli)
helipat.addUser(pat._username)

groups = [ patluk, lukheli, helipat ]

for i in groups:
    i.addMessage(Message(i._owner, 'Hello there.'))
    i.addMessage(Message(i._usernames[0], 'Hello there too.'))
    with open(f'./Groups/{i._name}.json', 'w') as file:
        json.dump(i.json, file, indent=3)
