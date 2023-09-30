from tkinter import *
from tkinter.ttk import *
import DashboardButton
import AddButton
import os

# Initialize variable for columns and rows
colHelper = 0
rowHelper = 0
# Implement list from json
buttonList = DashboardButton.button_list

root = Tk()
root.title("AD Menu")

# Button Generator
for items in buttonList:
    button = Button(root, text = items.title, command = items.onPressed)
    button.grid()
    # print(buttonList.index(items))
    # print(0%2)

root.mainloop()