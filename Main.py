from tkinter import *
from tkinter.ttk import *
import os

domain = 'dom.ain\\'
username = 'uname'
domainController = '192.168.111.10'

def connect():
        
    print ("uwu")
    #command = 'runas /netonly /user:' + domain + username +' "mmc dsa.msc /server='+ domainController +'" '
    #os.system(command)
        
root = Tk()

root.geometry("400x200+200+100")
root.title("AD Menu")

spc = Label(root, text="   ")
spc.grid(column=0, row=0)
butt1 = Button(root, text="Client1", command=connect)
#butt1.grid(column=2, row=1)
butt2 = Button(root, text="Client2", command=connect)
butt2.grid(column=4, row=1)
butt3 = Button(root, text="Client3", command=connect)
butt3.grid(column=2, row=3)
butt4 = Button(root, text="Client4", command=connect)
butt4.grid(column=4, row=3)
butt5 = Button(root, text="Client5", command=connect)
butt5.grid(column=2, row=5)
butt6 = Button(root, text="Client6", command=connect)
butt6.grid(column=4, row=5)

butt1.grid(row=0, column=0, sticky="NESW")
butt1.grid_rowconfigure(0, weight=1)
butt1.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


root.mainloop()