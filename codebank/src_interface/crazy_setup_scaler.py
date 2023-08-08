from tkinter import *

class scaler_widget (Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.master.title("Resizable Canvas")

        self.row_counter = StringVar(value="3")
        self.column_counter = StringVar(value="3")

        self.setup_widgets()

    def setup_widgets(self):

        label = Label(self, text = "Select Maze Size")
        label.pack()

        bframe = Frame(self)
        counter_frame1 = Frame(bframe)
        counter_frame1.pack(side="left")

        # Buttons and Entry for the row counter
        row_label = Label(counter_frame1, text="Rows:")
        row_label.pack(side="left")
        row_decrease_button = Button(counter_frame1, text="<", command=self.decrease_rows)
        row_decrease_button.pack(side="left")
        row_entry = Entry(counter_frame1, textvariable=self.row_counter, width=5)
        row_entry.pack(side="left")
        row_increase_button = Button(counter_frame1, text=">", command=self.increase_rows)
        row_increase_button.pack(side="left")

        # Canvas to display the grid
        self.canvas = Canvas(bframe, width=300, height=300, bg="black")
        self.canvas.pack(side="left")

        counter_frame = Frame(bframe)
        counter_frame.pack(side="right")

        # Buttons and Entry for the column counter
        column_label = Label(counter_frame, text="Columns:")
        column_label.pack(side="left")
        column_decrease_button = Button(counter_frame, text="<", command=self.decrease_columns)
        column_decrease_button.pack(side="left")
        column_entry = Entry(counter_frame, textvariable=self.column_counter, width=5)
        column_entry.pack(side="left")
        column_increase_button = Button(counter_frame, text=">", command=self.increase_columns)
        column_increase_button.pack(side="left")
        bframe.pack()

        # Cell size in pixels
        self.cell_size = 15

        # Show maze dimensions
        self.dimension_label = Label(self, text = str(self.column_counter.get()) + "x" + str(self.row_counter.get()))
        self.dimension_label.pack(side="bottom")

        # Call the update_canvas function initially to set up the grid
        self.update_canvas()

    def get_rows_cols(self) -> tuple[int, int]:
        return (int(self.column_counter.get()), int(self.row_counter.get()))

    def update_canvas(self):
        rows = int(self.row_counter.get())
        columns = int(self.column_counter.get())

        self.canvas.delete("all")

        canvas_width = (columns * self.cell_size) + 40
        canvas_height = (rows * self.cell_size) + 40
        self.canvas.config(width=canvas_width, height=canvas_height)

        for row in range(rows):
            for col in range(columns):
                x1 = (col * self.cell_size) + 20
                y1 = (row * self.cell_size) + 20
                x2 = (x1 + self.cell_size)
                y2 = (y1 + self.cell_size) 
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="white")
        
        self.dimension_label.config(text = str(self.column_counter.get()) + "x" + str(self.row_counter.get()))
        self.dimension_label.update()

    def increase_rows(self):
        self.row_counter.set(str(int(self.row_counter.get()) + 1))
        self.update_canvas()

    def decrease_rows(self):
        self.row_counter.set(str(max(1, int(self.row_counter.get()) - 1)))
        self.update_canvas()

    def increase_columns(self):
        self.column_counter.set(str(int(self.column_counter.get()) + 1))
        self.update_canvas()

    def decrease_columns(self):
        self.column_counter.set(str(max(1, int(self.column_counter.get()) - 1)))
        self.update_canvas()
    
    def get_columns(self) -> int: return self.column_counter.get()
    def get_rows(self) -> int: return self.row_counter.get()


if __name__ == "__main__":
    root = Tk()
    canvas_frame = scaler_widget(root)
    canvas_frame.pack()
    root.mainloop()
