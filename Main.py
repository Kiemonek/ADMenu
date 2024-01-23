from tkinter import *
from tkinter.ttk import *
from DashboardButton import *

root = Tk()
frame = Frame(root)
frame.pack()
root.title("AD Menu")
root.geometry("640x480")
DashboardButton.mainFrame(frame)

frame.mainloop()
