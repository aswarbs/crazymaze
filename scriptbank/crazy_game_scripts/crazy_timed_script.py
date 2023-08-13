from scriptbank.crazy_script_base import script_base
from tkinter import *

class timed_script(script_base):


    def get_setup_frame(self, frame) -> Frame:

        self.frame = frame

        Label(self.frame, text="TIMED SCRIPT").pack()

        return self.frame
    
    def on_time_slider_change(self, value:str):
        self.time = int(value)
    


    
