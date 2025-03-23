import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1536x864")
root.title("Theme Example")

# Load image
img = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/CODE/GUI/Icon.png/ace.png")

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
