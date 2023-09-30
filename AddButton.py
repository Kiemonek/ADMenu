from tkinter import *
from tkinter.ttk import *
import json

class AddButton:
    
    def __init__(self, root, title, domain, username, domain_controller):
        self.root = root
        self.title = title
        self.domain = domain
        self.username = username
        self.domain_controller = domain_controller
    
    def toJson(self):
    # Create a dictionary with the relevant attributes
        button_dictionary = {
        "title": self.title,
        "domain": self.domain,
        "username": self.username,
        "domain_controller": self.domain_controller
    }
