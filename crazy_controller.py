# Import the setup screen
from crazy_window import window
from crazy_maze_logic import maze_logic

class controller():
    def __init__(self) -> None:

        

        self.game_logic = maze_logic(self)

        self.main_window = window(self)

        self.main_window.master.mainloop()

    def on_key_released(self,event):
        if event.keysym == 'w':
            valid = self.main_window.current_frame.update_position(0, 0, -1)
            if(valid):
                self.game_logic.player1.move("up")
        elif event.keysym == 's':
            valid = self.main_window.current_frame.update_position(0, 0, 1)
            if(valid):
                self.game_logic.player1.move("down")
        elif event.keysym == 'a':
            valid = self.main_window.current_frame.update_position(0, -1, 0)
            if(valid):
                self.game_logic.player1.move("left")
        elif event.keysym == 'd':
            valid = self.main_window.current_frame.update_position(0, 1, 0)
            if(valid):
                self.game_logic.player1.move("right")

        elif event.keysym == 'Up':
            valid = self.main_window.current_frame.update_position(1, 0, -1)
            if(valid):
                self.game_logic.player2.move("up")
        elif event.keysym == 'Down':
            valid = self.main_window.current_frame.update_position(1, 0, 1)
            if(valid):
                self.game_logic.player2.move("down")
        elif event.keysym == 'Left':
            valid = self.main_window.current_frame.update_position(1, -1, 0)
            if(valid):
                self.game_logic.player2.move("left")
        elif event.keysym == 'Right':
            valid = self.main_window.current_frame.update_position(1, 1, 0)
            if(valid):
                self.game_logic.player2.move("right")



