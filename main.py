"""Main file of the application. It creates the main window and frames of the application."""
from tkinter import Tk, Frame
from app.utilities import Utilities

WINDOW_WIDTH = 520
WINDOW_HEIGHT = 480

root = Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.title("AD Menu")
root.resizable(width=False, height=False)
root.configure(background="#1E1E1E")
frame = Frame(root, background="#838383")
frame.place(relwidth=0.95, relheight=0.84, rely=0.02, relx=0.5, anchor="n")
bottom_bar = Frame(root, background="#838383")
bottom_bar.place(relwidth=0.95,
                 relheight=0.10,
                 rely=0.98,
                 relx=0.5,
                 anchor="s")
Utilities.main_frame(root, bottom_bar)

root.mainloop()
