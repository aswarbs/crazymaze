from tkinter import *
import crazy_colour_interface as cci

class setup(Frame):
    """
    The window which all frames are displayed on.
    """

    # Constructor
    def __init__(self, master: Tk) -> None:
        self.master = master

        self.colour_schemes: list(str)
        self.colour_schemes = cci.scan_colour_schemes()

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

        window_options_frame: Frame
        window_options_frame = self.create_window_options_frame()
        window_options_frame.pack(side=BOTTOM, fill=X)

        game_options_frame: Frame
        game_options_frame = self.create_game_options_frame()
        game_options_frame.pack(side=BOTTOM, fill=X)


        self.pack(side=LEFT, fill=BOTH, expand=TRUE)

    def create_game_options_frame(self) -> Frame:
        game_options_frame: Frame
        game_options_frame = Frame(self)

        row_frame: Frame
        row_frame = Frame(game_options_frame)

        column_frame: Frame
        column_frame = Frame(game_options_frame)

        colour_scheme_frame: Frame
        colour_scheme_frame = Frame(game_options_frame)

        row_label: Label
        row_label = Label(row_frame, text="Rows: ")
        row_label.pack(side=LEFT)

        rows_slider: Scale
        self.rows: int
        rows_slider = Scale(row_frame, from_ = 0, to=100, orient=HORIZONTAL, command=self.on_row_slider_change)
        rows_slider.pack(side=LEFT)

        row_frame.pack(side=LEFT, expand=TRUE)

        column_label: Label
        column_label = Label(column_frame, text="Columns: ")
        column_label.pack(side=LEFT)

        columns_slider: Scale
        self.columns: int
        columns_slider = Scale(column_frame, from_ = 0, to=100, orient=HORIZONTAL,command=self.on_column_slider_change)
        columns_slider.pack(side=LEFT)

        column_frame.pack(side=LEFT, expand=TRUE)

        colour_scheme_label: Label
        colour_scheme_label = Label(colour_scheme_frame, text="Colour Scheme: ")
        colour_scheme_label.pack(side=LEFT)

        # TODO: read dropdown options from file
        
        self.selected_colour_scheme: StringVar
        self.selected_colour_scheme = StringVar(colour_scheme_frame)
        self.selected_colour_scheme.set(self.colour_schemes[0])

        colour_scheme_dropdown: OptionMenu
        colour_scheme_dropdown = OptionMenu(colour_scheme_frame, self.selected_colour_scheme, self.colour_schemes)  
        colour_scheme_dropdown.pack(side=LEFT) 

        colour_scheme_frame.pack(side=LEFT, expand=TRUE)
        return game_options_frame
    


    

    def create_window_options_frame(self) -> Frame:
        window_options_frame: Frame
        window_options_frame = Frame(self)

        play_button: Button
        play_button = Button(window_options_frame, text="Play", command=self.start_game)
        play_button.pack(side=LEFT, expand=TRUE)

        exit_button: Button
        exit_button = Button(window_options_frame, text="Exit", command=self.master.quit)
        exit_button.pack(side=LEFT, expand=TRUE)

        return window_options_frame

    def start_game(self) -> None:
        pass


    def on_row_slider_change(self,value:int):
        self.rows=value

    def on_column_slider_change(self,value:int):
        self.columns=value

