from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider
from typing import Callable

class crazydock(Frame, theme_provider):

    def __init__(self, master: Tk) -> None:
        Frame.__init__(self, master)
        theme_provider.__init__(self)
        self.configure(bg = self.dock_background)

    def create_dock_button(self, name: str, func: Callable) -> None:
        pass

def start():
    master = Tk()
    f = crazydock(master)
    f.pack()
    master.mainloop()

if __name__ == "__main__":
    start()

