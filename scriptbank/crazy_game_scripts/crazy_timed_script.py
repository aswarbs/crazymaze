from scriptbank.crazy_script_base import script_base
from tkinter import *

class timed_script(script_base):


    def get_setup_frame(self, frame) -> Frame:

        self.frame = frame


        # Create a slider to represent the chosen number of rows.
        time_slider: Scale
        self.time: int = 8
        time_slider = Scale(self.frame, from_ = 8, to=100, orient=HORIZONTAL, command=self.on_time_slider_change)
        time_slider.pack(side=LEFT)


        return self.frame
    
    def on_time_slider_change(self, value:str):
        self.time = int(value)
    


    
