# TODO: add tkinter comment
from tkinter import *
import json
import codebank.src_scriptrunner.crazy_script_scanner as scanner

# Generic crazy import
import codebank.src_interface.crazy_colour_interface as cci

class setup_frame(Frame):
    """
    Extends Tk.Frame.

    Create the content for the Setup Frame.
    Allows the user to input the desired row and column size of the maze.
    Allows the user to decide the colour scheme for the program.
    """

    # Constructor
    def __init__(self, master: Tk, parent_window) -> None:
        self.master: Tk
        self.master = master

        self.maze_logic = parent_window.controller.game_logic

        self.parent_window = parent_window

        # Retrieve the colour scheme names from the Colour Schemes folder.
        self.colour_schemes: list(str)
        self.colour_schemes = cci.scan_colour_schemes()

        self.create_setup_screen()


    def create_setup_screen(self) -> None:
        """
        Initializes the main frame for the setup screen.
        Initializes the Game subframe which handles game parameters e.g. rows, columns, colour scheme.
        Initializes the Window subframe which handles window logic e.g. play game, exit
        """

        # Initialise the setup screen
        # Calls the Tk Frame Constructor
        super().__init__(self.master)

        # Create the game title on the top of the screen.
        title_label: Label
        title_label = Label(self, text="Crazy Maze")
        title_label.pack()

        # Create the Window subframe
        window_options_frame: Frame
        window_options_frame = self.create_window_options_frame()
        window_options_frame.pack(side=BOTTOM, fill=X)

        # Create the Game subframe
        game_options_frame: Frame
        game_options_frame = self.create_game_options_frame()
        game_options_frame.pack(side=BOTTOM, fill=X)

        self.pack(side=LEFT, fill=BOTH, expand=TRUE)

    def create_game_options_frame(self) -> Frame:
        """
        Create the game subframe.

        Initialise the row and column sliders.
        Initialise the colour scheme dropdown.
        """

        # Create a subframe to store the game options.
        game_options_frame: Frame
        game_options_frame = Frame(self)

        # Create a subframe to store information about the row.
        row_frame: Frame
        row_frame = Frame(game_options_frame)

        # Create a subframe to store information about the column.
        column_frame: Frame
        column_frame = Frame(game_options_frame)

        # Create a subframe to store information about the colour scheme.
        colour_scheme_frame: Frame
        colour_scheme_frame = Frame(game_options_frame)

        row_label: Label
        row_label = Label(row_frame, text="Rows: ")
        row_label.pack(side=LEFT)

        # Create a slider to represent the chosen number of rows.
        rows_slider: Scale
        self.rows: int = 8
        rows_slider = Scale(row_frame, from_ = 8, to=100, orient=HORIZONTAL, command=self.on_row_slider_change)
        rows_slider.pack(side=LEFT)

        row_frame.pack(side=LEFT, expand=TRUE)

        column_label: Label
        column_label = Label(column_frame, text="Columns: ")
        column_label.pack(side=LEFT)

        # Create a slider to represent the chosen number of columns.
        columns_slider: Scale
        self.columns: int = 8
        columns_slider = Scale(column_frame, from_ = 8, to=100, orient=HORIZONTAL,command=self.on_column_slider_change)
        columns_slider.pack(side=LEFT)

        column_frame.pack(side=LEFT, expand=TRUE)

        colour_scheme_label: Label
        colour_scheme_label = Label(colour_scheme_frame, text="Colour Scheme: ")
        colour_scheme_label.pack(side=LEFT)

        # Create a variable to store the selected colour scheme title.
        self.selected_colour_scheme: StringVar
        self.selected_colour_scheme = StringVar(colour_scheme_frame)
        self.selected_colour_scheme.set(self.colour_schemes[0])

        # Create a dropdown box to allow the user to choose a colour scheme.
        colour_scheme_dropdown: OptionMenu
        colour_scheme_dropdown = OptionMenu(colour_scheme_frame, self.selected_colour_scheme, *self.colour_schemes)  
        colour_scheme_dropdown.pack(side=LEFT) 

        colour_scheme_frame.pack(side=LEFT, expand=TRUE)

        self.create_game_modes(game_options_frame)

        self.create_maze_generation_options(game_options_frame)

        return game_options_frame
    
    def create_maze_generation_options(self, game_options_frame):
        maze_generation_list = scanner.find_scripts()

        maze_generation_frame = Frame(game_options_frame)

        maze_generation_label: Label
        maze_generation_label = Label(maze_generation_frame, text="Maze Generation: ")
        maze_generation_label.pack(side=LEFT)

        # Create a variable to store the selected colour scheme title.
        self.selected_maze_generation: StringVar
        self.selected_maze_generation = StringVar(maze_generation_frame)
        self.selected_maze_generation.set(maze_generation_list[0])

        # Create a dropdown box to allow the user to choose a colour scheme.
        maze_generation_dropdown: OptionMenu
        maze_generation_dropdown = OptionMenu(maze_generation_frame, self.selected_maze_generation, *maze_generation_list)  
        maze_generation_dropdown.pack(side=LEFT) 

        maze_generation_frame.pack(side=LEFT, expand=TRUE)



    def create_game_modes(self, frame) -> None:
        self.options = ["CRAZY CONTROLS", "CRAZY COLLISION", "CRAZY POWERUPS"]

        self.option_vars = [IntVar() for _ in self.options]

        for i, option in enumerate(self.options):
            Checkbutton(frame, text=option, variable=self.option_vars[i], command=self.submit_game_modes).pack(anchor=W)

        self.result_label = Label(frame, text="")
        self.result_label.pack()
        pass

    def submit_game_modes(self):
        selected_options = []
        for i, option_var in enumerate(self.option_vars):
            if option_var.get() == 1:
                selected_options.append(self.options[i])
        
    def reformat_game_modes(self, game_mode_names, game_mode_options) -> str:

        game_mode_request = {}

        for name in range(0, len(game_mode_names)):
            key = game_mode_names[name]
            game_mode_request[key] = game_mode_options[name].get()

        # Convert the dictionary to JSON format
        json_data = json.dumps(game_mode_request)

        return json_data




    

    def create_window_options_frame(self) -> Frame:
        """
        Create the window subframe.

        Allow the user to play the game.
        Allow the user to exit the program.
        """
        window_options_frame: Frame
        window_options_frame = Frame(self)

        # Create a button to allow the user to play the game.
        play_button: Button
        play_button = Button(window_options_frame, text="Play", command=self.start_game)
        play_button.pack(side=LEFT, expand=TRUE)

        # Create a button to allow the user to exit.
        exit_button: Button
        exit_button = Button(window_options_frame, text="Exit", command=self.master.quit)
        exit_button.pack(side=LEFT, expand=TRUE)

        return window_options_frame

    def start_game(self) -> None:
        """
        Change the frame to the script setup screen.
        """



        game_modes_dictionary = self.reformat_game_modes(self.options, self.option_vars)


        self.maze_logic.initialize_game(self.rows, self.columns, game_modes_dictionary, self.selected_maze_generation.get())

        self.parent_window.change_frame("crazy_script_display")



    def on_row_slider_change(self,value:str) -> None:
        """
        Change the value of the row variable.
        """
        self.rows=int(value)

    def on_column_slider_change(self,value:str) -> None:
        """
        Change the value of the column variable.
        """
        self.columns=int(value)



