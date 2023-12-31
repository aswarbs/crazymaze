from tkinter import *
import codebank.src_game_script_runner.crazy_game_script_loader as scanner

class script_display(Frame):

    def __init__(self, master: Tk, parent_window) -> None:
        """
        load the scripts from scriptbank
        call create_scripts_window to create the gui
        """

        self.master: Tk
        self.master = master
        self.parent_window = parent_window

        super().__init__(self.master)

        self.scripts = scanner.scan_scripts()

        self.script_name_to_frame = {}

        


        




        
        self.create_scripts_window()

        



    def initialize_chosen_frame(self):
        frame = Frame(self.content_frame, background="yellow")
        return frame

    def create_scripts_window(self) -> None:
        """
        create the main frame which will hold all subframes
        call create_scripts_subframe and display the list of scripts as a subframe
        create a frame to store the current script parameters

        - play button
        - back to setup button
        - 
        """

        

        self.create_content_frame()
        self.content_frame.pack(side=TOP, expand=TRUE)


        

        for script in self.scripts:
            initial_frame = self.initialize_chosen_frame()
            class_instance = scanner.load_script(script)
            self.script_name_to_frame[script] = class_instance.get_setup_frame(initial_frame)


       

        




        options_frame = self.create_options_frame()
        options_frame.pack(side=BOTTOM, fill=X, expand=TRUE)

        self.pack(fill=BOTH, expand=TRUE)

    def load_initial_script_subframe(self) -> Frame:
            initial_frame = self.initialize_chosen_frame()
            Label(initial_frame, text="initial").pack()
            return initial_frame

    def load_chosen_script_subframe(self, **kwargs) -> Frame:
        """
        load the subframe created from the chosen script
        """

        if "script" not in kwargs:
            frame = self.load_initial_script_subframe()
            

        else:
            script_name = kwargs["script"]
            frame = self.script_name_to_frame[script_name]
        
        return frame

    def pack_chosen_script_subframe(self,parent_frame:Frame, **kwargs):

        self.chosen_frame.pack_forget()

        self.chosen_frame = self.load_chosen_script_subframe(**kwargs)

        self.chosen_frame.pack(in_ = parent_frame, fill=BOTH, expand=TRUE)

    def create_content_frame(self) -> Frame:

        self.content_frame = Frame(self)

        self.chosen_frame = self.initialize_chosen_frame()

        script_frame = self.create_scripts_frame(self.content_frame, self.scripts)
        script_frame.pack(side=LEFT, fill=Y, expand=TRUE)
        #
        

        self.pack_chosen_script_subframe(self.content_frame)

    def create_options_frame(self):

        frame = Frame(self)

        play_button = Button(frame, text="play", command=self.start_game)
        play_button.pack(side=BOTTOM)

        return frame

    def start_game(self) -> None:
        self.parent_window.change_frame("crazy_maze_game")

    def create_scripts_frame(self, parent_frame, scripts:list[str]) -> Frame:
        """
        create the subframe that stores the retrieved list of scripts as buttons
        """

        subframe = Frame(parent_frame)

        scrollbar = Scrollbar(subframe, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)

        self.script_canvas = Canvas(subframe, yscrollcommand=scrollbar.set)
        self.script_canvas.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        script_frame = Frame(self.script_canvas)

        self.script_canvas.create_window((0,0), window=script_frame, anchor=NW)

        scrollbar.config(command=self.script_canvas.yview)

        self.script_canvas.bind("<Configure>", self.on_canvas_configure)
        
        
        for name in scripts:
            current_button = Button(script_frame, text=name, command=lambda n=name: self.pack_chosen_script_subframe(parent_frame, script=n))
            current_button.pack()

            

        return subframe

    def on_canvas_configure(self, event):
        self.script_canvas.configure(scrollregion=self.script_canvas.bbox("all"))



