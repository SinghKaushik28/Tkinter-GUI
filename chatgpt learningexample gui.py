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

# import tkinter as tk
# import random

# def move_button():
#     # Move button to a random position
#     x = random.randint(0, 300)
#     y = random.randint(0, 300)
#     click_button.place(x=x, y=y)

# def increment_score():
#     global score
#     score += 1
#     score_label.config(text=f"Score: {score}")
#     move_button()

# window = tk.Tk()
# window.title("Button Click Game")
# window.geometry("400x400")

# score = 0

# score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 14))
# score_label.pack()

# click_button = tk.Button(window, text="Click Me!", command=increment_score)
# click_button.place(x=150, y=150)

# window.mainloop()

# from tkinter import *

# def on_enter(event):
#     label.config(bg="lightblue")

# def on_leave(event):
#     label.config(bg="white")

# root = Tk()
# label = Label(root, text="Hover over me", bg="white", width=20)
# label.pack()
# label.bind("<Enter>", on_enter)  # Mouse enters widget
# label.bind("<Leave>", on_leave)  # Mouse leaves widget
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# # Function to show different messageboxes
# def show_message():
#     messagebox.showinfo("Info", "This is an information message!")
#     messagebox.showwarning("Warning", "This is a warning message!")
#     messagebox.showerror("Error", "This is an error message!")

# def ask_user():
#     response = messagebox.askyesno("Confirmation", "Do you want to proceed?")
#     if response:
#         label.config(text="You chose to proceed!")
#     else:
#         label.config(text="You chose not to proceed.")

# # Tkinter setup
# root = tk.Tk()
# root.title("Messagebox Example")

# btn_info = tk.Button(root, text="Show Messages", command=show_message)
# btn_info.pack(pady=10)

# btn_ask = tk.Button(root, text="Ask Question", command=ask_user)
# btn_ask.pack(pady=10)

# label = tk.Label(root, text="")
# label.pack(pady=10)

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# # Create a Frame
# # frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
# # frame.pack(fill=tk.BOTH, expand=True)

# # Add widgets to the Frame
# label = tk.Label(root, text="This is a label inside a frame")
# label.pack()

# button = tk.Button(root, text="Click Me")
# button.pack()

# root.mainloop()

#chess board
# import tkinter as tk

# def chessboard():
#     root = tk.Tk()
#     root.title("Chess Game")
#     root.geometry("600x500")

#     frame = tk.Frame(root)
#     frame.pack()

#     rows, cols = 8, 8
#     square_size = 50

#     for row in range(rows):
#         for col in range(cols):
#             color = "white" if (row + col) % 2 == 0 else "black"
#             canvas = tk.Canvas(frame, width=square_size, height=square_size, bg=color)
#             canvas.grid(row=row, column=col)

#     root.mainloop()

# chessboard()

#showcasee the use of messagebox,how to create the little above simple because so many option of menu
# import tkinter as tk
# from tkinter import messagebox

# # Functions for menu actions
# def open_file():
#     messagebox.showinfo("Open", "Open file action triggered!")

# def save_file():
#     messagebox.showinfo("Save", "Save file action triggered!")

# def exit_app():
#     root.quit()

# def cut():
#     messagebox.showinfo("Cut", "Cut action triggered!")

# def copy():
#     messagebox.showinfo("Copy", "Copy action triggered!")

# def paste():
#     messagebox.showinfo("Paste", "Paste action triggered!")

# def toggle_line_numbers():
#     state = "enabled" if show_line_numbers.get() else "disabled"
#     messagebox.showinfo("View", f"Line numbers {state}!")

# def apply_theme():
#     selected_theme = theme.get()
#     messagebox.showinfo("Theme", f"Theme set to: {selected_theme}")

# # Root window
# root = tk.Tk()
# root.title("Menu Example")
# root.geometry("400x300")

# # Create the menu bar
# menubar = tk.Menu(root)

# # File Menu
# file_menu = tk.Menu(menubar, tearoff=0)
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=exit_app)
# menubar.add_cascade(label="File", menu=file_menu)

# # Edit Menu
# edit_menu = tk.Menu(menubar, tearoff=0)
# edit_menu.add_command(label="Cut", command=cut)
# edit_menu.add_command(label="Copy", command=copy)
# edit_menu.add_command(label="Paste", command=paste)
# menubar.add_cascade(label="Edit", menu=edit_menu)

# # View Menu
# view_menu = tk.Menu(menubar, tearoff=0)
# show_line_numbers = tk.BooleanVar()
# view_menu.add_checkbutton(label="Show Line Numbers", variable=show_line_numbers, command=toggle_line_numbers)

# theme = tk.StringVar(value="Light")
# view_menu.add_radiobutton(label="Light Theme", variable=theme, value="Light", command=apply_theme)
# view_menu.add_radiobutton(label="Dark Theme", variable=theme, value="Dark", command=apply_theme)
# view_menu.add_radiobutton(label="med Theme", variable=theme, value="med", command=apply_theme)

# menubar.add_cascade(label="View", menu=view_menu)

# # Help Menu
# help_menu = tk.Menu(menubar, tearoff=0)
# help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a menu example!"))
# menubar.add_cascade(label="Help", menu=help_menu)

