import tkinter as tk 
from tkinter import messagebox

def open():
    messagebox.showinfo("Open","Action triggered!")
def export():
    messagebox.showinfo("export","Action triggered!")
def change():
    frame.config(bg="light blue")
def copy():
    messagebox.showinfo("copy","Action triggered!")

root=tk.Tk()
root.title("Context menu")
root.geometry("400x400")
root.config(background="Black")

frame=tk.Frame(root)
frame.pack()

text=tk.Text(frame,height=48,width=100)
text.pack(padx=20,pady=18,side="left",fill="both",expand="True")
scrollbar=tk.Scrollbar(frame,command=text.yview)
scrollbar.pack(side="right")
text.config(yscrollcommand=scrollbar.set)

#normal menu
menubar=tk.Menu(root)
file_menu=tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="Open",command=open,accelerator="Ctrl+o")
root.bind("<Control-o>",lambda event:open())
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_separator()
#submenu in file menu
share_menu=tk.Menu(file_menu,tearoff=0)
share_menu.add_command(label="Export profile",command=export)
root.bind("<Control-q>",lambda event:export)
file_menu.add_cascade(label="Share",menu=share_menu)

#Create a context (right-click) menu
change_menu=tk.Menu(root,tearoff=0)#Create a menu, setting `tearoff=0` to prevent it from detaching
change_menu.add_command(label="change colour",command=change)#Add an option to change the frame's background color

#Function to display the context menu at the cursor position when right-clicked
def show_context(event):
    change_menu.post(event.x_root,event.y_root)#Show the menu at the mouse cursor's position (absolute screen coordinates)
#Bind right-click (`<Button-3>`) to the `show_context` function on `frame'
    return "break"  # Prevents default context menu from appearing
frame.bind("<Button-3>",show_context) #When right-clicking on frame area , call `show_context` to show the menu
#in place of frame u can use root as well than the right click context menu will on visible in root area which is whole area of gui

option=tk.Menu(root,tearoff=0)
option.add_command(label="copy",command=copy)

def show_option(event):
    option.post(event.x_root,event.y_root)
text.bind("<Button-3>",show_option)#binding copy menu option of right click only in text box area only

root.config(menu=menubar)
root.mainloop()
