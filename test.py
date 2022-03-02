from CommandHandlers.GroupCommandHandler import GroupCommandHandler as GCH
import os
import json

file = os.path.join(os.getcwd(), 'testGroup.json')

anGCH = GCH()
anGCH.load(file)
group = anGCH.get_group()

with open('test.json', 'w') as file:
    json.dump(group.json, file, indent=3)
