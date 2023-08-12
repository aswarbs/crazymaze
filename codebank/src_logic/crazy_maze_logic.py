from codebank.src_logic.crazy_player import player
import codebank.src_scriptrunner.crazy_script_runner as runner
import codebank.src_scriptrunner.crazy_maze_converter as converter
import time

class maze_logic():

    def __init__(self, controller) -> None:
        self.controller = controller

    def set_win_condition():
        pass


    def initialize_game(self, row:int, column:int, game_mode_dict:dict, chosen_maze_generation_script:str) -> None:
        runner_queue = runner.run_script(chosen_maze_generation_script, row, column)
        while(runner_queue.qsize() == 0):
            #print(runner_queue.qsize())
            time.sleep(0.05)
        self.maze = converter.request_to_binary_maze(runner_queue.get())

        player1_spawn = self.maze.get_player_spawn(0)
        player2_spawn = self.maze.get_player_spawn(1)

        self.player1 = player(player1_spawn, 0)
        self.player2 = player(player2_spawn, 1)

        self.players = [self.player1, self.player2]

    

    
