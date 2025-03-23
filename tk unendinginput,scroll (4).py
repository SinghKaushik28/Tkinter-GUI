import tkinter as tk 
from tkinter import * #if u dont want to write tk.in Label,Frame,Text than import this line  
#line 2 is not compulsory in each gui program choose one way either keep it or dont else it will cause confusion 
root=tk.Tk()
root.title("Unending")
root.geometry("500x600")
frame1=Frame(root)#if u dont write number2 than it will be written like frame1=tk.Frame(root)
frame1.grid()

label1=Label(frame1,text="Hello")#if line 2 is not written than it would be written like label1=tk.Label(...)
label1.grid(row=5,column=20)

frame=Frame(root)
frame.grid()

#if line 2 not eritten than it would be writte like text=tk.Text(...) can also be written like this 
text=Text(frame,wrap=None, height=15, width=50)#Text is a widget in tkinter which allow to create a unending box for input ,in warpwe can use NONE<WORD<CHAR
text.pack(side=LEFT,fill=BOTH,expand=TRUE)#NONE will not break or move by default to next line its just keep adding in one line,WORD will break if it reach end of box and break from earlier space point
#warp CHAR will strictly follow  box geometry and it will break that word if left and size end andadd it in next line
#there is a specific meanin of left,right,top,bottom side
#Height and width is use to increase the size of the unending box,Text widget allow both height,width for to incraese the size of the box
# to check difference in side enable the bellow #
# text_right = Text(frame, wrap=NONE, height=5, width=40)
# text_right.pack(side=BOTTOM)
scrollbar=Scrollbar(frame,command=text.yview)#creates scroll bar widget within frame,command is connect scroll bar with text,telling what he have to do,.yview lets scroll in yaixs
scrollbar.pack(side=RIGHT,fill=Y,expand=TRUE)#side to tell where to show scrollbar,exapand is to let it scroll till the end else size will be fixed
text.config(yscrollcommand=scrollbar.set)#(config) Configures the Text widget to update the position of the scrollbar whenever the Text widget's content is scrolled.
#yscrollcommand=scrollbar.set Ensures that the scrollbar reflects the current vertical scroll position of the text widget.
#Without this, the scrollbar won't visually update as you scroll through the text.

for i in range(1,100):
  text.insert(END,f"This is a line number{i}\n")#inset function as it works(4,the string u want to insert at 4th index num)

root.mainloop()

