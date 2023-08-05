# Import the setup screen
from crazy_window import window
from crazy_maze_logic import maze_logic

class controller():
    def __init__(self) -> None:

        game_logic: maze_logic
        game_logic = maze_logic()

        main_window: window
        main_window = window(game_logic)




