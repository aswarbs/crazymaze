# TODO: add tkinter comment
from tkinter import *


class game_frame(Frame):
    """
    Display the game to the screen.
    Display game options to the screen, e.g. return to main menu
    """

    def __init__(self, master:Tk, parent_window, maze_logic) -> None:
        self.master: Tk
        self.master = master

        self.logic = maze_logic

        self.parent_window = parent_window

        self.create_game_screen()

    def create_game_screen(self) -> None:
        """
        Initialize the frame which will hold the game and options.
        """

        # Initialise the game screen
        # Calls the Tk Frame Constructor
        super().__init__(self.master)

        # Create the frame which will hold the game options.
        game_options_frame: Frame
        game_options_frame = self.create_game_options()
        game_options_frame.pack(side=LEFT)

        self.create_game_canvas()

        self.pack(fill=BOTH, expand=TRUE)

    def create_game_canvas(self) -> None:
        """
        Create the canvas which stores the game maze.
        """

        # Retrieve the dimensions of the grid
        grid_dimensions:tuple[int,int]
        grid_dimensions = self.logic.maze.get_maze_dimensions()

        # Determine the screen resolution
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the desired square size based on the grid and the screen resolution
        square_size = min(screen_width // grid_dimensions[0], screen_height // grid_dimensions[1])

        # Calculate the width and height of the canvas
        width:int
        width = grid_dimensions[0] * square_size
        height:int
        height = grid_dimensions[1] * square_size

        # Create a canvas to store the maze on.
        canvas:Canvas
        canvas = Canvas(self, width=width, height=height, bg="white")
        canvas.pack()

        self.draw_grid(canvas, grid_dimensions, width, height)

    def draw_grid(self, canvas:Canvas, dimensions:tuple[int,int], width:int, height:int) -> None:
        """
        Draw the maze grid to the canvas.
        """

        # Determine the width and height of the square.
        square_width: float
        square_width = width // dimensions[0]
        square_height:float
        square_height = height // dimensions[1]
        
        # For each square in the grid,
        for row in range(dimensions[0]):
            for col in range(dimensions[1]):

                # Calculate the coordinates of the square.
                x1:int = col * square_width
                y1:int = row * square_height
                x2:int = x1 + square_width
                y2:int = y1 + square_height

                # Retrieve if the square is path or wall.
                is_cell_path:bool = self.logic.maze.get_maze_cell(row, col)

                # If the square is path, it is green.
                # If the square is wall, it is red.
                if(is_cell_path):
                    canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red")

                

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
        """
        Return to the main setup menu.
        """
        self.parent_window.change_frame("crazy_setup")

    