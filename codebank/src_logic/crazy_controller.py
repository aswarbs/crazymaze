# Import the setup screen
from codebank.src_interface.crazy_window import window
from codebank.src_logic.crazy_maze_logic import maze_logic

class controller():
    def __init__(self) -> None:

        # Create a dictionary mapping a possible move key to a tuple,
        # containing the corresponsing direction, playerid, change in x and change in y.
        self.PLAYER_MOVES: dict[str: (str, int, int, int)]
        self.PLAYER_MOVES = {
            'w': ("up", 0, 0, -1),
            's': ("down", 0, 0, 1),
            'a': ("left", 0, -1, 0),
            'd': ("right", 0, 1, 0),
            'Up': ("up", 1, 0, -1),
            'Down': ("down", 1, 0, 1),
            'Left': ("left", 1, -1, 0),
            'Right': ("right", 1, 1, 0)
        }
        
        # Create an instance of the game logic and window. Start the GUI.
        self.game_logic = maze_logic(self)
        self.main_window = window(self)
        self.main_window.master.mainloop()

    def on_key_released(self, event):
        """
        Handle key presses and corresponding player movement and game logic.
        """

        # If the key pressed is in WASD or arrows,
        if event.keysym in self.PLAYER_MOVES:
            # Retrieve the corresponding player information from the PLAYER_MOVES dictionary.
            direction, player_num, dx, dy = self.PLAYER_MOVES[event.keysym]
            # Retrieve whether the corresponding move is valid.
            valid = self.main_window.current_frame.update_position(player_num, dx, dy)
            if valid:
                # Move the player to the new position.
                player = self.game_logic.player1 if player_num == 0 else self.game_logic.player2
                player.move(direction)







