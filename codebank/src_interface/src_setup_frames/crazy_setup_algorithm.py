from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider
from typing import Union

class setup_algorithm_frame(Frame, theme_provider):
    """
    A frame to set up and manage frames associated with dock tabs.

    Args:
        master (Union[Tk, Frame]): The master Tk instance or parent frame.
        crazy_dock (CrazyDock): The CrazyDock instance associated with this setup.
    """

    def __init__(self, master: Union[Tk, Frame]) -> None:
        theme_provider.__init__(self)
        Frame.__init__(self, master, bg = self.frame_colour)

        self.label = Label(self, text = "ALGORITHM Setup", font = ("Arial", 60, "bold"), bg= self.frame_colour).pack(fill="none", expand=True)
