import tkinter as tk 

root=tk.Tk()
root.title("level 3")
root.geometry("400x400")

shape_id= None
colors_index=0

canvas=tk.Canvas(root,height=300,width=300,bg="black")
canvas.pack()

entry=tk.Entry(root,width=30)
entry.pack(side="bottom")

def shape():
 global shape_id
 sh =entry.get().strip().lower()
 if shape_id:
        canvas.delete(shape_id)
 if sh.lower()=="rectangle":
  shape_id = canvas.create_rectangle(150, 100, 250, 150, fill="white")
 elif sh.lower()=="oval":
  shape_id=canvas.create_oval(150,100,250,150,fill="white")
 elif sh.lower()=="polygon":
  shape_id=canvas.create_polygon(150,100,250,150,fill="white")
 elif sh.lower()=="line": 
  shape_id=canvas.create_line(150,100,250,150,fill="white")
 elif sh.lower()=="arc": 
  shape_id=canvas.create_arc(150,100,250,150,fill="white")
 elif sh.lower()=="star":
   points = [200, 50,  250, 150,  350, 150,  
             270, 200,  300, 300,  200, 250,  
             100, 300,  130, 200,  50, 150,  150,150]
   shape_id=canvas.create_polygon(points, outline="red", fill="white", width=3)
 else:
        print("Invalid shape name! Use rectangle, oval, polygon, line, or arc.")

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

def change(event):
   global shape_id,colors_index
   colors=["orange","light green","light blue","white"]
   if shape_id:  
        canvas.itemconfig(shape_id, fill=colors[colors_index])  # Change color
        
        colors_index = (colors_index + 1) % len(colors)

btn_create=tk.Button(root,text="Create",command=shape)
btn_create.pack()

root.bind("<Left>",lambda event:move(event))
root.bind("<Right>",lambda event:move(event))
root.bind("<Up>",lambda event:move(event))
root.bind("<Down>",lambda event:move(event))
root.bind("<Button-3>",lambda event:change(event))
root.mainloop()