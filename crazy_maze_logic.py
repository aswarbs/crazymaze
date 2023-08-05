
from crazy_generator_prim import *
from crazy_player import player

class maze_logic():

    def __init__(self) -> None:
        pass


    def initialize_game(self, row:int, column:int) -> None:
        self.maze = generate_maze_prim(row, column)

        player1_spawn = self.maze.get_player_spawn(0)
        player2_spawn = self.maze.get_player_spawn(1)

        self.player1 = player(player1_spawn, 0)
        self.player2 = player(player2_spawn, 1)

        self.players = [self.player1, self.player2]

    
    def on_key_released(self,event):
        if event.keysym == 'w':
            self.player1.move("up")
        elif event.keysym == 's':
            self.player1.move("down")
        elif event.keysym == 'a':
            self.player1.move("left")
        elif event.keysym == 'd':
            self.player1.move("right")

        elif event.keysym == 'Up':
            self.player2.move("up")
        elif event.keysym == 'Down':
            self.player2.move("down")
        elif event.keysym == 'Left':
            self.player2.move("left")
        elif event.keysym == 'Right':
            self.player2.move("right")

    
