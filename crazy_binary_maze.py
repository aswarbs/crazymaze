
class binary_maze():

    def __init__(self, *args, **kwargs) -> None:
        
        # Getting the maze width
        self.maze_width: int
        try: self.maze_width = kwargs.get("width")
        except: raise ValueError("binary_maze: maze intantiation, keyword 'width' not found")

        # Getting the maze height
        self.maze_height: int
        try: self.maze_height = kwargs.get("height")
        except: raise ValueError("binary_maze: maze intantiation, keyword 'height' not found")
