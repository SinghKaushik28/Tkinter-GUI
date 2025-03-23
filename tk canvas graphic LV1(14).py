import tkinter as tk
from tkinter import *

def delete_rectangle():
     canvas.delete(rec)

root=tk.Tk()
root.title("Graphics")
root.geometry("400x500")

frame=tk.Frame(root).pack()

canvas=tk.Canvas(root,height=360,width=320,bg="white")
canvas.pack()
rec=canvas.create_rectangle(80,80,280,280,fill="blue")

root.after(3000,delete_rectangle)

root.mainloop()
