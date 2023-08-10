from codebank.src_logic.crazy_binary_maze import binary_maze

def request_to_binary_maze(maze_generation_callback: dict[str, any]) -> binary_maze:
    """
    Converts the callback from crazy_script_runner to a binary maze instance. Checks existence of keywords
    in passed crazy_script_runner callback object, should be in a JSON-style formatting. Required keywords are:
    (maze_data, player_one_start, player_two_start, goal)
    """

    for word in ["maze_data", "player_one_start", "player_two_start", "goal"]:
        if word not in maze_generation_callback.keys():
            raise Exception(f"string_to_binary_maze \t:\t{word} not found in callback request")

    maze_data: list[list[bool]]
    maze_data = maze_generation_callback["maze_data"]

    player_one_start = tuple[int]
    player_one_start = maze_generation_callback["player_one_start"]

    player_two_start = tuple[int]
    player_two_start = maze_generation_callback["player_two_start"]

    goal_position = tuple[int]
    goal_position = maze_generation_callback["goal"]

    bin_maze_instance = binary_maze(width = len(maze_data[0]), height = len(maze_data))

    for row_index, row_values in enumerate(maze_data):
        for column_index, maze_point_value in enumerate(row_values):
            bin_maze_instance.set_maze_cell(row_index, column_index, maze_point_value)
    
    bin_maze_instance.set_goal_position(goal_position)
    bin_maze_instance.set_player_spawn(0, player_one_start)
    bin_maze_instance.set_player_spawn(1, player_two_start)

    return bin_maze_instance