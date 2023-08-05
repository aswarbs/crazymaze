
from crazy_generator_dfs import *

class maze_logic():

    def __init__(self) -> None:
        pass

    def generate_maze(self, width:int, height:int) -> None:
        self.maze = generate_maze_dfs(width, height)
        print(self.maze)