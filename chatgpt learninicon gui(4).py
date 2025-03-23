#levl 1
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Custom Window Icon")

# Set the window icon (ONLY .ico files)
root.iconbitmap("C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/icon.ico")

tk.Label(root, text="Custom Icon Set!", font=("Arial", 12)).pack(pady=20)

root.mainloop()

#creates custom icon of your given image in fromat of .png
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Custom PNG Icon")

# Set a .png image as the icon
icon = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/Icon.png/logo.png")
root.iconphoto(True, icon)  # Apply icon to window

tk.Label(root, text="PNG Icon Set!", font=("Arial", 12)).pack(pady=20)

root.mainloop()


#Level 2
#adding image or icon to the button
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Button with Icon")

# Load Image (Only PNG works natively in Tkinter)
icon = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/Icon.png/logo.png")

# Button with an icon
button = tk.Button(root, image=icon, compound="left",height=16,width=14)  # Use "top", "right", "bottom" if needed
button.pack(pady=20)

root.mainloop()

#adding image or icon to the label
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Label with Icon")

# Load Image
icon = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/Icon.png/blue lock.png",height=16,width=16)

# Label with an icon
label = tk.Label(root, text="Hello!", image=icon, compound="left", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()

#button with icon but perfect size as buuton icon
import tkinter as tk
from PIL import Image, ImageTk  # Install Pillow if needed: pip install pillow

root = tk.Tk()
root.geometry("300x200")
root.title("Resized Icon in Button")

# Load and resize the image
img = Image.open("C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/Icon.png/ace.png")
img = img.resize((50, 50))  # Resize to 50x50 pixels
icon = ImageTk.PhotoImage(img)

# Button with resized icon
button = tk.Button(root, image=icon, compound="left")
button.pack(pady=20)

root.mainloop()

#Levl3
# for windows or linux app icon
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("my_custom_app")

import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
root.title("App Icon in Taskbar")
root.iconbitmap("C:/Users/KAUSHIK/Documents/PYTHONALL/GUI/Icon.ico")

tk.Label(root, text="Look at the Taskbar!", font=("Arial", 12)).pack(pady=20)
root.mainloop()

