#tkinter pdf of word is made and see that
import tkinter as tk

def display():#to display user info after taking its so its like enter command function
    name = name_entry.get()
    age = age_entry.get()
    result_label.config(text=f"Your Name:{name}")
    result_label1.config(text=f"Your Age:{age}")
def clear_field():#to clear the enter data user so its like clear command function
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    result_label.config(text="")
    result_label1.config(text="")

def exit_app():#to totaly close gui so its like it has exit command function here
    window.destroy()

def cond():
  try:
    age=int(age_entry.get())
    if age > 18:
        result_label.config(text="you are eligibe for this gui")
    else:
        result_label.config(text="you are not eligible for this gui")
  except ValueError:
    result_label1.config(text="Please enter a valid age")


window=tk.Tk() #creating a window
window.title("GUI") #it give title to the gui
window.geometry("800x300") #dimension of its box
window.configure(background="light blue") #adding background colour of gui

label=tk.Label(window,text="What's Your Name: ",font=("Bold",10),fg="white",bg="black").grid(column=4,row=5)#adding a text in gui
name_entry=tk.Entry(window,width=20)#making a box where user can enter name,width is giving length of box,Entry widget only allow width of the its box not height
name_entry.grid(column=10,row=5,columnspan=10)#giving size of the box
#grid is used to place them acc to grid of column,row,columncolumnspan etc
label1=tk.Label(window,text="What's Your Age: ",font=("Bold",10),fg="white",bg="black").grid(column=4,row=6,columnspan=4)
age_entry=tk.Entry(window,width=20)#makinga a box where user can enter age
age_entry.grid(column=10,row=6,columnspan=10)#give size of the box

tk.Button(window,text="Submit",font=("Bold",9), command=display).grid(column=6,row=10)#creating a button to submit the info of user,adding command func for that specific key
tk.Button(window,text="Clear",font=("Bold",9),command=clear_field).grid(column=7,row=10)#creating a button to claer the info of user if he done error
tk.Button(window,text="Exit",font=("Bold",9), command=exit_app).grid(column=8,row=10)#creating a button to close the gui
tk.Button(window,text="Check",font=("Bold",9), command=cond).grid(column=5,row=10)

result_label = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")#to display the use info,text is empty bcz its for before enter info diaplay
result_label.grid(column=4, row=8, columnspan=5)
result_label1 = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_label1.grid(column=4, row=9, columnspan=5)

window.mainloop()

##to get exact gui of my screen size
# import tkinter as tk

# root = tk.Tk()

# # Get screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Set the geometry to full screen size
# root.geometry(f"{screen_width}x{screen_height}")
# print(f"{screen_width}x{screen_height}")
# root.mainloop()