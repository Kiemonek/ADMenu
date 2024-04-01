"""Main file of the application. It creates the main window and frames of the application."""
from tkinter import Tk, Frame
from app.top_bar import TopBar
from app.bottom_bar import BottomBar
from utilities.window_config import WinConfig


def main():
    """Main function of the application."""
    root = Tk()
    top_frame = Frame(root)
    bottom_frame = Frame(root)

    WinConfig(root, top_frame, bottom_frame)

    TopBar.show_button_list(None, top_frame, "cmd")
    BottomBar.bottom_bar(None, top_frame, bottom_frame)

    root.mainloop()


if __name__ == "__main__":
    main()
