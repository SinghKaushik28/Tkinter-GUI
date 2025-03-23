import tkinter as tk

root = tk.Tk()
root.title("Move Shape Example")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

shape_id= None

# Creating shapes
def shape():
 global shape_id
 sh =shape_entry.get().strip().lower()
 if shape_id:
        canvas.delete(shape_id)
 if sh.lower()=="rectangle":
  shape_id = canvas.create_rectangle(150, 100, 250, 150, fill="blue")
 elif sh.lower()=="oval":
  shape_id=canvas.create_oval(150,100,250,150,fill="blue")
 elif sh.lower()=="polygon":
  shape_id=canvas.create_polygon(150,100,250,150,fill="blue")
 elif sh.lower()=="line": 
  shape_id=canvas.create_line(150,100,250,150,fill="black")
 elif sh.lower()=="arc": 
  shape_id=canvas.create_arc(150,100,250,150,fill="blue")
 else:
        print("Invalid shape name! Use rectangle, oval, polygon, line, or arc.")

# Move shape functions 
def move(event):
    global shape_id
    root.focus_set() ## Force main window to take focus (fix arrow key issue)

    if shape_id:
     if event.keysym=="Left":
        canvas.move(shape_id,-10, 0)
     if event.keysym=="Right":
       canvas.move(shape_id, 10, 0)    
     if event.keysym=="Up":
        canvas.move(shape_id, 0, -10)
     if event.keysym=="Down":
        canvas.move(shape_id, 0, 10)

shape_entry=tk.Entry(root,width=20)
shape_entry.pack(side="bottom")

btn_create=tk.Button(root,text="Create",command=shape)
btn_create.pack()
# Buttons to move shape using screen button
btn_left = tk.Button(root, text="Move Left",  command=lambda event=None: move(event))
btn_left.pack(side="left", padx=10)

btn_right = tk.Button(root, text="Move Right",  command=lambda event=None: move(event))
btn_right.pack(side="right", padx=10)

root.bind("<Left>",lambda event:move(event))
root.bind("<Right>",lambda event:move(event))
root.bind("<Up>",lambda event:move(event))
root.bind("<Down>",lambda event:move(event))

root.mainloop()