# TODO: add tkinter comment
from tkinter import *


class game_frame(Frame):
    """
    Display the game to the screen.
    Display game options to the screen, e.g. return to main menu
    """

    def __init__(self, master:Tk, parent_window) -> None:
        self.master: Tk
        self.master = master

        self.logic = parent_window.maze_logic
        self.controller = parent_window.controller

        self.parent_window = parent_window

        self.master.bind("<KeyRelease>", self.controller.on_key_released)

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
        self.grid_dimensions = self.logic.maze.get_maze_dimensions()

        # Determine the screen resolution
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the desired square size based on the grid and the screen resolution
        square_size = min(screen_width // self.grid_dimensions[1], screen_height // self.grid_dimensions[0])

        # Calculate the dimensions of each grid cell
        self.cell_width = square_size
        self.cell_height = square_size

        # Calculate the width and height of the canvas
        width = self.grid_dimensions[1] * self.cell_width
        height = self.grid_dimensions[0] * self.cell_height

        # Create a canvas to store the maze on.
        self.canvas = Canvas(self, width=width, height=height, bg="white")
        self.canvas.pack()  # Pack the canvas inside the frame

        self.draw_grid(self.grid_dimensions)


    def draw_grid(self, dimensions: tuple[int, int]) -> None:
        """
        Draw the maze grid to the canvas.
        """

        # For each square in the grid,
        for row in range(dimensions[0]):
            for col in range(dimensions[1]):
                # Calculate the coordinates of the rectangle.
                x1 = col * self.cell_width
                y1 = row * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height

                # Retrieve if the square is path or wall.
                is_cell_path = self.logic.maze.get_maze_cell(row, col)
                # If the square is path, it is green.
                # If the square is wall, it is red.
                if is_cell_path:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red")

        player1_x = self.logic.player1.position[1]
        player1_y = self.logic.player1.position[0]
        player1_x1 = player1_x * self.cell_width
        player1_y1 = player1_y * self.cell_height
        player1_x2 = player1_x1 + self.cell_width
        player1_y2 = player1_y1 + self.cell_height

        player2_x = self.logic.player2.position[1]
        player2_y = self.logic.player2.position[0]
        player2_x1 = player2_x * self.cell_width
        player2_y1 = player2_y * self.cell_height
        player2_x2 = player2_x1 + self.cell_width
        player2_y2 = player2_y1 + self.cell_height
        
        self.player1_sprite = self.canvas.create_oval(player1_x1, player1_y1, player1_x2, player1_y2, outline="black", fill=self.logic.player1.colour)
        self.player2_sprite = self.canvas.create_oval(player2_x1, player2_y1, player2_x2, player2_y2, outline="black", fill=self.logic.player2.colour)


    def update_position(self, player_id, change_x, change_y):

        if(player_id == 0):
            player_x = self.logic.player1.position[1]
            player_y = self.logic.player1.position[0]
        elif (player_id==1):
            player_x = self.logic.player2.position[1]
            player_y = self.logic.player2.position[0]

        current_x = player_x + change_x
        current_y = player_y + change_y

        if(current_x < 0 or current_x > self.grid_dimensions[1]):
            return False
        
        if(current_y < 0 or current_y > self.grid_dimensions[0]):
            return False
        
        if(not self.logic.maze.get_maze_cell(current_y, current_x)):
            return False
        
        if(player_id == 0):
            self.canvas.move(self.player1_sprite, (change_x * self.cell_width), (change_y * self.cell_height))
        elif(player_id == 1):
            self.canvas.move(self.player2_sprite, (change_x * self.cell_width), (change_y * self.cell_height))

        return True

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

    