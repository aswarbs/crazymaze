# TODO: add tkinter comment
from tkinter import *


class game_frame(Frame):

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

        game_options_frame: Frame
        game_options_frame = self.create_game_options()
        game_options_frame.pack()

        self.create_game_canvas()

        self.pack(fill=BOTH, expand=TRUE)

    def create_game_canvas(self):

        grid_dimensions = self.logic.maze.get_maze_dimensions()
        square_size = 50  # Size of each square in pixels
        width = grid_dimensions[0] * square_size
        height = grid_dimensions[1] * square_size

        canvas = Canvas(self, width=width, height=height, bg="white")
        canvas.pack()

        self.draw_grid(canvas, grid_dimensions, width, height)

    def draw_grid(self, canvas, dimensions, width, height):
        square_width = width // dimensions[0]
        square_height = height // dimensions[1]
        
        for row in range(dimensions[0]):
            for col in range(dimensions[1]):
                x1 = col * square_width
                y1 = row * square_height
                x2 = x1 + square_width
                y2 = y1 + square_height

                is_cell_path = self.logic.maze.get_maze_cell(row, col)
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
        self.parent_window.change_frame("crazy_setup")

    