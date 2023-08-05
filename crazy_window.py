from tkinter import *

from crazy_maze_game import game
from crazy_setup import setup

class window():
    def __init__(self) -> None:
        # Initiating the Tk Instance
        self.master: Tk
        self.master = Tk()

        self.init_frames_dictionary()

        # Make the window fullscreen
        self.master.attributes("-fullscreen", True)

        # Make the window white
        self.master.configure(background="white") 

        self.master.title("Crazy Maze")

        self.current_frame: setup
        self.current_frame = setup(self.master, self)

        # Start the tk instance
        self.master.mainloop()

    def init_frames_dictionary(self) -> None:
        """
        Initialise a dictionary converting classes to Strings to avoid circular imports.
        """
        self.class_names:dict[str, type]
        self.class_names = {
             "crazy_maze_game": game,
             "crazy_setup": setup
        }

    def change_frame(self, new_frame_name:str):
            """
            Switches the currently hosted frame.
            """
            self.current_frame.pack_forget()
            frame = self.class_names.get(new_frame_name)
            self.current_frame = frame(self.master, self)
            self.current_frame.pack()


