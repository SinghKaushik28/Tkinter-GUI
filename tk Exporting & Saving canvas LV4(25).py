import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

def save_canvas():
    # Ask user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("All Files", "*.*")])
    if file_path:
        # Get Canvas dimensions
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        
        # Capture the Canvas as an image
        image = Image.new("RGB", (canvas.winfo_width(), canvas.winfo_height()), "white")
        draw = ImageDraw.Draw(image)
        
        # Save the image
        image.save(file_path)
        print("Canvas saved as:", file_path)

# Create Tkinter window
root = tk.Tk()
root.title("Canvas Save Example")

# Create Canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw shapes for testing
canvas.create_rectangle(50, 50, 200, 150, outline="black", width=2)
canvas.create_text(100, 200, text="Hello World!", font=("Arial", 14))

# Save Button
btn_save = tk.Button(root, text="Save", command=save_canvas)
btn_save.pack()

root.mainloop()
