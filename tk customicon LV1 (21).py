# import tkinter as tk

# root=tk.Tk()
# root.title("Icon")
# root.geometry("300x200")

# root.iconbitmap("C:/Users/KAUSHIK/OneDrive/Documents/CODE/GUI/icon.ico")#add icon same as windows which is a file one
# root.wm_iconname("MyApp")

# root.mainloop()

import tkinter as tk

root=tk.Tk()
root.title("Icon")
root.geometry("300x200")

icon=tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/CODE/GUI/Icon.png/one.png")#add icon but photo of your choice
root.iconphoto(True, icon)
root.wm_iconname("MyApp")

root.mainloop()

