from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from Utilities import *

x = 520
y = 480
root = Tk()
root.geometry("%sx%s" % (x, y))
root.title("AD Menu")
root.resizable(width=False, height=False)
root.configure(background="#1E1E1E")
frame = tk.Frame(root, background="#838383")
frame.place(relwidth=0.95, relheight=0.84, rely=0.02, relx=0.5, anchor="n")
bottomBar = tk.Frame(root, background="#838383")
bottomBar.place(relwidth=0.95, relheight=0.10, rely=0.98, relx=0.5, anchor="s")
Utilities.mainFrame(frame, bottomBar)

frame.mainloop()
