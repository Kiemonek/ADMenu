# import json
from tkinter import *
from DashboardButton import DashboardButton
# from Main import refresh
# import Main

class AddNewButton():
    
    def __init__(self, root):
        self.root = root
        self.root.title("Add new button")
        self.root.geometry("200x500")
        
        self.label = Label(root, text="Insert data")
        self.label.grid()
        
        self.label_name = Label(root, text="Name:")
        self.label_name.grid()
        
        self.entry_name = Entry(root)
        self.entry_name.insert(0, "test name")
        self.entry_name.grid()
        
        self.label_domain = Label(root, text="Domain:")
        self.label_domain.grid()
        
        self.entry_domain = Entry(root)
        self.entry_domain.insert(0, "test domain")
        self.entry_domain.grid()
        
        self.label_username = Label(root, text="Username:")
        self.label_username.grid()
        
        self.entry_username = Entry(root)
        self.entry_username.insert(0, "login")
        self.entry_username.grid()
        
        self.label_server = Label(root, text="Server:")
        self.label_server.grid()
        
        self.entry_first_octet = Entry(root)
        self.entry_first_octet.insert(0, "111")
        self.entry_first_octet.grid()
        
        self.label_dot = Label(root, text=".")
        self.label_dot.grid()
        
        self.entry_second_octet = Entry(root)
        self.entry_second_octet.insert(0, "222")
        self.entry_second_octet.grid()
        
        self.label_dot = Label(root, text=".")
        self.label_dot.grid()
        
        self.entry_third_octet = Entry(root)
        self.entry_third_octet.insert(0, "333")
        self.entry_third_octet.grid()
        
        self.label_dot = Label(root, text=".")
        self.label_dot.grid()
        
        self.entry_fourth_octet = Entry(root)
        self.entry_fourth_octet.insert(0, "444")
        self.entry_fourth_octet.grid()
        
        self.save_button = Button(root, text="SAVE", command=lambda: [AddNewButton.save(self), root.destroy()])
        self.save_button.grid()
        
        self.exit_button = Button(root, text="EXIT", command=lambda: root.destroy())
        self.exit_button.grid()
        
    def save(self):

        append_button = DashboardButton.getButtonList()
        
        new_title = self.entry_name.get()
        new_domain = self.entry_domain.get()
        new_username = self.entry_username.get()
        new_domain_controller = self.entry_first_octet.get() + "." + self.entry_second_octet.get() + "." + self.entry_third_octet.get() + "." + self.entry_fourth_octet.get()

        button = DashboardButton(
            root='',
            title=new_title,
            domain=new_domain,
            username=new_username,
            domain_controller=new_domain_controller
        )
        append_button.append(button)    
        
        DashboardButton.addButtonsToDB(append_button)
