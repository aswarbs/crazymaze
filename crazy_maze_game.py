from tkinter import *

class game(Frame):

    def __init__(self, master:Tk, parent_window) -> None:
        self.master: Tk
        self.master = master

        self.parent_window = parent_window

        self.create_game_screen()

    def create_game_screen(self) -> None:
        """
        Initialize the frame which will hold the game and options.
        """

        # Initialise the game screen
        # Calls the Tk Frame Constructor
        super().__init__(self.master)

        game_options_frame: Frame
        game_options_frame = self.create_game_options()
        game_options_frame.pack()

        self.pack(fill=BOTH, expand=TRUE)

    def create_game_options(self) -> Frame:
        """
        Initialize the frame which will hold the game options.
        """

        game_options_frame: Frame
        game_options_frame = Frame(self)

        back_button: Button
        back_button = Button(game_options_frame, text="Back", command=self.return_to_setup)
        back_button.pack()

        return game_options_frame

    def return_to_setup(self) -> None:
        self.parent_window.change_frame("crazy_setup")

    