# JSON is a module to serialize/deserialize JSON data
# It's used here to load and save mazes and their associated data
# Documentation: https://docs.python.org/3/library/json.html
import json

# Random is a module used to generate random numbers
# Here it is used to generate random noise mazes (there are incompleteable, just for testing)
# Documentation: https://docs.python.org/3/library/random.html
import random

DEFAULT_MAZE_BLOCK = '-'

class binary_maze():
    """
    binary_maze is a class to represent and handle binary mazes.

    This class allows you to create and manage binary mazes. A binary maze is a grid-based maze
    where each cell can either be open (True) or blocked (False). It also supports saving and
    loading maze data from a JSON file. To access each cell please use the provided getter and 
    setter functions.
    """

    def __init__(self, *args, **kwargs) -> None|Exception:
        """
        constructor for the binary_maze class. provide different keyword arguments to either create a new
        maze of 2 dimensions, or load an existing maze from a file:
            - if "path" keyword is provided, it will load the maze from a JSON file with the given path.
            - if "width" and "height" keywords are provided, it will create a new maze with the given dimensions.
            - if "random" and "width" and "height" keywords, it will fill the maze with random noise (impossible to complete)

        if neither keywords are provided, a value exception will be thrown

        example usage (loading from file):
            maze_instance = binary_maze(path = "maze_data.json")

        example usage (creating from dimensions):
            maze_instance = binary_maze(width = 10, height=8)
        """

        if "path" in kwargs:
            self._create_maze_from_file(kwargs)
        
        elif "width" in kwargs and "height" in kwargs:
            self._create_maze_from_dimensions(kwargs)

        else:
            return ValueError("binary_maze: failed to initialize, no relevant keyword argument")

    def __repr__(self) -> str:
        """
        provides the string representation of the binary maze
        """

        # Uses list comprehension
        string: str
        string = "\n".join(
            "".join(" " if self.maze[row][column] else DEFAULT_MAZE_BLOCK for column in range(self.maze_width))
            for row in range(self.maze_height)
        )

        return string


    def _create_maze_from_file(self, kwargs) -> None|Exception:
        """
        create the maze from the data stored in a JSON file.
            kwargs (dict): Keyword arguments containing "path" as the key, which specifies the JSON file path.

        can throw a value error if required keywords are non-existent in the provided file
        """

        # File Path
        file_path = kwargs.get("path")

        # Opening JSON file and reading data into json data
        json_file: json.TextIOWrapper
        json_file = open()
        json_data: dict(any, any)
        json_data = json.load(json_file)
        json_file.close()

        # Checking Variables
        check_strings: list[str]
        check_strings = ["maze_width", "maze_height", "maze_binary", "goal_position", "player_spawn"]

        # Making sure all relevant keywords exist in the file
        for check_word in check_strings:
            if check_word not in json_data:
                return ValueError(f"binary_maze: keyword {check_word} not found in mazefile ({file_path})")
            else:
                pass
            continue

        # Setting Variables
        self.maze_width = json_data['maze_width']
        self.maze_height = json_data['maze_height']
        self.maze = json_data["maze_binary"]
        self.goal_position = json_data["goal_position"]
        self.player_spawn = json_data["player_spawn"]

    def _create_maze_from_dimensions(self, kwargs) -> None:
        """
        create a new maze with given dimensions. uses 'width' and 'height' keywords in kwargs
            kwargs (dict): Keyword arguments containing "width" and "height" as the keys, specifying the maze dimensions.

        can throw a value error if 'width'/'height' missing, although this is checked in constructor
        """
                
        # Getting the maze width
        self.maze_width: int
        try: self.maze_width = kwargs.get("width")
        except: raise ValueError("binary_maze: maze intantiation, keyword 'width' not found")

        # Getting the maze height
        self.maze_height: int
        try: self.maze_height = kwargs.get("height")
        except: raise ValueError("binary_maze: maze intantiation, keyword 'height' not found")

        # Creating a binary 2D array  of the map
        self.maze: list(int)
        self.maze = [[True for row in range(0, self.maze_width)] for column in range(0, self.maze_height)]

        # Check for random noise generation, if true make random
        if "random" in kwargs:
            if kwargs.get("random") is True:
                self.maze = [[bool(random.getrandbits(1)) for row in range(0, self.maze_width)] for column in range(0, self.maze_height)]
            else:
                pass
        

        # Player Start Point Dictionary, default is None
        self.player_spawn: dict[int, tuple[int, int]|None] = {}
        self.player_spawn[1], self.player_spawn[2] = None, None

        # Goal Row and Column
        self.goal_position: tuple(int, int)
        self.goal_position = (None, None)

    def write_maze_to_file(self, maze_path: str) -> None|Exception:
        """
        write the maze to a JSON file. maze_path (str) is the file path where the maze data will be saved. 
        can throw an exception if there is an error writing to file

        example usage:
            maze_instance = binary_maze(width=10, height=8)
            maze_instance.write_maze_to_file("maze_data.json")
        """

        # Gathering all relevant maze data
        json_data: dict(any, any) = dict()
        json_data['maze_width'] = self.maze_width
        json_data['maze_height'] = self.maze_height
        json_data["maze_binary"] = self.maze
        json_data["goal_position"] = self.goal_position
        json_data["player_spawn"] = self.player_spawn

        # Write to json file
        try:
            json_file = open(maze_path, 'w')
            json.dump(json_data, json_file, indent = 4, sort_keys = True)
            json_file.close()
        except Exception as e:
            return Exception(f"binary_maze: failed to write maze to file, exception: {e}")

    # Getters & Setters for maze cells
    def get_maze_cell(self, row: int, column: int) -> bool: return self.maze[row][column]
    def set_maze_cell(self, row: int, column: int, value: bool) -> None: self.maze[row][column] = value

    # Player Start Points Getters and Setters
    def get_player_spawn(self, player_id: int) -> tuple[int, int]|None: return self.player_spawn[player_id]
    def set_player_spawn(self, player_id: int, spawn_row: int, spawn_col: int) -> None: self.player_spawn[player_id] = (spawn_row, spawn_col)
    def set_player_spawn(self, player_id: int, spawn: tuple[int]) -> None: self.player_spawn[player_id] = spawn

    # Getters and setters for the goal position
    def set_goal_position(self, goal_row: int, goal_column: int) -> None: self.goal_position = (goal_row, goal_column)
    def set_goa_position(self, goal_position_tuple: tuple[int, int]): self.goal_position = goal_position_tuple
    def get_goal_position(self) -> tuple[int, int]|tuple[None, None]: return self.goal_position
    def get_goal_row(self) -> int|None: return self.goal_position.first
    def get_goal_column(self) -> int|None: return self.goal_position.second

    # Getters for width and height 
    def get_maze_width(self) -> int: return self.maze_width
    def get_maze_height(self) -> int: return self.maze_height
    def get_maze_dimensions(self) -> tuple[int, int]: return (self.maze_width, self.maze_height)

# Testing, just displaying a printed maze
if __name__ == "__main__":
    print("binary_maze: generating and displaying a random noise maze")
    test_maze = binary_maze(width = 50, height = 5, random = True)
    print(test_maze)