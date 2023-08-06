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

        # Bind key releases to a method in controller which will handle the corresponding actions.
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
        square_size = min(screen_width // self.grid_dimensions[0], screen_height // self.grid_dimensions[1])

        # Calculate the dimensions of each grid cell
        self.cell_width = square_size
        self.cell_height = square_size

        # Calculate the width and height of the canvas based on the grid and cell size
        width = self.grid_dimensions[1] * self.cell_width
        height = self.grid_dimensions[0] * self.cell_height

        # Create a canvas to store the maze on.
        self.canvas = Canvas(self, width=width, height=height, bg="red")
        self.canvas.pack()  # Pack the canvas inside the frame

        self.draw_grid()


    def draw_grid(self) -> None:
        """
        Draw the maze grid to the canvas.
        """

        # Clear the canvas before drawing the grid
        self.canvas.delete("all")

        # For each square in the grid,
        for row in range(self.grid_dimensions[0]):
            for col in range(self.grid_dimensions[1]):
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
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="")

        # Draw the first player to the screen.
        player1_position = self.logic.player1.position
        player1_colour = self.logic.player1.colour
        self.player1_sprite = self.create_sprite(player1_position, player1_colour, "player")

        # Draw the second player to the screen.
        player2_position = self.logic.player2.position
        player2_colour = self.logic.player2.colour
        self.player2_sprite = self.create_sprite(player2_position, player2_colour, "player")

        # Draw the goal to the screen.
        self.goal_position = self.logic.maze.get_goal_position()
        goal_colour = "#FFFFFF"
        self.create_sprite(self.goal_position, goal_colour, "goal")

    def handle_win_condition(self, player_id: int):
        if player_id == 0:
            self.player1_score += 1
            self.player1_score_label.config(text=self.player1_score)
        elif player_id == 1:
            self.player2_score += 1
            self.player2_score_label.config(text=self.player2_score)

        # Reset the maze
        self.logic.initialize_game(self.grid_dimensions[0], self.grid_dimensions[1])
        self.draw_grid()


    def create_sprite(self, tuple:[int,int], colour:str, type:str) -> int:
        """
        Create a sprite on the screen in the corresponding tuple position, with the corresponding colour.
        """

        # Retrieve the x and y coordinates from the tuple.
        x = tuple[1]
        y = tuple[0]

        # Calculate the boundaries of the shape.
        x1 = x * self.cell_width
        y1 = y * self.cell_height
        x2 = x1 + self.cell_width
        y2 = y1 + self.cell_height

        # Create and return the corresponding sprite.
        if(type == "player"):
            sprite = self.canvas.create_oval(x1, y1, x2, y2, outline="black", fill=colour)
        else:
            sprite = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=colour)
        return sprite


    def update_position(self, player_id:int, change_x:int, change_y:int) -> bool:
        """
        Update the position of a player on the screen.
        """

        # Retrieve the coordinates from the corresponding player.
        if(player_id == 0):
            player_x = self.logic.player1.position[1]
            player_y = self.logic.player1.position[0]
        elif (player_id==1):
            player_x = self.logic.player2.position[1]
            player_y = self.logic.player2.position[0]

        # Calculate the new coordinates of the player.
        current_x = player_x + change_x
        current_y = player_y + change_y

        # If the x coordinate is not in the maze, return false.
        if(current_x < 0 or current_x > self.grid_dimensions[1]):
            return False
        
        # If the y coordinate is not in the maze, return false.
        if(current_y < 0 or current_y > self.grid_dimensions[0]):
            return False
        
        # If the coordinate is not a valid path, return false.
        if(not self.logic.maze.get_maze_cell(current_y, current_x)):
            return False
        
        # If a player has hit the goal, handle the win condition
        if(current_x == self.goal_position[1] and current_y == self.goal_position[0]):
            self.handle_win_condition(player_id)
            return False
        
        # Else, move the position of the corresponding player on the screen.
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

        score_frame = Frame(game_options_frame)

        player1_frame = Frame(score_frame)

        player1_label = Label(player1_frame, text="Player 1")
        player1_label.pack()

        self.player1_score = 0
        self.player1_score_label = Label(player1_frame, text=self.player1_score)
        self.player1_score_label.pack()

        player1_frame.pack(side=LEFT)

        player2_frame = Frame(score_frame)

        player2_label = Label(player2_frame, text="Player 2")
        player2_label.pack()

        self.player2_score = 0
        self.player2_score_label = Label(player2_frame, text=self.player2_score)
        self.player2_score_label.pack()

        player2_frame.pack(side=LEFT)

        score_frame.pack(side=TOP)
        
        back_button: Button
        back_button = Button(game_options_frame, text="Back", command=self.return_to_setup)
        back_button.pack()


        return game_options_frame

    def return_to_setup(self) -> None:
        """
        Return to the main setup menu.
        """
        self.parent_window.change_frame("crazy_setup")

    