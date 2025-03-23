import tkinter as tk
import math

root = tk.Tk()
root.title("Scaling, Rotation & Dragging")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Initial rectangle (centered)
rect_coords = [200, 150, 300, 150, 300, 200, 200, 200]  # x1, y1, x2, y2
rect = canvas.create_polygon(rect_coords, fill="blue", outline="black", tags="rect")

# Variables for dragging
drag_data = {"x": 0, "y": 0}

def start_drag(event):
    """Store the initial position when dragging starts"""
    drag_data["x"] = event.x
    drag_data["y"] = event.y

def on_drag(event):
    """Move the rectangle while dragging"""
    dx = event.x - drag_data["x"]
    dy = event.y - drag_data["y"]
    canvas.move("rect", dx, dy)
    drag_data["x"] = event.x
    drag_data["y"] = event.y

def scale_rectangle(event):
    """Increase size with W, Decrease size with S"""
    if event.keysym == "w":
        scale_factor = 1.1 # Increase
    elif event.keysym == "s":
        scale_factor = 0.9  # Decrease
    else:
        return 
    
    coords = canvas.coords(rect)
    cx, cy = sum(coords[::2]) / 4, sum(coords[1::2]) / 4  # Find center

    new_coords = []
    for i in range(0, len(coords), 2):
        x, y = coords[i], coords[i+1]
        new_x = cx + (x - cx) * scale_factor
        new_y = cy + (y - cy) * scale_factor
        new_coords.extend([new_x, new_y])

    canvas.coords(rect, *new_coords)

def move_left():
    canvas.move(rect, -10, 0)

def move_right():
    canvas.move(rect, 10, 0)

def move_up():
    canvas.move(rect, 0, -10)

def move_down():
    canvas.move(rect, 0, 10)

def rotate_rectangle(event):
    """Rotate left with A, Rotate right with D"""
    if event.keysym == "a":
        angle = -10  # Rotate Left
    elif event.keysym == "d":
        angle = 10  # Rotate Right
    else:
        return  # Exit if any other key
    angle = math.radians(angle)  # Convert to radians

    coords = canvas.coords(rect)
    cx, cy = sum(coords[::2]) / 4, sum(coords[1::2]) / 4  # Find center

    new_coords = []
    for i in range(0, len(coords), 2):
        x, y = coords[i], coords[i+1]
        new_x = cx + (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle)
        new_y = cy + (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle)
        new_coords.extend([new_x, new_y])

    canvas.coords(rect, *new_coords)

# Bind events
canvas.tag_bind("rect", "<ButtonPress-1>", start_drag)
canvas.tag_bind("rect", "<B1-Motion>", on_drag)
root.bind("<w>", scale_rectangle)
root.bind("<s>", scale_rectangle)
root.bind("<a>", rotate_rectangle)
root.bind("<d>", rotate_rectangle)

root.bind("<Left>",lambda event:move_left())
root.bind("<Right>",lambda event:move_right())
root.bind("<Up>",lambda event:move_up())
root.bind("<Down>",lambda event:move_down())

root.mainloop()
