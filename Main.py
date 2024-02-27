from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from Utilities import *

x = 570
y = 480
root = Tk()
root.geometry("%sx%s" % (x, y))
root.title("AD Menu")
root.resizable(width=False, height=True)
frame = Frame(root)
frame.place(relwidth=1, relheight=0.6, rely=0)
bottomBar = tk.Frame(root, background="black")
bottomBar.place(relwidth=1, height=120, rely=1, relx=0.5, anchor="s")
Utilities.mainFrame(frame, bottomBar)

frame.mainloop()
