from CommandHandlers.GroupCommandHandler import GroupCommandHandler as GCH
from Classes.User import User
from gui.gui import GUI
import os
from os import listdir
from os.path import isfile, join

user = User('Philipp')

groupPath = os.path.join(os.getcwd(), 'Groups')

handler = GCH(commandingUser=user)

handler.load('testGroup.json')

gui = GUI()
row = gui.create_row('left')

lBox = gui.create_listbox('left', row, 'single')

onlyfiles = [f for f in listdir(groupPath) if isfile(join(groupPath, f))]

lBox.insert(0, handler._group._name)

def callback(lBox):
    for i in lBox.curselection():
        print(lBox.get(i))

lBox.bind('<<ListboxSelect>>', lambda event: callback(lBox))

gui.window.mainloop()
