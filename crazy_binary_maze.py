import json

class binary_maze():

    def __init__(self, *args, **kwargs) -> None|Exception:
        
        if "path" in kwargs:
            self.create_maze_from_file(kwargs)
        
        elif "width" in kwargs and "height" in kwargs:
            self.create_maze_from_dimensions(kwargs)

        else:
            return ValueError("binary_maze: failed to initialize, no relevant keyword argument")

    def create_maze_from_file(self, kwargs) -> None|Exception:

        # File Path
        file_path = kwargs.get("path")

        # Opening JSON file and reading data
        json_file: json.TextIOWrapper
        json_file = open()

        json_data: dict(any, any)
        json_data = json.load(json_file)

        json_file.close()

        # Checking Variables
        check_strings: list[str]
        check_strings = [
            "maze_width",
            "maze_height",
            "maze_binary",
            "goal_position",
            "player_spawn"
        ]

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

    def create_maze_from_dimensions(self, kwargs) -> None:

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
        self.maze = [[True for row in range(0, self.maze_height)] for column in range(0, self.maze_width)]

        # Player Start Point Dictionary, default is None
        self.player_spawn: dict[int, tuple[int, int]|None] = {}
        self.player_spawn[1], self.player_spawn[2] = None, None

        # Goal Row and Column
        self.goal_position: tuple(int, int)
        self.goal_position = (None, None)

    def write_maze_to_file(self, maze_path: str) -> None|Exception:

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

x = binary_maze(width = 10, height = 10)
x.write_maze_to_file("test_maze.json")