from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider


class dock_tab(Button, theme_provider):
    """
    Represents an individual dock tab in the CrazyDock container.

    Args:
        master (CrazyDock): The parent CrazyDock instance.
        text (str): The text to display on the dock tab.
        **kwargs: Additional keyword arguments for the Button widget.
    """

    def __init__(self, master, text: str, **kwargs) -> None:
        Button.__init__(self, master)
        theme_provider.__init__(self)

        self.button_selected: bool = False
        self.button_text: str = text
        self.parent = master

        # Configure button appearance
        self.configure(bg=self.dock_tab_background_unselected)
        self.configure(fg=self.dock_tab_text_unselected)
        self.configure(command=self.switch_tab, text=text)
        self.configure(highlightthickness=0, relief='ridge', bd = 0)
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