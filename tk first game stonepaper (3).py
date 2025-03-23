import tkinter as tk #imported tkinter library so that we can create a gui
import random as rd #imported random library so that computer can choose randomly
from tkinter import ttk

point=0#assign the initial value to poins of user and cp for comp point
cp=0

def display():#function to user enter name,age
 name = entry.get()
 age = entry1.get()
 result_n.config(text=f"Name:{name}")

def clear(): #function to clear the name,age entry box if user made mistake
 entry.delete(0, tk.END)
 entry1.delete(0, tk.END)
 result_n1.config(text="")
 clear_eligible()

def cond():#function to check user age
    try:
     age=int(entry1.get())
     if var.get() == 1:
       if age > 18:
        b1.config(state="normal")
        result_n1.config(text="Eligible",font=("bold",14))
        result_n1.place(x=300,y=200)
        
       else:
        result_n1.config(text="Not Eligible",font=("bold",14))
        
     else:
        
        result_n1.config(text="Please accept the terms",font=("bold",14))
    except ValueError:
  
     result_n1.config(text="Please enter a valid age",font=("bold",14))

def clearall():#function to again empty the gui for further use or adding something
    b2.place_forget()
    result_n1.place_forget()
    entry.place_forget()
    entry1.place_forget()
    c.place_forget()
    l1.place_forget()
    n.place_forget()
    a.place_forget()
    b3.place_forget()
    l2.place_forget()
    b1.place_forget()
 
def clear_eligible():#to clear the text of n,n1 if user press clear button
    result_n1.place_forget()
    result_n.place_forget()

def combined():#combine function to display name in gui,check age condition
    display()
    cond()

def Game():#function to give button for the play
   global st,st1,st2#global so that later in sone other function as well this st,st1,st2 can be used
   st=tk.Button(window,text="Stone",font=("Bold",12),bg="orange",command=lambda: gamecond("Stone"))
   st.place(x=300,y=300)
   st1=tk.Button(window,text="Paper",font=("Bold",12),bg="orange",command=lambda: gamecond("Paper"))
   st1.place(x=350,y=300)
   st2=tk.Button(window,text="Scissor",font=("Bold",12),bg="orange",command=lambda: gamecond("Scissor"))
   st2.place(x=400,y=300)
   
