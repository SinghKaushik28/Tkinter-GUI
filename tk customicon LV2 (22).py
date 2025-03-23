import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Button with Icon")

icon = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/CODE/GUI/Icon.png/ace.png")

icon1 = tk.PhotoImage(file="C:/Users/KAUSHIK/Documents/CODE/GUI/Icon.png/one.png",height=16,width=16)

# Label with an icon
label = tk.Label(root, text="Hello!", image=icon1, compound="left", font=("Arial", 14))
label.pack(pady=20)

# # Button with an icon
button = tk.Button(root, image=icon, compound="top",height=24,width=28)  # Use "top", "right", "bottom" if needed
button.pack(pady=20)

root.icon = icon
root.icon1 = icon1

root.mainloop()