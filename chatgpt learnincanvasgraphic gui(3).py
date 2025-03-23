# ## LEVEL 1
# ##basic deleting shape after 3 seconds
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Delete Example")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# # Creating a rectangle
# rect = canvas.create_rectangle(50, 50, 200, 150, fill="blue")

# # Function to delete rectangle
# def delete_rectangle():
#     canvas.delete(rect)

# # Delete rectangle after 3 seconds
# root.after(3000, delete_rectangle)

# root.mainloop()

# ## LEVEL 2
# # #moving shape using the button which we created
# import tkinter as tk

# root = tk.Tk()
# root.title("Move Shape Example")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# # Creating a rectangle
# rect = canvas.create_rectangle(150, 100, 250, 150, fill="blue")

# # Move shape functions 
# def move_left():
#     canvas.move(rect, -10, 0)

# def move_right():
#     canvas.move(rect, 10, 0)

# # Buttons to move rectangle
# btn_left = tk.Button(root, text="Move Left", command=move_left)
# btn_left.pack(side="left", padx=10)

# btn_right = tk.Button(root, text="Move Right", command=move_right)
# btn_right.pack(side="right", padx=10)

# root.mainloop()

# #moving shape using the keyboard and mouse which we created
# import tkinter as tk

# root = tk.Tk()
# root.title("Keyboard Control")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# rect = canvas.create_rectangle(150, 100, 250, 150, fill="blue")

# # Function to move rectangle
# def move(event):
#     if event.keysym == "Left":
#         canvas.move(rect, -10, 0)
#     elif event.keysym == "Right":
#         canvas.move(rect, 10, 0)
#     elif event.keysym == "Up":
#         canvas.move(rect, 0, -10)
#     elif event.keysym == "Down":
#         canvas.move(rect, 0, 10)

# # Bind keys
# root.bind("<Left>", move)
# root.bind("<Right>", move)
# root.bind("<Up>", move)
# root.bind("<Down>", move)

# root.mainloop()

# #change shape and colour on click
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Update")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# rect = canvas.create_rectangle(150, 100, 250, 150, fill="blue")

# # Function to change color
# def change_color(event):
#     canvas.itemconfig(rect, fill="red")

# # Bind left-click to change color
# canvas.tag_bind(rect, "<Button-1>", change_color)

# root.mainloop()

# ## LEVEL-3
# ##Moving a Ball in a Loop
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Animation")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# ball = canvas.create_oval(50, 50, 80, 80, fill="red")

# dx, dy = 2, 2  # Speed

# def move_ball():
#     global dx, dy
#     canvas.move(ball, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(ball)

#     # Bounce off walls
#     if x1 <= 0 or x2 >= 400:
#         dx = -dx
#     if y1 <= 0 or y2 >= 300:
#         dy = -dy

#     root.after(20, move_ball)  # Call function every 20ms

# move_ball()  # Start animation
# root.mainloop()

# #Detect Collision Between Two Shapes
# import tkinter as tk

# root = tk.Tk()
# root.title("Smooth Collision Detection")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# # Create rectangles
# rect1 = canvas.create_rectangle(50, 50, 100, 100, fill="blue", tags="rect1")
# rect2 = canvas.create_rectangle(200, 100, 250, 150, fill="red", tags="rect2")

# # Speed of movement
# dx1, dy1 = 3, 3  # Smoother speed
# dx2, dy2 = -3, 3

# collision_detected = False  # To prevent rapid flickering

# def move_shapes():
#     global dx1, dy1, dx2, dy2, collision_detected

#     # Move both rectangles
#     canvas.move("rect1", dx1, dy1)
#     canvas.move("rect2", dx2, dy2)

#     # Get new positions
#     x1, y1, x2, y2 = canvas.bbox("rect1")
#     a1, b1, a2, b2 = canvas.bbox("rect2")

#     # Collision Detection (Prevent Flickering)
#     if x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1:
#         if not collision_detected:  # Change color only once
#             canvas.itemconfig("rect1", fill="green")
#             collision_detected = True
#     else:
#         canvas.itemconfig("rect1", fill="blue")
#         collision_detected = False  # Reset when not colliding

#     # Bounce off walls (rect1)
#     if x1 <= 0 or x2 >= 400:
#         dx1 = -dx1
#     if y1 <= 0 or y2 >= 300:
#         dy1 = -dy1

#     # Bounce off walls (rect2)
#     if a1 <= 0 or a2 >= 400:
#         dx2 = -dx2
#     if b1 <= 0 or b2 >= 300:
#         dy2 = -dy2

#     root.after(20, move_shapes)  # Faster refresh rate for smoother motion

# # Start movement
# move_shapes()

# root.mainloop()

# ##complex shape & Patterns
# ##Star Pattern using
# import tkinter as tk

# root = tk.Tk()
# root.title("Star Pattern")

# canvas = tk.Canvas(root, width=400, height=400, bg="white")
# canvas.pack()

# # Star Coordinates
# points = [200, 50,  250, 150,  350, 150,  
#           270, 200,  300, 300,  200, 250,  
#           100, 300,  130, 200,  50, 150,  150, 150]

# canvas.create_polygon(points, outline="black", fill="yellow", width=3)

# root.mainloop()

# #Canvas-Based Button
# import tkinter as tk

# root = tk.Tk()
# root.title("Custom Canvas Button")

# canvas = tk.Canvas(root, width=400, height=200, bg="white")
# canvas.pack()

# # Draw button
# button_rect = canvas.create_rectangle(100, 50, 300, 100, fill="lightblue")

# # Draw button text
# button_text = canvas.create_text(200, 75, text="Click Me", font=("Arial", 16))

# # Button click function
# def on_click(event):
#     canvas.itemconfig(button_rect, fill="green")  # Change color on click
#     canvas.itemconfig(button_text, text="Clicked!")

# # Bind click event
# canvas.tag_bind(button_rect, "<Button-1>", on_click)
# canvas.tag_bind(button_text, "<Button-1>", on_click)

# root.mainloop()

# #Paint App
# import tkinter as tk

# root = tk.Tk()
# root.title("Paint App")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# # Drawing function
# def draw(event):
#     x, y = event.x, event.y
#     canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", outline="black")

# # Bind mouse drag to draw
# canvas.bind("<B1-Motion>", draw)

# root.mainloop()
