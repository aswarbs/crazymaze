
class binary_maze():

    def __init__(self, *args, **kwargs) -> None:
        
        # Getting the maze width
        self.maze_width: int
        try: self.maze_width, width = kwargs.get("width")
        except: raise ValueError("binary_maze: maze intantiation, keyword 'width' not found")

        # Getting the maze height
        self.maze_height: int
        try: self.maze_height, height = kwargs.get("height")
        except: raise ValueError("binary_maze: maze intantiation, keyword 'height' not found")

        # Creating a binary 2D array  of the map
        self.maze: list(int)
        self.maze: [[True for row in range(0, height)] for column in range(0, width)]

        # Player Start Point Dictionary, default is None
        self.player_spawn = dict(int, tuple(int, int)|None)
        self.player_spawn[1], self.player_spawn[2] = None

        # Goal Row and Column
        self.goal_position: tuple(int, int)
        self.goal_position = (None, None)

    # Getters & Setters for maze cells
    def get_maze_cell(self, row: int, column: int) -> bool: return self.maze[row][column]
    def set_maze_cell(self, row: int, column: int, value: bool) -> None: self.maze[row][column] = value

    # Player Start Points Getters and Setters
    def get_player_spawn(self, player_id: int) -> tuple(int, int)|None: return self.player_spawn[player_id]
    def set_player_spawn(self, player_id: int, spawn_row: int, spawn_col: int) -> None: self.player_spawn[player_id] = (spawn_row, spawn_col)
    def set_player_spawn(self, player_id: int, spawn: tuple(int, int)) -> None: self.player_spawn[player_id] = spawn

    # Getters and setters for the goal position
    def set_goal(self, goal_row: int, goal_column: int) -> None: self.goal_position = (goal_row, goal_column)
    def set_goal(self, goal_position_tuple: tuple(int, int)): self.goal_position = goal_position_tuple