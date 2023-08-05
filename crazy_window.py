from tkinter import *
from crazy_setup import setup

class window():
    def __init__(self) -> None:
        # Initiating the Tk Instance
        self.master: Tk
        self.master = Tk()

        # Make the window fullscreen
        self.master.attributes("-fullscreen", True)

        # Make the window white
        self.master.configure(background="white") 

        self.master.title("Crazy Maze")

        self.current_frame: setup
        self.current_frame = setup(self.master)

        # Start the tk instance
        self.master.mainloop()
