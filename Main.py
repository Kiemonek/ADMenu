from tkinter import *
from tkinter.ttk import *
from DashboardButton import *

def mainFrame():
    
    showButtonList(frame, "cmd")

    # Usable Buttons
    add_button = Button(frame, text = "Add New Button", command = lambda: [clear_frame(), addNewButton(frame)])
    add_button.grid()
    mod_button = Button(frame, text = "Modify Buttons" )
    mod_button.grid()
    rem_button = Button(frame, text = "Remove Button", command = lambda: [clear_frame(), removeButton(frame)])
    rem_button.grid()

############### Add Button Window ###############   
def addNewButton(frame):
    frame = frame
        
    label = Label(frame, text="Insert data")
    label.grid()
    
    label_name = Label(frame, text="Name:")
    label_name.grid()
    
    entry_name = Entry(frame)
    entry_name.insert(0, "test name")
    entry_name.grid()
    
    label_domain = Label(frame, text="Domain:")
    label_domain.grid()
    
    entry_domain = Entry(frame)
    entry_domain.insert(0, "test domain")
    entry_domain.grid()
    
    label_username = Label(frame, text="Username:")
    label_username.grid()
    
    entry_username = Entry(frame)
    entry_username.insert(0, "login")
    entry_username.grid()
    
    label_server = Label(frame, text="Server:")
    label_server.grid()
    
    entry_first_octet = Entry(frame)
    entry_first_octet.insert(0, "111")
    entry_first_octet.grid()
    
    label_dot = Label(frame, text=".")
    label_dot.grid()
    
    entry_second_octet = Entry(frame)
    entry_second_octet.insert(0, "222")
    entry_second_octet.grid()
    
    label_dot = Label(frame, text=".")
    label_dot.grid()
    
    entry_third_octet = Entry(frame)
    entry_third_octet.insert(0, "333")
    entry_third_octet.grid()
    
    label_dot = Label(frame, text=".")
    label_dot.grid()
    
    entry_fourth_octet = Entry(frame)
    entry_fourth_octet.insert(0, "444")
    entry_fourth_octet.grid()
    
    save_button = Button(frame, text="SAVE", command=lambda: [saveAddedButton(entry_name, entry_domain, entry_username, entry_first_octet, entry_second_octet, entry_third_octet, entry_fourth_octet), clear_frame(), mainFrame()])
    save_button.grid()
    
    exit_button = Button(frame, text="EXIT", command=lambda: [clear_frame(), mainFrame()])
    exit_button.grid()

def saveAddedButton(entry_name, entry_domain, entry_username, entry_first_octet, entry_second_octet, entry_third_octet, entry_fourth_octet):

        append_button = DashboardButton.getButtonList()
        
        new_title = entry_name.get()
        new_domain = entry_domain.get()
        new_username = entry_username.get()
        new_domain_controller = entry_first_octet.get() + "." + entry_second_octet.get() + "." + entry_third_octet.get() + "." + entry_fourth_octet.get()

        # Generate a unique id for the button
        if append_button:
            max_id = max(button.id for button in append_button)
            button_id = max_id + 1
        else:
            button_id = 0

        button = DashboardButton(
            id=button_id,
            root='',
            title=new_title,
            domain=new_domain,
            username=new_username,
            domain_controller=new_domain_controller
        )
        append_button.append(button)    
        
        DashboardButton.addButtonsToDB(append_button)

# NOTE: Remove Button Window   
def removeButton(frame):
    
    clear_frame()
    showButtonList(frame, "rm")
    # TODO: Add refresh after remove 
            
    exit_button = Button(frame, text="EXIT", command=lambda: [clear_frame(), mainFrame()])
    exit_button.grid()

# NOTE: Modify Button Window


############### Utilities ###############
def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

def showButtonList(frame, option):
    # Implement list from json
    buttonList = DashboardButton.getButtonList()
    
    # Button Generator
    for items in buttonList:
            button = Button(frame, text = items.title, command = lambda: [items.onPressed(option)])
            button.grid()

############### Customize Window ###############
root = Tk()
frame = Frame(root)
frame.pack()
root.title("AD Menu")
root.geometry("640x480")
mainFrame()
frame.mainloop()
