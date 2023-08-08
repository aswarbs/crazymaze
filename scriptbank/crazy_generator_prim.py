
## Imports
import random
import time
import itertools
import math
from codebank.src_logic.crazy_binary_maze import *

SYMBOL_WALL = "w"
SYMBOL_CELL = "c"
SYMBOL_UNVISITED = "u"

# Init variables
wall = SYMBOL_WALL
cell = SYMBOL_CELL
unvisited = SYMBOL_UNVISITED


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_furthest_points(coordinates):
    max_distance = 0
    furthest_points = None

    # Calculate pairwise distances and find the three points with maximum distances
    distances: dict[float, tuple(tuple(int, int), tuple(int, int), tuple(int, int))] = {}
    for p1, p2, p3 in itertools.combinations(coordinates, 3):
        d1 = euclidean_distance(p1, p2)
        d2 = euclidean_distance(p2, p3)
        distances[d1+d2] = (p1, p2, p3)

    max_distance = max(distances.keys())
    return distances[max_distance]

def surrounding_cells(maze, rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells +=1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1
    
    return s_cells

def get_starting_point(width, height):
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)
    if (starting_height == 0): starting_height += 1
    if (starting_height == height - 1): starting_height -= 1
    if (starting_width == 0): starting_width += 1
    if (starting_width == width - 1): starting_width -= 1
    return starting_width, starting_height

def check_left(walls, maze, rand_wall, width, height) -> bool:
    # Check if it is a left wall
    cont = False
    if (rand_wall[1] != 0):
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            # Find the number of surrounding cells
            s_cells = surrounding_cells(maze, rand_wall)

            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])


                # Bottom cell
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):	
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
            

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            cont = True
    
    return walls, maze, cont

def check_upper(walls, maze, rand_wall, width, height):
    # Check if it is an upper wall
    cont = False
    if (rand_wall[0] != 0):
        if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

            s_cells = surrounding_cells(maze, rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])

                # Rightmost cell
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall) 

            cont = True

    return walls, maze, cont

def check_lower(walls, maze, rand_wall, width, height):
    # Check the bottom wall
    cont = False
    if (rand_wall[0] != height-1):
        if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

            s_cells = surrounding_cells(maze, rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)
            cont = True
    return walls, maze, cont

def check_right(walls, maze, rand_wall, width, height):
    # Check the right wall
    cont = False
    if (rand_wall[1] != width-1):
        if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

            s_cells = surrounding_cells(maze,rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[0] != 0):	
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)
            cont = True
    return walls, maze, cont

def mark_unvisited(maze, width, height):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = 'w'

    # Set entrance and exit
    for i in range(0, width):
        if (maze[1][i] == 'c'):
            maze[0][i] = 'c'
            break

    for i in range(width-1, 0, -1):
        if (maze[height-2][i] == 'c'):
            maze[height-1][i] = 'c'
            break

    return maze

def generate_maze_prim(rows, columns) -> binary_maze:

    width = columns
    height = rows

    maze: list[list[str]] = []

    # Denote all cells as unvisited
    maze = [[unvisited for _ in range(width)] for _ in range(height)]

    # Randomize starting point and set it a cell
    starting_width: int
    starting_height: int
    starting_width, starting_height = get_starting_point(width, height)

    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # Denote walls in maze
    maze[starting_height-1][starting_width] = 'w'
    maze[starting_height][starting_width - 1] = 'w'
    maze[starting_height][starting_width + 1] = 'w'
    maze[starting_height + 1][starting_width] = 'w'

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        walls, maze, cont = check_left(walls, maze, rand_wall, width, height)
        if cont: continue
        walls, maze, cont = check_upper(walls, maze, rand_wall, width, height)
        if cont: continue

        walls, maze, cont = check_lower(walls, maze, rand_wall, width, height)
        if cont: continue

        walls, maze, cont = check_right(walls, maze, rand_wall, width, height)
        if cont: continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    maze = mark_unvisited(maze, width, height)

    potential_spawns: list[tuple[int, int]] = []

    binary_maze_instance = binary_maze(width = width, height = height)
    for row in range(0, height):
        for column in range(0, width):
            current = maze[row][column]
            if(current == 'c'):
                binary_maze_instance.set_maze_cell(row, column, True)
                potential_spawns.append((row, column))
            else:
                binary_maze_instance.set_maze_cell(row, column, False)
    p1, goal, p2 = find_furthest_points(potential_spawns)
    binary_maze_instance.set_goal_position(goal)
    binary_maze_instance.set_player_spawn(0, p1)
    binary_maze_instance.set_player_spawn(1, p2)
    
    return binary_maze_instance

if __name__ == "__main__":
    bin_maze_test = generate_maze_prim(100, 100)
    print(bin_maze_test)
                   
    