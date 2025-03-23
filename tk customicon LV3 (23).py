#ensures your app has a proper icon in the taskbar instead of the default Tkinter icon.
#for windows
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("my_custom_app")

import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
root.title("App Icon in Taskbar,Minimize to Tray")
root.iconbitmap("C:/Users/KAUSHIK/Documents/CODE/GUI/Icon.ico")

tk.Label(root, text="Look at the Taskbar!", font=("Arial", 12)).pack(pady=20)
root.mainloop()

#for linux
# import tkinter as tk     b

# root = tk.Tk()
# root.geometry("300x200")
# root.title("Linux Custom Icon")

# # Use a PNG file (Linux)
# icon = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/CODE/GUI/icon.png/logo.png")
# root.iconphoto(False, icon)

# tk.Label(root, text="Check the app icon!", font=("Arial", 12)).pack(pady=20)
# root.mainloop()

