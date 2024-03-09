"""Main file of the application. It creates the main window and frames of the application."""
from tkinter import Tk, Frame
from app.utilities import Utilities
from app.bottom_bar import BottomBar
import app.constants as constants

root = Tk()
root.geometry(f"{constants.WINDOW_WIDTH}x{constants.WINDOW_HEIGHT}")
root.title("AD Menu")
root.resizable(width=False, height=False)
root.configure(background="#1E1E1E")
top_frame = Frame(root, background="#838383")
top_frame.place(relwidth=0.95, relheight=0.84, rely=0.02, relx=0.5, anchor="n")
bottom_frame = Frame(root, background="#838383")
bottom_frame.place(relwidth=0.95,
                   relheight=0.10,
                   rely=0.98,
                   relx=0.5,
                   anchor="s")
Utilities.show_button_list(top_frame, "cmd")

BottomBar.bottom_bar(self=root, top_frame=top_frame, bottom_frame=bottom_frame)

root.mainloop()
