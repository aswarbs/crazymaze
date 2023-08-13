from scriptbank.crazy_script_base import script_base
from tkinter import *

class visibility_script(script_base):


    def get_setup_frame(self, frame) -> Frame:

        self.frame = frame

        Label(self.frame, text="VISIBILITY SCRIPT").pack()
        return self.frame

    