def gamecond(user_choice):
    global point,cp #to use point,cp first used global key else it restrict the use
    computer_choice=rd.choice(["Stone","Paper","Scissor"])#giving choice to comp to choose,using rd to let select randomly
    result_compchoice.config(text=f"Computer Choice: {computer_choice}")
    if (user_choice == "Stone" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Stone") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        point+=1 #has condition where user wins
        result_a1.config(text=f"You Choosed: {user_choice}")
        result_p.config(text=f"Your Points: {point}")
        result_p.place(x=200,y=80)
        result_n1.config(text="You Won this Round",font=("Bold"))
        result_n1.place(x=300,y=180)
    elif (user_choice == "Scissor" and computer_choice == "Stone") or \
         (user_choice == "Stone" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Scissor"):
        cp+=1 #this elif condtion where computer wins
        result_a1.config(text=f"You Choosed: {user_choice}")
        result_p1.config(text=f"Computer Points: {cp}")
        result_p1.place(x=400,y=80)
        result_n1.config(text="Computer Won this Round",font=("Bold"))
        result_n1.place(x=300,y=180)
    else:#for tie
        result_p1.config(text=f"Computer Points: {cp}")
        result_n1.config(text= f"This Round is a Tie",font=("Bold"))
        result_n1.place(x=300,y=180)
        result_a1.config(text=f"You Choosed: {user_choice}")
    win()#to end the game when 5 point reached

def gamecomb():#to combine different function in one function and place that combine function in one key
    Game()#here combine func is placed is  play button which lets displacy game buttons and clear previous text
    clearall()#cleared everything using this function

def win():#function to check who wins user or comp
   point,cp
   if point >= 5:
        result_n2.config(text=f"Congratulations You Won The Match.  Your Points: {point} | Computer Points: {cp}", font=("bold", 14))
        result_n2.place(x=300,y=220)#to show result in n2 area
        disable_game()
   elif cp >=5:
        result_n2.config(text=f"Computer Won The Match,Try Again. Your Points: {point} | Computer Points: {cp}", font=("bold", 14))
        result_n2.place(x=300,y=220)
        disable_game()

def disable_game():#this function to disable the stone,paper... button when user or comp hit 5 points
    st.config(state="disabled")#using config to change the st value or to change what earlier it was doing
    st1.config(state="disabled")
    st2.config(state="disabled")

def exit_app():#defined the function to exit and totally close the gui
    window.destroy()#its used to close the gui when the buttton releated to it is pressed

window=tk.Tk()
window.title("Kaush Game")#given the gui a title
window.geometry("1000x400")#used to create the gui box
window.configure(bg="light blue")#used to give colour to gui

style = ttk.Style()
style.theme_use("classic") 

t1=tk.Frame(window)#its used to adjust the frame of gui
t1.pack()#it place according to blocks
l1=tk.Label(window,text="Hello",font=("Bold",14),bg="light blue",fg="black")#its used to showcase the label the gui
l1.place(x=400,y=10)#used place to tell the comp where to put taht label text in the gui using x,y axis
l2=tk.Label(window,text="Check Eligibility First.",font=("Bold",10),bg="light blue",fg="black")#given the instruction to user using label which will show the word in gui
l2.place(x=100,y=130)#while using place u need to give cordinate where to pace using x,y axis
n=tk.Label(window,text="Name:",font=("Bold",12),padx=8,pady=2)#used label to instruct the user that here u need to enter name
n.place(x=100,y=70)#font is used to give the size,adjust the font accordingly,for bolding the text
entry=tk.Entry(window,width=20)#using entry made a empty box where user can enter name
entry.place(x=210,y=70)
a=tk.Label(window,text="Age:",font=("Bold",12),padx=8,pady=2)#used label to instruct the user that here u need to enter age
a.place(x=100,y=100)
entry1=tk.Entry(window,width=20)#using entry made a empty box where user can enter age
entry1.place(x=210,y=100)

#to let user accept the trems used checkbutton and if var=1 than allow to play
var =tk.IntVar()
c=tk.Checkbutton(window, text="Accept Terms", variable=var)
c.place(x=100,y=210)

result_n = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_n.place(x=100,y=5)#to showcase the Name of the user
result_n1 = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_n1.place(x=300,y=180)#to showcase eligibility ans,won and loss
result_n2 = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_n2.place(x=300,y=220)#to showcase final result wheter he won the match or not
result_p = tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_p.place(x=200,y=80)#to showcase the user points
result_compchoice= tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_compchoice.place(x=100,y=100)#to sowcase the computer choice in that round
result_p1= tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_p1.place(x=400,y=80)#to showcase the computer points
result_a1= tk.Label(window, text="", font=("Bold", 12), bg="light blue", fg="black")
result_a1.place(x=100,y=250)#to showcase what user choosed in that round

#adding buttons play,clear,check,exitgame as a all time button but using disable when not needed
b1=tk.Button(window,text="Play",command=gamecomb,font=("bold",12),bg="white",fg="black")
b1.place(x=380,y=250)#placing the button using place,giving keys command or function using command word
b1.config(state="disabled")#disabled the play button until user check the eligiblity
b2=tk.Button(window,text="clear",command=clear,font=("bold",10),bg="white",fg="black")
b2.place(x=270,y=250)
b3=tk.Button(window,text="Check",font=("bold",10),command=combined,bg="white",fg="black")
b3.place(x=220,y=250)
b4=tk.Button(window,text="Exit Game",font=("bold",10),command=exit_app,bg="white",fg="black")
b4.place(x=300,y=350)

window.mainloop()