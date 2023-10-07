import json
from tkinter import *
from tkinter.ttk import *

class AddNewButton():
    
    def __init__(self, root):
        self.root = root
        self.root.title("Add new button")
        self.root.geometry("200x500")
        
        self.label = Label(root, text="Insert data")
        self.label.pack()
        
        self.label1 = Label(root, text="Domain:")
        self.label1.pack()
        
        self.textDomain = Text(root, height=2)
        self.textDomain.pack()
        
        self.label2 = Label(root, text="Username:")
        self.label2.pack()
        
        self.textUsername = Text(root, height=2)
        self.textUsername.pack()
        
        self.label3 = Label(root, text="Server:")
        self.label3.pack()
        
        self.textServer = Text(root, height=2)
        self.textServer.pack()
        
        self.button = Button(root, text="SAVE")
        self.button.pack()
        self.button = Button(root, text="EXIT")
        self.button.pack()