import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

def rec():
 global canvas
# Drawing a rectangle
 canvas.create_rectangle(50, 50, 200, 150, fill="blue")
def ov():
 global canvas
 canvas.create_oval(40,40,200,150,fill="red")

listbox = tk.Listbox(root)
listbox.pack()

# Drawing a rectangle #if only one shape in gui no need of function
#canvas.create_rectangle(50, 50, 200, 150, fill="blue")

# Adding items
listbox.insert(1, "rectangle")
root.bind("rectangle",lambda event:rec())#rectangle from listbox will not be clicked or work but when you write rectangle rec function will work and show shape
listbox.insert(2, "oval")
root.bind("oval",lambda event:ov())
listbox.insert(3, "Cherry")

root.mainloop()