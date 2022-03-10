from tokenize import group
from CommandHandlers.GroupCommandHandler import GroupCommandHandler as GCH
from Classes.User import User
from gui.gui import GUI
import os
import codecs

current_dir = os.getcwd()
group_files = os.listdir(os.path.join(current_dir, 'Groups'))

user = User('pat')

handler = GCH(commandingUser=user)

gui = GUI()
row = gui.create_row('left')

lBox = gui.create_listbox('left', row, 'single')

for i in group_files:
    handler.load(i)
    if handler.user_in_group(user):
        lBox.insert(0, handler._group._name)

def callback(lBox):
    for i in lBox.curselection():
        print(lBox.get(i))

lBox.bind('<<ListboxSelect>>', lambda event: callback(lBox))

gui.window.mainloop()
