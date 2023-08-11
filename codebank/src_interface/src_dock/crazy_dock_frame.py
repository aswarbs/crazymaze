from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider
from typing import Callable, Union


class dock_tab(Button, theme_provider):
    """
    Represents an individual dock tab in the CrazyDock container.

    Args:
        master (CrazyDock): The parent CrazyDock instance.
        text (str): The text to display on the dock tab.
        **kwargs: Additional keyword arguments for the Button widget.
    """

    def __init__(self, master: "crazydock", text: str, **kwargs) -> None:
        Button.__init__(self, master)
        theme_provider.__init__(self)

        self.button_selected: bool = False
        self.button_text: str = text
        self.parent: "crazydock" = master

        # Configure button appearance
        self.configure(bg=self.dock_tab_background_unselected)
        self.configure(fg=self.dock_tab_text_unselected)
        self.configure(command=self.switch_tab, text=text)
        self.configure(**kwargs)

    def switch_tab(self):
        """Callback when the dock tab is clicked."""
        self.master.button_pressed(self)

    def mark_selected(self):
        """Mark the dock tab as selected."""
        self.configure(bg=self.dock_tab_background_selected)
        self.configure(fg=self.dock_tab_text_selected)
        self.update()
    
    def mark_unselected(self):
        """Mark the dock tab as unselected."""
        self.configure(bg=self.dock_tab_background_unselected)
        self.configure(fg=self.dock_tab_text_unselected)
        self.update()

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

    def create_dock_tab(self, button_text: str, command: Callable) -> None:
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

        # Create dock tabs with corresponding frame show functions
        self.crazy_dock.create_dock_tab("Cum", lambda: self.show_frame("dimensions"))
        self.crazy_dock.create_dock_tab("Lau", lambda: self.show_frame("lau"))

    def show_frame(self, frame: str):
        """
        Display the specified frame associated with a dock tab.

        Args:
            frame (str): The name of the frame to display.
        """
        print(frame)

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