# # Configure the menu bar
# root.config(menu=menubar)

# # Run the application
# root.mainloop()


#simple menu bcz less option 
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox

# # Functions for menu actions
# def open_file():
#     messagebox.showinfo("Open", "Open file action triggered!")

# def save_file():
#     messagebox.showinfo("Save", "Save file action triggered!")

# def exit_app():
#     root.quit()

# # Root window
# root = tk.Tk()
# root.title("Simple Menu Example")
# root.geometry("400x300")

# # Create the menu bar
# menubar = tk.Menu(root)

# # File Menu
# file_menu = tk.Menu(menubar, tearoff=0)  # Tear-off disabled
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=exit_app)
# menubar.add_cascade(label="File", menu=file_menu)

# #for unending input box
# text = Text(root, wrap=WORD)
# text.pack(side=LEFT, fill=BOTH, expand=True)  # Make sure text fills the space

# # Edit Menu
# edit_menu = tk.Menu(menubar, tearoff=0)
# edit_menu.add_command(label="Cut", command=lambda: messagebox.showinfo("Cut", "Cut action triggered!"))
# edit_menu.add_command(label="Copy", command=lambda: messagebox.showinfo("Copy", "Copy action triggered!"))
# edit_menu.add_command(label="Paste", command=lambda: messagebox.showinfo("Paste", "Paste action triggered!"))
# menubar.add_cascade(label="Edit", menu=edit_menu)

# # Configure the menu bar
# root.config(menu=menubar)

# # Run the application
# root.mainloop()


# # scrollbar
# from tkinter import *
# root = Tk()
# text = Text(root, wrap=WORD)
# text.pack(side=LEFT)
# scrollbar = Scrollbar(root, command=text.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# text.config(yscrollcommand=scrollbar.set)
# root.mainloop()

# #Scrollbar
# import tkinter as tk
# from tkinter import *

# # Root window setup
# root = tk.Tk()
# root.title("Scrollbar Example")
# root.geometry("500x400")

# # Frame to hold the Text widget and Scrollbar
# frame = Frame(root)
# frame.pack(fill=BOTH, expand=True)

# # Text widget
# text = Text(frame, wrap=WORD, height=15, width=50)
# text.pack(side=LEFT, fill=BOTH, expand=True)

# # Scrollbar widget
# scrollbar = Scrollbar(frame, command=text.yview)
# scrollbar.pack(side=RIGHT, fill=Y)

# # Linking the Scrollbar to the Text widget
# text.config(yscrollcommand=scrollbar.set)

# # Add some sample content to the Text widget
# for i in range(1, 101):
#     text.insert(END, f"This is line number {i}\n")

# # Run the application
# root.mainloop()


#Context menu

# import tkinter as tk
# from tkinter import messagebox

# def open_action():
#     messagebox.showinfo("Open", "Open action triggered!")

# def copy_action():
#     messagebox.showinfo("Copy", "Copy action triggered!")

# def paste_action():
#     messagebox.showinfo("Paste", "Paste action triggered!")

# # Create main window
# root = tk.Tk()
# root.title("Context Menu Example")
# root.geometry("400x300")

# # Create a context menu
# context_menu = tk.Menu(root, tearoff=0)
# context_menu.add_command(label="Open", command=open_action)
# context_menu.add_command(label="Copy", command=copy_action)
# context_menu.add_command(label="Paste", command=paste_action)
# context_menu.add_separator()  # Adds a separator line
# context_menu.add_command(label="Exit", command=root.quit)



# # Function to show the context menu
# def show_context_menu(event):
#     context_menu.post(event.x_root, event.y_root)

# # Bind right-click event to show context menu
# root.bind("<Button-3>", show_context_menu)

# # Run the application
# root.mainloop()

#options in context menu
import tkinter as tk

def text_copy():
    print("Text Copied!")

def text_paste():
    print("Text Pasted!")

def frame_color_change():
    frame.config(bg="lightblue")

root = tk.Tk()
root.geometry("400x300")

# Frame context menu
frame = tk.Frame(root, bg="black")
frame.pack()

frame_menu = tk.Menu(root, tearoff=0)
frame_menu.add_command(label="Change Color", command=frame_color_change)

text = tk.Text(frame, height=20, width=30)  # Now placed inside frame
text.pack(padx=10,pady=12,side="left",fill="both",expand="True")

# Textbox context menu
text_menu = tk.Menu(root, tearoff=0)
text_menu.add_command(label="Copy", command=text_copy)
text_menu.add_command(label="Paste", command=text_paste)

# Function to display text context menu (copy/paste) and prevent default menu
def show_text_menu(event): 
    text_menu.post(event.x_root, event.y_root)
    return "break"  # Prevents default context menu from appearing
# Function to display frame context menu (change color)
def show_frame_menu(event):
    frame_menu.post(event.x_root, event.y_root)

# Binding right-click for Frame
frame.bind("<Button-3>", show_frame_menu)  

# Binding right-click for Text widget, preventing the default menu
text.bind("<Button-3>", show_text_menu)

root.mainloop()
