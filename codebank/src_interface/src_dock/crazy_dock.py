from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider
from codebank.src_interface.src_dock.crazy_dock_tab import dock_tab
from typing import Callable, Union


class crazydock(Frame, theme_provider):
    """
    A container to manage dock tabs and their associated frames.

    Args:
        master (Tk): The master Tk instance.
    """

    def __init__(self, master: Tk) -> None:
        Frame.__init__(self, master)
        theme_provider.__init__(self)

        self.configure(bg=self.dock_background)

        self.dock_buttons: list[dock_tab] = []
        self.dock_commands: dict[dock_tab, Callable] = {}

    def button_pressed(self, button_pressed: dock_tab) -> None:
        """
        Handle the button press event of a dock tab.

        Args:
            button_pressed (DockTab): The dock tab that was pressed.
        """
        for tab in self.dock_buttons:
            if tab is not button_pressed:
                tab.mark_unselected()
            else:
                tab.mark_selected()
        
        self.dock_commands[button_pressed]()

    def create_dock_tab(self, button_text: str, command: Callable) -> dock_tab:
        """
        Create and add a new dock tab.

        Args:
            button_text (str): The text to display on the dock tab.
            command (Callable): The callback function associated with the tab.
        """
        temp_button: dock_tab = dock_tab(self, button_text)
        self.dock_buttons.append(temp_button)
        self.dock_commands[temp_button] = command
        temp_button.pack(padx=10, pady=10)
        return temp_button