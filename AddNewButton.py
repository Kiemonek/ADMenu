# import json
from tkinter import *
    
class AddNewButton():

    def __init__(self, root):
        self.root = root
        self.root.title("Add new button")
        # self.root.geometry("200x500")
        
        self.label = Label(root, text="Insert data").grid()
        
        self.label_Domain = Label(root, text="Domain:").grid()
        
        self.textDomain = Text(root, height=2).grid()
        
        self.label_Username = Label(root, text="Username:").grid()
        
        self.textUsername = Text(root, height=2).grid()
        
        self.label_Server = Label(root, text="Server:").grid()
        
        self.firstOctet = Text(root, height=2, width=4).grid()
        
        self.label_dot1 = Label(root, text=".").grid()
        
        self.secOctet = Text(root, height=2, width=4).grid()
        
        self.label_dot2 = Label(root, text=".").grid()
        
        self.thirdOctet = Text(root, height=2, width=4).grid()
        
        self.label_dot3 = Label(root, text=".").grid()
        
        self.fourthOctet = Text(root, height=2, width=4).grid()
        
        self.button = Button(root, text="SAVE").grid()
        self.button = Button(root, text="EXIT", command=lambda :root.destroy()).grid()
