from tkinter import *
from codebank.src_interface.crazy_theme_provider import theme_provider
from codebank.src_interface.src_dock.crazy_dock_tab import dock_tab
from typing import Callable, Union
import math

CANVAS_WIDTH = 180
CANVAS_HEIGHT = 80

PLAY_CANVAS_HEIGHT = 80
PLAY_CANVAS_WIDTH = 80

def draw_play_button(canvas, green):
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    
    center_x = canvas_width / 2
    center_y = canvas_height / 2
    radius = min(center_x, center_y) * 0.4
    
    # Draw the circle
    circle = canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill=green, outline=green)
    
    # Calculate triangle points
    triangle_size = radius * 0.8  # Slightly larger triangle
    half_triangle_size = triangle_size / 2
    triangle_points = [
        center_x - half_triangle_size, center_y - half_triangle_size,
        center_x + half_triangle_size, center_y,
        center_x - half_triangle_size, center_y + half_triangle_size
    ]
    
    # Draw the triangle
    triangle = canvas.create_polygon(triangle_points, fill="white", outline="white")
    
    return circle, triangle

class crazydock(Frame, theme_provider):
    """
    A container to manage dock tabs and their associated frames.

    Args:
        master (Tk): The master Tk instance.
    """

    def __init__(self, master: Tk) -> None:
        Frame.__init__(self, master, bg = "green")
        theme_provider.__init__(self)

        self.configure(bg=self.dock_background)

        self.dock_buttons: list[dock_tab] = []
        self.dock_commands: dict[dock_tab, Callable] = {}

        self.crazy_maze_label = Canvas(self, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = self.dock_background, border=0, borderwidth = 0, highlightthickness=0, relief='ridge')
        self.crazy_maze_label.create_text(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, text = "crazymaze", fill = "#FBFBFB", font = ("C059", 24, "bold"))

        self.crazy_maze_play = Canvas(self, width = PLAY_CANVAS_WIDTH, height = PLAY_CANVAS_HEIGHT, bg = self.dock_background, border=0, borderwidth = 0, highlightthickness=0, relief='ridge')
        draw_play_button(self.crazy_maze_play, self.play_button)

        self.crazy_maze_play.pack(side = RIGHT)
        self.crazy_maze_label.pack(side=RIGHT, padx = (20, 0))

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
        temp_button: dock_tab = dock_tab(self, button_text, font = ("C059", 18, "bold"))
        self.dock_buttons.append(temp_button)
        self.dock_commands[temp_button] = command

        temp_button.pack(side=LEFT, anchor=S, ipadx = 4, ipady = 4,)

        return temp_button