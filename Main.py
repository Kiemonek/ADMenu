from tkinter import *
from tkinter.ttk import *
from DashboardButton import *
import os

# Initialize variable for columns and rows
colHelper = 0
rowHelper = 0
# Implement list from json
buttonList = DashboardButton.getButtonList()

root = Tk()
root.title("AD Menu")
root.geometry("640x320")

# Button Generator
for items in buttonList:
    button = Button(root, text = items.title, command = items.onPressed)
    button.grid()
    # print(buttonList.index(items))
    # print(0%2)

# button = Button(root, text = "Add New Button", command = )
# button.grid()

root.mainloop()