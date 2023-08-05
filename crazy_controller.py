# Import the setup screen
from crazy_window import game_window
from crazy_maze_logic import maze_logic

class controller():
    def __init__(self) -> None:

        game_logic: maze_logic
        game_logic = maze_logic()

        main_window: game_window
        main_window = game_window(maze_logic)




