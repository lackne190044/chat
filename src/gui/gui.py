"""Class GUI has all methods for creating elements for the gui"""
from tkinter import *

class GUI:
    """Create Class GUI"""
    def __init__(self, title=None):
        """Initialize GUI"""
        self.title = title
        self.window = Tk(title)

        self.window.title = title
        self.children = []

    def remove(self, widget):
        """Remove a widget from the gui"""
        widget.pack_forget()

    def create_entry(self, show=None, side="top", container=None):
        """Create a Entry"""
        if container == None:
            container = self.window
        entry = Entry(container, show=show)
        entry.pack(side=side)
        self.children.append(entry)
        return entry

    def create_label(self, text, side, container = lambda: self.window):
        """Create a Label"""
        label = Label(self.window, text=text)
        label.pack(side=side)
        self.children.append(label)
        return label

    def create_row(self, side, container=lambda: self.window):
        """Create a row"""
        row = Frame(container)
        row.pack(side=side)
        self.children.append(row)
        return row

    def create_listbox(self, _side, _container=lambda: self.window, _selectmode='browse'):
        """Create a Listbox"""
        lBox = Listbox(_container, selectmode=_selectmode)
        lBox.pack(side=_side)
        self.children.append(lBox)
        return lBox

    def create_button(self, text, command, side='top', container=None):
        """Create a Button"""
        if container == None:
            container = self.window
        button = Button(container, text=text, command=command)
        button.pack(side=side)
        self.children.append(button)
        return button

    def callback(self, event, _lBox):
        """Print the selected Element of the Curser in the Listbox"""
        for i in _lBox.curselection():
            print(_lBox.get(i))

    def create_column(self, _side, _container=lambda: self.window):
        """Create a Column"""
        column = Frame(container=_container, row=0, column=1)
        column.pack(side=_side)
        self.children.append(column)
        return column

    def create_textbox(self, _side, _container=lambda: self.window):
        """Create a Textbox"""
        textbox = Text(_container)
        textbox.pack(side=_side)
        self.children.append(textbox)
        return textbox

    def clear_textbox(self, textbox):
        """Clear Textbox of all string"""
        textbox.delete('1.0', 'end')


if __name__ == '__main__':
    """For Testing Purposes of the File gui.py"""
    gui = GUI()
    row = gui.create_row('left')

    lBox = gui.create_listbox('left', row, 'single')

    lBox.insert(0, 'testLabel')
    lBox.insert(1, 'anotherLabel')

    lBox.bind('<<ListboxSelect>>', lambda event: gui.callback(event, lBox))
    
    gui.window.mainloop()
