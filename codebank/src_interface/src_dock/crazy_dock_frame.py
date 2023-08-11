from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider
from typing import Callable

class dock_tab(Button, theme_provider):

    def __init__(self, master: Tk|Frame, **kwargs) -> None:
        Button.__init__(self, master)
        theme_provider.__init__(self)

        self.configure(bg = self.dock_tab_background_unselected)
        self.configure(fg = self.dock_tab_text_unselected)
        self.configure(kwargs)

class crazydock(Frame, theme_provider):

    def __init__(self, master: Tk) -> None:
        Frame.__init__(self, master)
        theme_provider.__init__(self)
        self.configure(bg = self.dock_background)

        self.dock_buttons: list[Button]

    def create_dock_tab(self, name: str, func: Callable) -> None:
        
        temp_button: dock_tab
        temp_button

def start():
    master = Tk()
    f = crazydock(master)
    f.pack()
    master.mainloop()

if __name__ == "__main__":
    start()

