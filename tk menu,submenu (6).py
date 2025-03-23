import tkinter as tk
from tkinter import messagebox

def open_file():
    messagebox.showinfo("Open", "Open file action triggered!")

def save_file():
    messagebox.showinfo("Save", "Save file action triggered!")

def exit_app():
    root.quit()

root=tk.Tk()
root.title("Menu")
root.geometry("300x400")
root.config(background="lightblue")

menubar=tk.Menu(root)#This line creates a menu bar for the root window.
file_menu=tk.Menu(menubar,tearoff=0)
#Add commands (actions) to the File menu.
file_menu.add_command(label="New File",command=open_file) #Adds the "Open" command to the File menu
file_menu.add_command(label="Save",command=save_file) #Adds the "Save" command to the File menu
file_menu.add_separator() #Adds a separator line between exit and above open,save in the File menu
file_menu.add_command(label="Exit", command=exit_app) #Adds the "Exit" command to the File menu.
menubar.add_cascade(label="File",menu=file_menu)#This line adds the file_menu to the menubar,label="File" specifies the text that will appear in the menu bar for this item. In this case, the text "File" will be shown in the menu bar
#menu=file_menu links the file_menu object (which holds the items like "Open", "Save", and "Exit") to the "File" menu on the menu bar.

edit_menu=tk.Menu(menubar,tearoff=0)#Create an Edit menu with no tearoff (can't be separated as a floating menu).
edit_menu.add_command(label="cut")#Adds the "cut" command to the Edit menu
edit_menu.add_command(label="Copy")
edit_menu.add_separator()
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
menubar.add_cascade(label="Edit",menu=edit_menu) #Add the Edit menu to the menubar, with the label "Edit" appearing in the menubar,Links the edit_menu to the "Edit" item on the menubar.

view_menu=tk.Menu(menubar,tearoff=0)
view_menu.add_command(label="Open View")
view_menu.add_command(label="Output")
view_menu.add_command(label="Terminal")
menubar.add_cascade(label="View",menu=view_menu)

help_menu=tk.Menu(menubar,tearoff=0)
help_menu.add_command(label="Help")
menubar.add_cascade(label="....",menu=help_menu)


frame=tk.Frame(root)
frame.grid()

text=tk.Text(frame,wrap="none",height=24,width=76)
text.pack(side="left",fill="both",expand="True")

scrollbar=tk.Scrollbar(frame,command=text.yview)#for y axis scroll or u can say vertical scrolls
scrollbar.pack(side="right",fill="y")#placing it at right side,filling in vertical way
text.config(yscrollcommand=scrollbar.set)
scrollbar1=tk.Scrollbar(frame,orient="horizontal",command=text.xview)#for x axis scroll,it works when we exceed the words after geometry
scrollbar1.pack(side="bottom",fill="x")
text.config(xscrollcommand=scrollbar1.set)

for i in range(1,100):
    text.insert(tk.END,f"Its line number is {i}\n")

root.config(menu=menubar)
root.mainloop()