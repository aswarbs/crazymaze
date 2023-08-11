from tkinter import *
from codebank.src_interface.src_dock.crazy_dock import *

# Setup Windows
from codebank.src_interface.src_setup.crazy_setup_dimensions import *
from codebank.src_interface.src_setup.crazy_setup_algorithm import *
from codebank.src_interface.src_setup.crazy_setup_mode import *
from codebank.src_interface.src_setup.crazy_setup_players import *
from codebank.src_interface.src_setup.crazy_setup_colors import *


class setup_frame(Frame, theme_provider):
    """
    A frame to set up and manage frames associated with dock tabs.

    Args:
        master (Union[Tk, Frame]): The master Tk instance or parent frame.
        crazy_dock (CrazyDock): The CrazyDock instance associated with this setup.
    """

    def __init__(self, master: Union[Tk, Frame], crazy_dock: crazydock) -> None:
        Frame.__init__(self, master)
        theme_provider.__init__(self)

        self.master = master
        self.crazy_dock = crazy_dock

        # Create Frames
        dimensions_frame = setup_dimensions_frame(self)
        algorithm_frame = setup_algorithm_frame(self)
        mode_frame = setup_mode_frame(self)
        players_frame = setup_players_frame(self)
        colors_frame = setup_colors_frame(self)

        # Create dock tabs with corresponding frame show functions
        b = self.crazy_dock.create_dock_tab("Dimensions", lambda: self.show_frame(dimensions_frame))
        self.crazy_dock.create_dock_tab("Colors", lambda: self.show_frame(colors_frame))
        self.crazy_dock.create_dock_tab("Algorithm", lambda: self.show_frame(algorithm_frame))
        self.crazy_dock.create_dock_tab("Players", lambda: self.show_frame(players_frame))
        self.crazy_dock.create_dock_tab("Mode", lambda: self.show_frame(mode_frame))

        self.set_starting_frame(dimensions_frame, b)
    
    def set_starting_frame(self, frame: Frame, button: dock_tab) -> None:
        self.current_frame = frame
        self.crazy_dock.button_pressed(button)

    def show_frame(self, frame: Frame):
        """
        Display the specified frame associated with a dock tab.

        Args:
            frame (str): The name of the frame to display.
        """
        
        self.current_frame.forget()
        self.current_frame = frame
        self.current_frame.pack()
        self.update()

def start():
    """Start the application."""
    master = Tk()
    f = crazydock(master)
    f.pack()

    s = setup_frame(master, f)
    s.pack()
    master.mainloop()

if __name__ == "__main__":
    start()