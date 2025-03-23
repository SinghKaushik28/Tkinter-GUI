import tkinter as tk
from tkinter import messagebox

def open_file():
    messagebox.showinfo("Open", "Open file action triggered!")

def New_file():
    messagebox.showinfo("New", "New file action triggered!")

def save_file():
    messagebox.showinfo("Save", "Save file action triggered!")

def clear_recent():
    messagebox.showwarning("Delete all Changes", "Clear all action triggered!")

def more():
    messagebox.askyesno("Proceed ?","Would like some more option to edit file")

def cut():
    messagebox.askyesnocancel("Cut", "You want use Cut")

def copy():
     messagebox.showinfo("Copy","Copy action triggered!")

def undo():
     messagebox.showerror("Undo","It will cause you to bring back errors.")

def redo():
     messagebox.showinfo("Redo","Redo action triggered!")

def open_view():
    messagebox.askquestion("Open view", "would like to view or not")

def output():
    messagebox.askokcancel("Output", "Output is already triggered!")

def terminal():
    messagebox.askretrycancel("terminal", "would like to open again")

def welcome():
    messagebox.showinfo("Welcome","For help go to All Command. ")

def all_command():
    messagebox.showinfo("All Command ","How may i help you in command.")

def exit_app():
    root.quit()

root=tk.Tk()
root.title("Menu")
root.geometry("300x400")
root.config(background="lightblue")

menubar=tk.Menu(root)
file_menu=tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="New File",command=New_file) 
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator() 
#Using 'accelerator' displays the shortcut for the menu item, but does not handle the key press event
file_menu.add_command(label="Exit", command=exit_app,accelerator="Ctrl+e")
root.bind("<Control-e>",lambda event:exit_app())#Adding 'bind' allows the shortcut to trigger the action, but it won't display the shortcut in the menu
file_menu.add_separator()
file_menu.add_command(label="Open File",command=open_file)
menubar.add_cascade(label="File",menu=file_menu)

Open_menu=tk.Menu(file_menu,tearoff=0)
Open_menu.add_command(label="Clear Recent",command=clear_recent)
Open_menu.add_command(label="More",command=more)
file_menu.add_cascade(label="Open Recent",menu=Open_menu)

edit_menu=tk.Menu(menubar,tearoff=0)
edit_menu.add_command(label="cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_separator()
#Dybamic menu in undo,redo
edit_menu.add_command(label="Undo",command=undo, state="normal")
edit_menu.add_command(label="Redo",command=redo, state="disabled")
#Dynamically enable or disable undo and redo option in menu
edit_menu.entryconfig("Redo", state="normal")  #Enable Redo
edit_menu.entryconfig("Undo", state="disabled") #Disable Undo
#simple method of enable or disable in menu is checkbutton
# edit_menu.add_checkbutton(label="Undo", command=undo)
# edit_menu.add_checkbutton(label="Redo", command=redo)
menubar.add_cascade(label="Edit",menu=edit_menu) #Add the Edit menu to the menubar, with the label "Edit" appearing in the menubar,Links the edit_menu to the "Edit" item on the menubar.


view_menu=tk.Menu(menubar,tearoff=0)
view_menu.add_command(label="Open View",command=open_view)
view_menu.add_command(label="Output",command=output)
view_menu.add_command(label="Terminal",command=terminal)
menubar.add_cascade(label="View",menu=view_menu)

help_menu=tk.Menu(menubar,tearoff=0)#This creates a top-level menu named help_menu that will be added to the main menubar.
#help_menu.add_command(label="Help") ##if i want one optiona nd not some other submenu of it i will just have to use this line
menubar.add_cascade(label="....",menu=help_menu)

help_option=tk.Menu(help_menu,tearoff=0)
help_option.add_command(label="Welcome",command=welcome)
help_option.add_command(label="All Commmand",command=all_command)
help_menu.add_cascade(label="Help",menu=help_option)

#Adding keyboard shortcut bind allow to link shortcut but it wont show its shortcut in fron of that submenu 
root.bind("<Control-s>",lambda event: save_file())
root.bind("<Control-o>",lambda event: open_file())

frame=tk.Frame(root)
frame.grid()

text=tk.Text(frame,wrap="none",height=46,width=182)
text.pack(side="left",fill="both",expand="True")

scrollbar=tk.Scrollbar(frame,command=text.yview)
scrollbar.pack(side="right",fill="y")
text.config(yscrollcommand=scrollbar.set)
scrollbar1=tk.Scrollbar(frame,orient="horizontal",command=text.xview)
scrollbar1.pack(side="bottom",fill="x")
text.config(xscrollcommand=scrollbar1.set)


root.config(menu=menubar)
root.mainloop()