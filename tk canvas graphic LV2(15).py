import tkinter as tk

root = tk.Tk()
root.title("Move Shape Example")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Creating a rectangle
rect = canvas.create_rectangle(150, 100, 250, 150, fill="blue")

# Move shape functions 
def move_left():
    canvas.move(rect, -10, 0)

def move_right():
    canvas.move(rect, 10, 0)

def move_up():
    canvas.move(rect, 0, -10)

def move_down():
    canvas.move(rect, 0, 10)

def move(event):
    if event.keysym=="Left":
        canvas.move(rect, -10, 0)
    if event.keysym=="Right":
       canvas.move(rect, 10, 0)    
    if event.keysym=="Up":
        canvas.move(rect, 0, -10)
    if event.keysym=="Down":
        canvas.move(rect, 0, 10)

# Buttons to move rectangle
btn_left = tk.Button(root, text="Move Left", command=move_left)
btn_left.pack(side="left", padx=10)

btn_right = tk.Button(root, text="Move Right", command=move_right)
btn_right.pack(side="right", padx=10)

root.bind("<Left>",lambda event:move(event))
root.bind("<Right>",lambda event:move(event))
root.bind("<Up>",lambda event:move(event))
root.bind("<Down>",lambda event:move(event))

root.mainloop()