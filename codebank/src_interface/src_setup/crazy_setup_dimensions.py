from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider
from typing import Union

class setup_dimensions_frame(Frame, theme_provider):
    """
    A frame to set up and manage frames associated with dock tabs.

    Args:
        master (Union[Tk, Frame]): The master Tk instance or parent frame.
        crazy_dock (CrazyDock): The CrazyDock instance associated with this setup.
    """

    def __init__(self, master: Union[Tk, Frame]) -> None:
        Frame.__init__(self, master)
        theme_provider.__init__(self)

        self.label = Label(self, text = "DIMENSIONS", font = ("Arial", 60, "bold")).pack()
