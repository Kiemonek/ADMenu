"""Main file of the application. It creates the main window and frames of the application."""
from tkinter import Tk, Frame
from app.top_bar import ShowButtons as sb
from app.bottom_bar import BottomBar
import app.constants as cons

root = Tk()
root.geometry(f"{cons.WINDOW_WIDTH}x{cons.WINDOW_HEIGHT}")
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
sb.show_button_list(None, top_frame, "cmd")

BottomBar.bottom_bar(self=root, top_frame=top_frame, bottom_frame=bottom_frame)

root.mainloop()
