import random
from typing import List, Tuple
from crazy_binary_maze import *

def get_neighbors(row: int, col: int, width: int, height: int) -> List[Tuple[int, int]]:
    
    # returns a list of valid neighboring cells for the given row and column within the maze boundaries.
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    valid_neighbors = [(r, c) for r, c in neighbors if 0 <= r < height and 0 <= c < width]
    return valid_neighbors

def carve_passage(maze: List[List[bool]], row1: int, col1: int, row2: int, col2: int) -> None:

    # carves a passage between two cells in the maze by setting the wall cell in between to be False (open).
    wall_row: int = (row1 + row2) // 2
    wall_col: int = (col1 + col2) // 2
    maze[wall_row][wall_col] = False

def generate_maze_dfs(width: int, height: int) -> binary_maze:

    # generates a random maze of the specified width and height using the Depth-First Search algorithm.
    maze: List[List[bool]] = [[True for _ in range(width)] for _ in range(height)]

    # stack to keep track of visited cells during maze generation.
    stack: List[Tuple[int, int]] = []   

    # set to store visited cells during maze generation.
    visited: set[Tuple[int, int]] = set()  

    start_row: int = random.randint(0, height - 1)
    start_col: int = random.randint(0, width - 1)

    # start the maze generation from a random cell.
    stack.append((start_row, start_col))  

    while stack:
        current_row, current_col = stack[-1]
        visited.add((current_row, current_col))

        neighbors: List[Tuple[int, int]] = get_neighbors(current_row, current_col, width, height)
        unvisited_neighbors: List[Tuple[int, int]] = [(r, c) for r, c in neighbors if (r, c) not in visited]

        if unvisited_neighbors:
            next_row, next_col = random.choice(unvisited_neighbors)
            stack.append((next_row, next_col))

            # carve a passage to the next cell.
            carve_passage(maze, current_row, current_col, next_row, next_col)  
        else:
            # backtrack if there are no unvisited neighbors from the current cell.
            stack.pop()  

    # Find positions for player spawns and goal
    top_spawn_row, top_spawn_col = random.choice([(0, random.randint(0, width - 1))])
    bottom_spawn_row, bottom_spawn_col = random.choice([(height - 1, random.randint(0, width - 1))])
    goal_row, goal_col = height // 2, width // 2

    # create a binary maze instance
    binary_maze_instance = binary_maze(width = width, height = height)
    binary_maze_instance.set_maze_internal([[False if cell else True for cell in row] for row in maze])
    binary_maze_instance.set_player_spawn(0, (top_spawn_row, top_spawn_col))
    binary_maze_instance.set_player_spawn(1, (bottom_spawn_row, bottom_spawn_col))
    binary_maze_instance.set_goal_position((goal_row, goal_col))
    return binary_maze_instance

if __name__ == "__main__":
    test_maze = generate_maze_dfs(20, 5)
    print(test_maze)
