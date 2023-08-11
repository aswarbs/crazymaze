from tkinter import *
from codebank.src_interface.src_dock.crazy_dock import *

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
        dimension_frame = Frame(self)
        dlabel = Label(dimension_frame, text = "dimensions").pack()

        colors_frame = Frame(self)
        clabel = Label(colors_frame, text = "Colors").pack()

        # Create dock tabs with corresponding frame show functions
        self.crazy_dock.create_dock_tab("Dimensions", lambda: self.show_frame(dimension_frame))
        self.crazy_dock.create_dock_tab("Colors", lambda: self.show_frame(colors_frame))

        self.current_frame = dimension_frame
        self.current_frame.pack()
        

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