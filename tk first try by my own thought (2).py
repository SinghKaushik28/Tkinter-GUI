#taking just info and displaying but putting button else where and adding more
#function to one button check

import tkinter as tk

def display():#to display user info after taking its so its like enter command function
    name = name_entry.get()
    age = age_entry.get()
    result_label.config(text=f"Your Name:{name}")
    result_label1.config(text=f"Your Age:{age}")

    tk.Button(window,text="Check",font=("Bold",9), command=cond).grid(column=5,row=10)
    tk.Button(window,text="Clear",font=("Bold",9),command=clear_field).grid(column=7,row=10)
def clear_field():#to clear the enter data user so its like clear command function
    name_entry.delete(0, tk.END)#tk.end delete the data from box
    age_entry.delete(0, tk.END)
    result_label.config(text="")
    result_label1.config(text="")

def exit_app():#to totaly close gui so its like it has exit command function here
    window.destroy()

def cond():
  result_label.config(text="")
  result_label1.config(text="")
  try:
    age=int(age_entry.get())
    if age > 18:
        result_label.config(text="You are Eligibe for this GUI")
    else:
        result_label.config(text="You are not Eligible for this GUI")
  except ValueError:
    result_label1.config(text="Please enter a valid age")

window=tk.Tk() #creating a window
window.title("GUI") #it give title to the gui
window.geometry("800x300") #dimension of its box
window.configure(background="light blue") #adding background colour of gui

label=tk.Label(window,text="What's Your Name: ",font=("Bold",10),fg="white",bg="black").grid(column=4,row=5)#adding a text in gui
name_entry=tk.Entry(window,width=20)#making a box where user can enter name
name_entry.grid(column=10,row=5,columnspan=10)#giving size of the box

label1=tk.Label(window,text="What's Your Age: ",font=("Bold",10),fg="white",bg="black").grid(column=4,row=6,columnspan=4)
age_entry=tk.Entry(window,width=20)#makinga a box where user can enter age
age_entry.grid(column=10,row=6,columnspan=10)#give size of the box

tk.Button(window,text="Submit",font=("Bold",9), command=display).grid(column=6,row=10)#creating a button to submit the info of user,adding command func for that specific key
tk.Button(window,text="Exit",font=("Bold",9), command=exit_app).grid(column=8,row=10)#creating a button to close the gui


result_label = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")#to display the use info,text is empty bcz its for before enter info diaplay
result_label.grid(column=4, row=8, columnspan=5)
result_label1 = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_label1.grid(column=4, row=9, columnspan=5)
window.mainloop()