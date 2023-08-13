from scriptbank.crazy_script_base import script_base
from tkinter import *

class timed_script(script_base):

    def __init__(self):
        pass
    
    def get_setup_frame(self, frame: Frame) -> Frame:
        self.frame = frame

        # Create a slider to represent the chosen number of rows.
        time_slider = Scale(self.frame, from_=8, to=100, orient=HORIZONTAL, command=self.on_time_slider_change)
        time_slider.pack(side=LEFT)

        return self.frame
    
    def on_time_slider_change(self, value):
        self.time = int(value)


    
