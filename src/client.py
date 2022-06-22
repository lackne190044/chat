"""This file is the client"""
from cgitb import text
from Classes.Group import Group
from CommandHandlers.GroupCommandHandler import GroupCommandHandler as GCH
from Classes.User import User
from gui.gui import GUI
from getpass import getpass
from tkinter import Button
import os
import codecs

current_dir = os.getcwd()
group_files = os.listdir(os.path.join(current_dir, 'Groups'))
group = None

def main():
    global user

    gui = GUI()

    name_label = gui.create_label('username', 'top')
    name_entry = gui.create_entry()

    password_label = gui.create_label('password', 'top')
    password_entry = gui.create_entry(show="*")

    log_in_button = gui.create_button(text='Login', command=lambda: log_in(gui, name_entry.get(), password_entry.get()))

#lambda: log_in(gui, name_entry.get(), password_entry.get())

    gui.window.mainloop()
    setup_logged_in(gui, user)

def setup_logged_in(gui):
    current_group = None
    global user
    handler = GCH(commandingUser=user)
    row = gui.create_row('left', container=gui.window)

    global lBox
    lBox = gui.create_listbox('left', row, 'single')
    column = gui.create_row('left', gui.window)

    textbox = gui.create_textbox('top', _container=column)
    textbox.config(state='disabled')

    message_and_send_button = gui.create_row('bottom', column)
    message = gui.create_entry(side='left', container=message_and_send_button)
    send_button = gui.create_button(side='left', text='send', command=lambda: send_message(message), container=message_and_send_button)

    for i in group_files:
        handler.load(i)
        if handler.user_in_group(user):
            lBox.insert(0, handler._group._name)

    def callback(lBox):
        global current_group
        for i in lBox.curselection():
            textbox.config(state='normal')
            textbox.delete("1.0","end")
            handler = GCH(commandingUser=user)
            current_group = lBox.get(i)
            handler.load(current_group + '.json')
            add_to_textbox(textbox, handler.load_messages())
            group = current_group

    lBox.bind('<<ListboxSelect>>', lambda event: callback(lBox))

    def send_message(message):
        message = message.get()
        global user
        handler = GCH(commandingUser=user)
        global current_group
        handler.load(current_group + '.json')
        handler.add_message(message)
        handler.save()
        global lBox
        callback(lBox)


def add_message(user, message, group, textbox):
    handler = GCH(commandingUser=user, group=group)
    handler.add_message(message)

def add_to_textbox(textbox, message):
    textbox.config(state='normal')
    textbox.insert('end', message)
    textbox.config(state='disabled')

def log_in(gui, username, password):
    widgets = gui.children
    global user
    user = User(username)
    user.read_file()
    if user.checkpwd(password):
        for i in widgets:
            i.destroy()
            
        setup_logged_in(gui)

if __name__ == '__main__':
    main()
   