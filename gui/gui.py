from tkinter import *

class GUI:
    def __init__(self):
        self.window = Tk('chat')

        self.window.title = 'chat'

    def create_row(self, side, container=lambda: self.window):
        row = Frame(self.window)
        row.pack(side=side)
        return row

    def create_listbox(self, _side, _container=lambda: self.window, _selectmode='browse'):
        lBox = Listbox(_container, selectmode=_selectmode)
        lBox.pack(side=_side)
        return lBox

    def callback(self, event, _lBox):
        for i in _lBox.curselection():
            print(_lBox.get(i))


if __name__ == '__main__':
    gui = GUI()
    row = gui.create_row('left')

    lBox = gui.create_listbox('left', row, 'single')

    lBox.insert(0, 'testLabel')
    lBox.insert(1, 'anotherLabel')

    lBox.bind('<<ListboxSelect>>', lambda event: gui.callback(event, lBox))
    
    gui.window.mainloop()
