from tkinter import *
import os

class setup(Frame):
    """
    The window which all frames are displayed on.
    """

    # Constructor
    def __init__(self, master: Tk) -> None:
        self.master = master


        self.create_setup_screen()



    def create_setup_screen(self) -> None:
        """
        """

        # Initialise the setup screen
        # Calls the Tk Frame Constructor
        super().__init__(self.master)

        title_label: Label
        title_label = Label(self, text="Crazy Maze")
        title_label.pack()

        options_frame: Frame
        options_frame = Frame(self)

        rows_slider: Scale
        self.rows: int
        rows_slider = Scale(options_frame, from_ = 0, to=100, orient=HORIZONTAL, command=self.on_row_slider_change)
        rows_slider.pack()

        columns_slider: Scale
        self.columns: int
        columns_slider = Scale(options_frame, from_ = 0, to=100, orient=HORIZONTAL,command=self.on_column_slider_change)
        columns_slider.pack()

        play_button: Button
        play_button = Button(options_frame, text="Play", command=self.start_game)
        play_button.pack(side=LEFT, expand=TRUE)

        exit_button: Button
        exit_button = Button(options_frame, text="Exit", command=self.master.quit)
        exit_button.pack(side=LEFT, expand=TRUE)

        options_frame.pack(side=BOTTOM, fill=X)


        self.pack(side=LEFT, fill=BOTH, expand=TRUE)

    def start_game(self) -> None:
        pass


    def on_row_slider_change(self,value):
        self.rows=value
        print(self.rows)

    def on_column_slider_change(self,value):
        self.columns=value
        print(self.columns)

