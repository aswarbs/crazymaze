from scriptbank.crazy_script_base import script_base
from tkinter import *

class timed_script(script_base):


    def get_setup_frame(self) -> Frame:

        frame = Frame()
        Label(frame, text="frame 1").pack()
        return frame

    
