#thre is a image i imported use same path
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Theme Example")

img = tk.PhotoImage(file="C:/Users/KAUSHIK/OneDrive/Documents/CODE/GUI/Icon.png/logo.png")
label = tk.Label(root, image=img)
label.pack()

# Apply a second theme (optional, just for learning purposes)
style = ttk.Style()
style.theme_use("clam")  # Change themes here (this won't take effect unless you reapply styles after theme change)

# Customizing button style for "clam" theme
style.configure("TButton", foreground="white", background="blue", font=("Arial", 12, "bold"))

# Create and pack buttons
ttk.Button(root, text="Styled Button", style="TButton").pack(pady=20)
ttk.Label(root, text="Hello, Tkinter!", font=("Arial", 12)).pack(pady=20)
ttk.Button(root, text="Click Me").pack(pady=10)
#Both blue bcz the rule is only one theme at one time
root.mainloop()
