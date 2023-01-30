from ast import Try
from tkinter import ttk
import tkinter as tk
from turtle import width
from turtle import window_height
from webbrowser import BackgroundBrowser

window=tk.Tk()
text_var=tk.StringVar()
input_user=tk.Label(window,width=43,text="0",height=2,background="#4682B4")
def operation(btn):
    current=input_user["text"]
    if current=="0":
        input_user["text"]=btn
    elif btn=="=":
        input_user["text"]=eval(current)
    elif btn=="c":
        input_user["text"]=""
    else:
        input_user["text"]+=btn
        
button1=ttk.Button(window,text="1",command=lambda:operation("1")) 
button2=ttk.Button(window,text="2",command=lambda:operation("2"))
button3=ttk.Button(window,text="3",command=lambda:operation("3"))
button4=ttk.Button(window,text="4",command=lambda:operation("4"))
button5=ttk.Button(window,text="5",command=lambda:operation("5"))
button6=ttk.Button(window,text="6",command=lambda:operation("6"))
button7=ttk.Button(window,text="7",command=lambda:operation("7"))
button8=ttk.Button(window,text="8",command=lambda:operation("8"))
button9=ttk.Button(window,text="9",command=lambda:operation("9"))
button10=ttk.Button(window,text=".",command=lambda:operation("."))
button11=ttk.Button(window,text="0",command=lambda:operation("0"))
button12=ttk.Button(window,text="+",command=lambda:operation("+"))
button13=ttk.Button(window,text="-",command=lambda:operation("-"))
button14=ttk.Button(window,text="*",command=lambda:operation("*"))
button15=ttk.Button(window,text="=",command=lambda:operation("="))
button16=ttk.Button(window,text="c",command=lambda:operation("c"))

input_user.grid(row=0,column=0,columnspan=4,)
button1.grid(row=1,column=0,)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button12.grid(row=1,column=3)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button13.grid(row=2,column=3)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button14.grid(row=3,column=3)
button10.grid(row=4,column=0)
button11.grid(row=4,column=1)
button16.grid(row=4,column=2)
button15.grid(row=4,column=3)



window.mainloop()