
from crazy_generator_dfs import *

class maze_logic():

    def __init__(self) -> None:
        pass


    def initialize_game(self, row:int, column:int) -> None:
        self.maze = generate_maze_dfs(row, column)

        self.player1: dict[str,type]
        self.player1 = self.initialise_player(0)

        self.player2: dict[str,type]
        self.player2 = self.initialise_player(1)

        self.players = [self.player1, self.player2]

    def initialise_player(self, id:int) -> tuple[int,int]:
        player = {
            "position":self.maze.get_player_spawn(id),
            "colour":self.generate_random_hex()
        }
        return player
    
    def generate_random_hex(self) -> str:
        """
        Generate a random color in hexadecimal format (#RRGGBB).
        """
        # Generate random values for red, green, and blue components
        red:int = random.randint(0, 255)
        green:int = random.randint(0, 255)
        blue:int = random.randint(0, 255)

        # Convert the values to hexadecimal format and concatenate them
        color_hex:str = f"#{red:02x}{green:02x}{blue:02x}"

        return color_hex