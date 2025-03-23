
from pystray import Icon, MenuItem, Menu
from PIL import Image
import tkinter as tk
import threading

def exit_app(icon, item):
    """Exit the app from system tray."""
    icon.stop()
    root.quit()

def show_window(icon, item):
    """Restore the main window from system tray."""
    icon.stop()
    root.deiconify()

root = tk.Tk()
root.geometry("300x200")
root.title("Minimize to Tray") 

# Hide the window instead of closing it
def minimize_to_tray():
    root.withdraw()  # Hide the window
    threading.Thread(target=icon.run, daemon=True).start()  # Run tray icon in a separate thread

# Load icon 
image = Image.open("C:/Users/KAUSHIK/Documents/CODE/GUI/icon.png/logo.png")
  
# Create system tray menu
menu = Menu(
    MenuItem("Show App", show_window),
    MenuItem("Exit", exit_app))

# Create system tray icon
icon = Icon("test_icon", image, "My App", menu)

root.mainloop()
