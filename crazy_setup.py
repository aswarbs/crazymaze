from tkinter import *

class setup:
    """
    The window which all frames are displayed on.
    """

    # Constructor
    def __init__(self) -> None:

        # Initiating the Tk Instance
        self.master = Tk()
        self.master.attributes("-fullscreen", True)
        self.master.configure(background="white")  
        self.master.title("Crazy Maze")
        

        self.create_setup_screen()
        self.master.mainloop()

    def create_setup_screen(self) -> None:

        frame = Frame(self.master)
        frame.pack()

