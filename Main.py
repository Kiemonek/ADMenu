from tkinter import *
from tkinter.ttk import *
from DashboardButton import *
from AddNewButton import AddNewButton
import os
# Implement list from json
buttonList = DashboardButton.getButtonList()

def add_new_button():
    newButton = Toplevel(root)
    app = AddNewButton(newButton)

# Initialize variable for columns and rows
colHelper = 0
rowHelper = 0

root = Tk()
root.title("AD Menu")
root.geometry("640x320")

# Button Generator
for items in buttonList:
    button = Button(root, text = items.title, command = items.onPressed)
    button.grid()
    # print(buttonList.index(items))
    # print(0%2)

butt = Button(root, text = "Add New Button", command = add_new_button)

butt.grid()

root.mainloop()