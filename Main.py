from tkinter import *
from tkinter.ttk import *
from DashboardButton import *
from AddNewButton import *
import os

def addButton():
    newButton = Toplevel(root)
    app = AddNewButton(newButton)

def refresh():
    root.update()
    root.destroy()

# Implement list from json
buttonList = DashboardButton.getButtonList()

# Customize Window
root = Tk()
root.title("AD Menu")
root.geometry("640x480")

# Button Generator
for items in buttonList:
    button = Button(root, text = items.title, command = items.onPressed)
    button.grid()

# Usable Buttons
add_button = Button(root, text = "Add New Button", command = addButton)
add_button.grid()
mod_button = Button(root, text = "Modify Buttons" )
mod_button.grid()
rem_button = Button(root, text = "Remove Button")
rem_button.grid()

root.mainloop()