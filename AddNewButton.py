import json
from tkinter import *
from tkinter.ttk import *

class AddNewButton():

    def __init__(self, root):
        self.root = root
        self.root.title("Add new button")
        self.root.geometry("200x200")
        self.label = Label(root, text="insert data")
        self.label.pack()