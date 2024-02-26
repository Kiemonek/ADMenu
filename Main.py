from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from Utilities import *

x = 640
y = 480
root = Tk()
root.geometry("%sx%s" % (x, y))
root.title("AD Menu")
frame = Frame(root)
frame.pack(side=TOP, expand=True, fill=BOTH)
bBar = 0.5 * y
bottomBar = tk.Frame(root, background='black')
bottomBar.pack(side=BOTTOM, expand=True, fill=BOTH)
Utilities.mainFrame(frame, bottomBar)

frame.mainloop()
