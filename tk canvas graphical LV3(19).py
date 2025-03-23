import tkinter as tk

root = tk.Tk()
root.title("Smooth Collision Detection")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Create rectangles
rect1 = canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags="rect1")
rect2 = canvas.create_rectangle(200, 100, 250, 150, fill="red", tags="rect2")

# Speed of movement
dx1, dy1 = 3, 3  # Smoother speed
dx2, dy2 = -3, 3

collision_detected = False  # To prevent rapid flickering

def move_shapes():
    global dx1, dy1, dx2, dy2, collision_detected

    # Move both rectangles
    canvas.move("rect1", dx1, dy1)
    canvas.move("rect2", dx2, dy2)

    # Get new positions
    x1, y1, x2, y2 = canvas.bbox("rect1")
    a1, b1, a2, b2 = canvas.bbox("rect2")

    # Collision Detection (Prevent Flickering)
    if x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1:
        if not collision_detected:  # Change color only once
            canvas.itemconfig("rect1", fill="green")
            collision_detected = True
    else:
        canvas.itemconfig("rect1", fill="blue")
        collision_detected = False  # Reset when not colliding

    # Bounce off walls (rect1)
    if x1 <= 0 or x2 >= 400:
        dx1 = -dx1
    if y1 <= 0 or y2 >= 300:
        dy1 = -dy1

    # Bounce off walls (rect2)
    if a1 <= 0 or a2 >= 400:
        dx2 = -dx2
    if b1 <= 0 or b2 >= 300:
        dy2 = -dy2

    root.after(20, move_shapes)  # Faster refresh rate for smoother motion

# Start movement
move_shapes()

root.mainloop()
