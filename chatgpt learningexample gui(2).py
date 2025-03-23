# #Event Driven
# import tkinter as tk

# def on_click(event):
#     print("Button was clicked!")

# root = tk.Tk()

# btn = tk.Button(root, text="Click Me")
# btn.pack()

# # Bind left mouse click to the button
# btn.bind("<Button-1>", on_click)

# root.mainloop()

# import tkinter as tk

# def on_key(event):
#     print(f"You pressed: {event.keysym}")

# root = tk.Tk()

# root.bind("<KeyPress>", on_key)  # Bind any key press

# root.mainloop()

# import tkinter as tk

# def track_mouse(event):
#     print(f"Mouse at ({event.x}, {event.y})")

# root = tk.Tk()
# root.bind("<Motion>", track_mouse)  # Track mouse movement

# root.mainloop()

# import tkinter as tk

# def on_click(event):
#     print("Button clicked!")
#     btn.unbind("<Button-1>")  # Disable clicking after first use

# root = tk.Tk()
# btn = tk.Button(root, text="Click Me")
# btn.pack()
# btn.bind("<Button-1>", on_click)
# root.mainloop()

# import tkinter as tk

# def start_drag(event):
#     label.startX, label.startY = event.x, event.y

# def on_drag(event):
#     x = label.winfo_x() + (event.x - label.startX)
#     y = label.winfo_y() + (event.y - label.startY)
#     label.place(x=x, y=y)

# root = tk.Tk()
# label = tk.Label(root, text="Drag Me", bg="yellow", padx=10, pady=5)
# label.place(x=50, y=50)

# label.bind("<Button-1>", start_drag)
# label.bind("<B1-Motion>", on_drag)

# root.mainloop()

# #THEME
# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry("300x200")
# root.title("Theme Example")

# # Apply a theme
# style = ttk.Style()
# style.theme_use("winnative")  # Change to "alt", "classic", etc.
# style.configure("TButton", 
#                 foreground="white", 
#                 background="black", 
#                 font=("Arial", 12, "bold"), 
#                 padding=5)


# ttk.Label(root, text="Hello, Tkinter!", font=("Arial", 12)).pack(pady=20)
# ttk.Button(root, text="Click Me").pack()

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry("300x200")
# root.title("Custom Style")

# # Define a style
# style = ttk.Style()
# style.theme_use("clam")  # Change themes here

# # Customizing button style
# style.configure("TButton", foreground="white", background="blue", font=("Arial", 12, "bold"))

# ttk.Button(root, text="Styled Button", style="TButton").pack(pady=20)

# root.mainloop()

# #FONT
# import tkinter as tk
# from tkinter import font

# root = tk.Tk()
# root.geometry("400x300")
# root.title("Font Example")

# # Custom fonts
# custom_font = font.Font(family="Comic Sans MS", size=18, weight="bold", slant="italic")

# label = tk.Label(root, text="Custom Font Example", font=custom_font)
# label.pack(pady=20)

# root.mainloop()

#IMAGE import successfull

import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Image Example")

# Load Image
img = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/Icon.png/logo.png")  # or "logo.png"
# Display Image in Label
label = tk.Label(root, image=img)
label.pack()

root.mainloop()

#using image as background
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1536x864")
root.title("Theme Example")

# Load image
img = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/Icon.png/ace.png")

# Create a Canvas widget
canvas = tk.Canvas(root, width=1536, height=864)
canvas.pack(fill="both", expand=True)

# Display the image on the canvas
canvas.create_image(0,0, anchor="nw", image=img)

# Apply a theme
style = ttk.Style()
style.theme_use("winnative")  # Change to "alt", "classic", "winnative" etc.
style.configure("TButton", 
                foreground="white", 
                background="black", 
                font=("Arial", 12, "bold"), 
                padding=5)

# Apply a second theme (optional, just for learning purposes)
style1 = ttk.Style()
style1.theme_use("clam")  # Change themes here (this won't take effect unless you reapply styles after theme change)

# Customizing button style for "clam" theme
style1.configure("TButton", foreground="white", background="blue", font=("Arial", 12, "bold"))

# Create and place buttons and labels on the canvas
canvas.create_window(150, 50, window=ttk.Label(root, text="Hello, Tkinter!", font=("Arial", 12)))
canvas.create_window(150, 100, window=ttk.Button(root, text="Styled Button", style="TButton"))
canvas.create_window(150, 150, window=ttk.Button(root, text="Click Me"))

root.mainloop()

