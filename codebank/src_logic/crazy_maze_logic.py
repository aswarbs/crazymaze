
from scriptbank.crazy_generator_prim import *
from codebank.src_logic.crazy_player import player

class maze_logic():

    def __init__(self, controller) -> None:
        self.controller = controller


    def initialize_game(self, row:int, column:int) -> None:
        self.maze = generate_maze_prim(row, column)

        player1_spawn = self.maze.get_player_spawn(0)
        player2_spawn = self.maze.get_player_spawn(1)

        self.player1 = player(player1_spawn, 0)
        self.player2 = player(player2_spawn, 1)

        self.players = [self.player1, self.player2]

    

    
