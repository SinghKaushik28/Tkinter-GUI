#advance paint app will do it 
import tkinter as tk
from tkinter import colorchooser
import math

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Drawing App")

        # Create Canvas
        self.canvas = tk.Canvas(root, width=500, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Default Drawing Settings
        self.current_shape = "line"
        self.pen_color = "black"
        self.brush_size = 2
        self.shapes = []

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # File menu (Clear canvas)
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Canvas", command=self.clear_canvas)

        # Edit menu (Undo/Redo)
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)

        # Settings menu (Brush Size & Color)
        settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label="Pick Color", command=self.change_color)
        settings_menu.add_command(label="Brush Size", command=self.change_brush_size)

        # Shape menu (Choose shape)
        shape_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Shapes", menu=shape_menu)
        shape_menu.add_command(label="Line", command=lambda: self.change_shape("line"))
        shape_menu.add_command(label="Rectangle", command=lambda: self.change_shape("rectangle"))
        shape_menu.add_command(label="Circle", command=lambda: self.change_shape("circle"))

        # History for undo/redo
        self.history = []
        self.redo_history = []

        # Bind mouse events to draw shapes
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_shape)
        self.canvas.bind("<ButtonRelease-1>", self.finalize_shape)

        # Responsive resizing of canvas
        self.root.bind("<Configure>", self.resize_canvas)

    def start_draw(self, event):
        """ Initialize the starting position for drawing """
        self.start_x = event.x
        self.start_y = event.y
        self.temp_shape = None

    def draw_shape(self, event):
        """ Draw the selected shape while dragging the mouse """
        x1, y1 = self.start_x, self.start_y
        x2, y2 = event.x, event.y
        shape_func = self.shape_functions[self.current_shape]

        # Delete the previous temp shape
        if self.temp_shape:
            self.canvas.delete(self.temp_shape)

        # Draw the current shape in real-time
        self.temp_shape = shape_func(self, x1, y1, x2, y2, temp=True)

    def finalize_shape(self, event):
        """ Finalize the shape on mouse release and save it to history """
        x1, y1 = self.start_x, self.start_y
        x2, y2 = event.x, event.y
        shape_func = self.shape_functions[self.current_shape]

        # Create and save the shape
        shape_id = shape_func(self, x1, y1, x2, y2)
        self.shapes.append(shape_id)
        self.history.append(("draw", shape_id))
        self.redo_history.clear()  # Clear redo history

    def change_color(self):
        """ Open a color picker to change the pen color """
        color = colorchooser.askcolor()[1]
        if color:
            self.pen_color = color

    def change_brush_size(self):
        """ Change the brush size """
        size = tk.simpledialog.askinteger("Brush Size", "Enter brush size (1-10):", minvalue=1, maxvalue=10)
        if size:
            self.brush_size = size

    def change_shape(self, shape):
        """ Change the current shape to draw """
        self.current_shape = shape

    def undo(self):
        """ Undo the last drawn shape """
        if self.history:
            action, shape_id = self.history.pop()
            self.canvas.delete(shape_id)
            self.redo_history.append(("undo", shape_id))

    def redo(self):
        """ Redo the last undone shape """
        if self.redo_history:
            action, shape_id = self.redo_history.pop()
            self.canvas.itemconfig(shape_id, state=tk.NORMAL)
            self.history.append(("draw", shape_id))

    def resize_canvas(self, event):
        """ Handle window resize and maintain canvas size """
        self.canvas.config(width=event.width, height=event.height)

    def clear_canvas(self):
        """ Clear the entire canvas """
        self.canvas.delete("all")
        self.shapes.clear()
        self.history.clear()
        self.redo_history.clear()

    def draw_line(self, x1, y1, x2, y2, temp=False):
        """ Draw a line on the canvas """
        line_id = self.canvas.create_line(x1, y1, x2, y2, width=self.brush_size, fill=self.pen_color, tags="temp" if temp else "")
        return line_id

    def draw_rectangle(self, x1, y1, x2, y2, temp=False):
        """ Draw a rectangle on the canvas """
        rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.pen_color, width=self.brush_size, tags="temp" if temp else "")
        return rect_id

    def draw_circle(self, x1, y1, x2, y2, temp=False):
        """ Draw a circle on the canvas """
        radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        circle_id = self.canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline=self.pen_color, width=self.brush_size, tags="temp" if temp else "")
        return circle_id

    # Shape functions for easy shape switching
    shape_functions = {
        "line": draw_line,
        "rectangle": draw_rectangle,
        "circle": draw_circle
    }

# Create the main window
root = tk.Tk()

# Initialize the drawing app
app = DrawingApp(root)

# Run the app
root.mainloop()
#interactive gui which take and store data
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# Creating the root window
root = tk.Tk()
root.title("Advanced Tkinter Program")
root.geometry("600x400")

# Styling the window
style = ttk.Style()
style.configure('TButton', font=('Arial', 12, 'bold'), foreground='white', background='#4CAF50', padding=10)
style.configure('TLabel', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))
style.configure('Treeview', font=('Arial', 10), rowheight=25)

# External Data (CSV) File Path
data_file = r"C:\Users\KAUSHIK\OneDrive\Documents\data.csv"

# Ensure the CSV file exists
if not os.path.exists(data_file):
    with open(data_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])  # Write headers (optional)

# Function to load data from the CSV file
def load_data():
    try:
        with open(data_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row if present
            for row in reader:
                treeview.insert("", "end", values=row)
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found!")

# Function to add data to the CSV file and the Treeview
def add_data():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    if name and age:
        try:
            int(age)  # Ensure age is a valid number
            with open(data_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, age])
            treeview.insert("", "end", values=(name, age))
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Age must be a number.")
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Function to delete selected row from Treeview and CSV file
def delete_data():
    selected_item = treeview.selection()
    if selected_item:
        # Get selected item's data
        selected_values = treeview.item(selected_item)["values"]
        treeview.delete(selected_item)
        # Remove the selected row from the CSV file
        rows = []
        with open(data_file, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row != selected_values:
                    writer.writerow(row)
    else:
        messagebox.showwarning("Selection Error", "No item selected for deletion.")

# Creating the Entry widgets for adding data
name_label = ttk.Label(root, text="Name:")
name_label.pack(pady=5)

name_entry = ttk.Entry(root)
name_entry.pack(pady=5)

age_label = ttk.Label(root, text="Age:")
age_label.pack(pady=5)

age_entry = ttk.Entry(root)
age_entry.pack(pady=5)

# Button to add data to Treeview and CSV
add_button = ttk.Button(root, text="Add Data", command=add_data)
add_button.pack(pady=10)

# Treeview for displaying data
treeview = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")
treeview.pack(pady=10, fill=tk.BOTH, expand=True)

# Scrollbar for the Treeview
scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
treeview.configure(yscrollcommand=scrollbar.set)

# Button to delete selected data from Treeview and CSV
delete_button = ttk.Button(root, text="Delete Data", command=delete_data)
delete_button.pack(pady=10)

# Load data from CSV file on program start
load_data()

# Run the Tkinter event loop
root.mainloop()
