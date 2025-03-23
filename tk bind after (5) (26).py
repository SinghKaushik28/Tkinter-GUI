from tkinter import *

def on_enter(event):
    label.config(bg="lightblue")

def on_leave(event):
    label.config(bg="white")

root = Tk()
label = Label(root, text="Hover over me", bg="white", width=20)
label.pack()
label.bind("<Enter>", on_enter)  # Mouse enters widget
label.bind("<Leave>", on_leave)  # Mouse leaves widget
root.mainloop()
