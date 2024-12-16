import tkinter as tk
from tkinter import ttk, colorchooser


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Canvas")
        self.pen_color = "black"
        self.pen_size = 3
        self.active_tool = "pencil"
        self.eraser_mode = False
        self.eraser_indicator = None
        
        # canvas Setup
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # event bindings
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        
        self.setup_toolbar()
        self.start_x = self.start_y = None 
        self.shape_id = None

    def setup_toolbar(self):
        toolbar = tk.Frame(self.root, bg="#37474f")
        toolbar.pack(fill=tk.X, pady=10)

        # styling for buttons
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12, "bold"), padding=10, relief="flat")
        style.configure("TButton", background="#1e88e5", foreground="white")
        style.map("TButton", background=[('active', '#1565c0')])
        
        color_btn = ttk.Button(toolbar, text="Color", command=self.select_color)
        color_btn.pack(side=tk.LEFT, padx=10)

        clear_btn = ttk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT, padx=10)

        eraser_btn = ttk.Button(toolbar, text="Eraser", command=self.toggle_eraser)
        eraser_btn.pack(side=tk.LEFT, padx=10)

        line_btn = ttk.Button(toolbar, text="Line", command=lambda: self.set_tool("line"))
        line_btn.pack(side=tk.LEFT, padx=10)

        rectangle_btn = ttk.Button(toolbar, text="Rectangle", command=lambda: self.set_tool("rectangle"))
        rectangle_btn.pack(side=tk.LEFT, padx=10)

        pencil_btn = ttk.Button(toolbar, text="Pencil", command=lambda: self.set_tool("pencil"))
        pencil_btn.pack(side=tk.LEFT, padx=10)

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.active_tool in ["line", "rectangle", "oval"]:
            self.shape_id = None

    def draw(self, event):
        x, y = event.x, event.y

        if self.eraser_mode:
            self.display_eraser(x, y)
            self.canvas.create_oval(
                x - self.pen_size // 2, y - self.pen_size // 2,
                x + self.pen_size // 2, y + self.pen_size // 2,
                fill=self.canvas["bg"], outline=self.canvas["bg"]
            )
        elif self.active_tool == "pencil":
            if self.start_x is not None and self.start_y is not None:
                self.canvas.create_line(self.start_x, self.start_y, x, y, fill=self.pen_color, width=self.pen_size, capstyle=tk.ROUND, smooth=True)
            self.start_x, self.start_y = x, y
        elif self.active_tool in ["line", "rectangle", "oval"]:
            if self.shape_id:
                self.canvas.delete(self.shape_id)
            if self.active_tool == "line":
                self.shape_id = self.canvas.create_line(self.start_x, self.start_y, x, y, fill=self.pen_color, width=self.pen_size)
            elif self.active_tool == "rectangle":
                self.shape_id = self.canvas.create_rectangle(self.start_x, self.start_y, x, y, outline=self.pen_color, width=self.pen_size)

    def stop_draw(self, event):
        self.start_x, self.start_y = None, None

    def select_color(self):
        color = colorchooser.askcolor(title="Color Selection")[1]
        if color:
            self.pen_color = color
            self.eraser_mode = False

    def toggle_eraser(self):
        self.pen_size = 15  
        self.pen_color = self.canvas["bg"]
        self.eraser_mode = True
        self.set_tool("pencil")

    def clear_canvas(self):
        self.canvas.delete("all")

    def set_tool(self, tool):
        self.active_tool = tool
        self.eraser_mode = False

    def display_eraser(self, x, y):
        if self.eraser_indicator:
            self.canvas.delete(self.eraser_indicator)
        self.eraser_indicator = self.canvas.create_oval(
            x - self.pen_size // 2, y - self.pen_size // 2,
            x + self.pen_size // 2, y + self.pen_size // 2,
            outline="red", width=2
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
