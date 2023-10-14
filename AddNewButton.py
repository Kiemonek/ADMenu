# import json
from tkinter import *
    
class AddNewButton():
    global appendButton 
    # appendButton = []
    
    def __init__(self, root):
        self.root = root
        self.root.title("Add new button")
        self.root.geometry("200x500")
        
        self.label = Label(root, text="Insert data")
        self.label.grid()
        
        self.label_Name = Label(root, text="Name:")
        self.label_Name.grid()
        
        self.e_Name = Entry(root)
        self.e_Name.grid()
        
        self.label_Domain = Label(root, text="Domain:")
        self.label_Domain.grid()
        
        self.e_Domain = Entry(root)
        self.e_Domain.grid()
        
        self.label_Username = Label(root, text="Username:")
        self.label_Username.grid()
        
        self.e_Username = Entry(root)
        self.e_Username.grid()
        
        self.label_Server = Label(root, text="Server:")
        self.label_Server.grid()
        
        self.e_fOctet = Entry(root)
        self.e_fOctet.grid()
        
        self.label_dot1 = Label(root, text=".")
        self.label_dot1.grid()
        
        self.e_sOctet = Entry(root)
        self.e_sOctet.grid()
        
        self.label_dot2 = Label(root, text=".")
        self.label_dot2.grid()
        
        self.e_tOctet = Entry(root)
        self.e_tOctet.grid()
        
        self.label_dot3 = Label(root, text=".")
        self.label_dot3.grid()
        
        self.e_foOctet = Entry(root)
        self.e_foOctet.grid()
        
        self.saveButton = Button(root, text="SAVE", command=self.save)
        self.saveButton.grid()
        
        self.exitButton = Button(root, text="EXIT", command=lambda :root.destroy())
        self.exitButton.grid()
        
    def save(self):
        # return
        # server = self.e_fOctet.get() + "." + self.e_sOctet.get() + "." + self.e_tOctet.get() + "." + self.e_foOctet.get()
        # print(server)
        appendButton = [
            None, 
            self.e_Name.get(), 
            self.e_Domain.get(), 
            self.e_Username.get(),
            self.e_fOctet.get() + "." + self.e_sOctet.get() + "." + self.e_tOctet.get() + "." + self.e_foOctet.get()
            ]
        print(appendButton)
        