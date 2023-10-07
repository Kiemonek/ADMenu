from tkinter import *
from tkinter.ttk import *
from DashboardButton import *
from AddNewButton import AddNewButton
import os

def add_new_button():
    newButton = Toplevel(root)
    app = AddNewButton(newButton)

# Implement list from json
buttonList = DashboardButton.getButtonList()

#Customize Window
root = Tk()
root.title("AD Menu")
root.geometry("640x480")

# Button Generator
for items in buttonList:
    button = Button(root, text = items.title, command = items.onPressed)
    button.grid()

#Usable Buttons
butt = Button(root, text = "Add New Button", command = add_new_button)
butt.grid()
butt = Button(root, text = "Modify Buttons" )
butt.grid()
butt = Button(root, text = "Remove Button")
butt.grid()

root.mainloop()