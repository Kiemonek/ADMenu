from tkinter import *
from tkinter.ttk import *
import os

domain = 'dom.ain\\'
username = 'uname'
domainController = '192.168.111.10'

def connect():
        
    command = 'runas /netonly /user:' + domain + username +' "mmc dsa.msc /server='+ domainController +'" '
    os.system(command)
        
root = Tk()

root.geometry("400x200+200+100")
root.title("AD Menu")

butt1 = Button(root, text="Client", command=connect)
butt1.pack()

root.mainloop()