import tkinter as tk
from tkinter import messagebox

#all function defined here
def open():
    messagebox.showinfo("Open","Action triggered!")
def save():
    messagebox.showinfo("Save","Action triggered!")
def New():
    messagebox.showinfo("New File","Action triggered!")
def exit():
    root.quit()
def delete():
     if messagebox.askokcancel("proceed?","it will delte the history "):  #Only runs if user confirms
      messagebox.showwarning("Delte history","Action triggered!")
def search():
    messagebox.askyesno("did you mean ...","Action triggered!")
def cut():
    messagebox.showerror("Cut","cant proceed the cut action")
def copy():
    messagebox.askyesnocancel("Copy","would you really want to copy that")
def paste():
    messagebox.askyesno("Paste","would you like to paste here")
def undo():
    messagebox.showinfo("Undo","Action triggered!")
    edit_menu.entryconfig("Undo", state="disabled") 
    edit_menu.entryconfig("Redo", state="normal") 
def redo():
    messagebox.showinfo("Redo","Action triggered!")
    edit_menu.entryconfig("Undo", state="normal")  
    edit_menu.entryconfig("Redo", state="disable")

def submit(event):
     print("Submit was clicked!")
     bt.unbind("<Button-1>")  # Disable clicking after first use
def key(event):
     print(f"You pressed: {event.keysym}")
def track(event):
     print(f"Mouse at ({event.x}, {event.y})")

def start_drag(event):
    label.startX, label.startY = event.x, event.y
def on_drag(event):
    x = label.winfo_x() + (event.x - label.startX)
    y = label.winfo_y() + (event.y - label.startY)
    label.place(x=x, y=y)

def change():
    frame.config(bg="light blue")

root=tk.Tk()
root.title("Event")
root.geometry("400x500")

#creating a frame
frame=tk.Frame(root)
frame.pack()

#labeling at top
tk.Label(frame,text="Hello in event Gui").pack()

#button which will be dragged in place of button it can be label ...etc
label = tk.Button(root, text="zoom in", bg="light blue", padx=10, pady=5)
label.place(x=50, y=50)
label.bind("<Button-1>", start_drag)
label.bind("<B1-Motion>", on_drag)

#for text entry box with no limit
text=tk.Text(frame,font=("Arial",18,"bold"),wrap="word")
text.pack(fill="both",expand="true")

#for scrollbar
scrollbar=tk.Scrollbar(frame,command=text.yview)
scrollbar.pack(side="right",fill="y")
text.config(yscrollcommand=scrollbar.set)

#foe making a accept term option
var =tk.IntVar()
c=tk.Checkbutton(frame, text="Accept Terms", variable=var)
c.pack(side="bottom")

#Events
#submit event if i dont write unbined in def of submit than submit can be clicked unlimited time but for one time click we rite unbind in def of that button
bt=tk.Button(frame,text="Submit")
bt.pack(side="bottom")
bt.bind("<Button-1>",submit)
#key eventbind any key press
text.bind("<KeyPress>",key)
#mouse movement bind
root.bind("<Motion>",track)

#creating a menu
menubar=tk.Menu(root,tearoff=0)
file_menu=tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="Open",command=open)
file_menu.add_command(label="New File",command=New)
file_menu.add_command(label="Save",command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit)
menubar.add_cascade(label="File",menu=file_menu)
#creating a submenu in File 
option=tk.Menu(file_menu,tearoff=0)
option.add_command(label="delete history",command=delete)
option.add_command(label="search history",command=search)
file_menu.add_cascade(label="History",menu=option)

edit_menu=tk.Menu(menubar,tearoff=0)
edit_menu.add_command(label="cut",command=cut)
edit_menu.add_command(label="copy",command=copy,accelerator="Ctrl+C")
root.bind("<Control-c>",lambda event:copy())
edit_menu.add_command(label="paste",command=paste)
edit_menu.add_separator()
#dynamic menu in undo and redo using check button
edit_menu.add_checkbutton(label="Undo", command=undo)
edit_menu.add_checkbutton(label="Redo", command=redo)
menubar.add_cascade(label="Edit",menu=edit_menu)

#context menu but work only when right clicked in frame area
change_framecolour=tk.Menu(root,tearoff=0)
change_framecolour.add_command(label="change colour",command=change)
def show_context(event):
    change_framecolour.post(event.x_root,event.y_root)
    return "break" 
frame.bind("<Button-3>",show_context)

#context menu option available when right click in text box or its area
option=tk.Menu(root,tearoff=0)
option.add_command(label="copy",command=copy)
def show_option(event):
    option.post(event.x_root,event.y_root)
text.bind("<Button-3>",show_option)

#keyword shortcut creating
root.bind("<Control-o>",lambda event:open())
root.bind("<Control-s>",lambda event:save())

root.config(menu=menubar)
root.mainloop()