import tkinter as tk
from tkinter import messagebox
from tkinter import * #for scale use we need to import *

name=""
def display():
    result_n=tk.Label(root,text="")
    result_n.grid(row=20,column=10)

def showmessage():
    global name
    #ask,show is like a keyword which should before the info,okcancel... words
    messagebox.showinfo(f"Information", "Name entered already")#it shows the message if there is any problem,it only give one option of ok 
    messagebox.showwarning("Warns","before issue happens info is wrong input correctly")#only ok option it display warning to user id there any error occur while processing etc 
    messagebox.showerror("Eroor occur","error occured ")#only ok option it display the error if user did the erroe that programer has defined earlier
    messagebox.askokcancel("what you want ","would you like to proceed ")#gives two option ok or cancel 
    messagebox.askquestion("review","are you satisfied")# gives option yes,no,if programmer want to know i user satified or not,does not allow x which is cancel option of that box 
    messagebox.askretrycancel("something wrong","would you  like to try again ")#gives option retry,cancel if error occurs
    messagebox.askyesno("exit","would you like to exit or not")#it gives option yes no,eg would be while exit press we usually see yes or no u want to exit,does not allow x which is cancel option of that box 
    messagebox.askyesnocancel("file already existed","Its already saved so what would be next action")#it give 3 option yes,no,cancel for the queery
#xyz than , abc than xyz will act as title of that box and after , will be shown in box

root=tk.Tk()
root.title("Another basic")
root.geometry("500x400")
root.configure(bg="orange")

t1=tk.Frame(root)
t1.pack()
btn_info = tk.Button(root, text="Show Messages", command=showmessage)
btn_info.pack(pady=10)

tk.Entry(t1,width=30).grid(row=24,column=15)

Scale(root, from_=0, to=100, orient=HORIZONTAL).pack()#provides a slider for selecting a range of values.

root.mainloop()