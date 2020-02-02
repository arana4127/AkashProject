# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:53:59 2018

@author: Owner
"""

import tkinter
import sqlite3

from tkinter import*
root=Tk()
root.title("PYTHON PROJECT")
x=StringVar()
def db():
    N=x.get()
    
    conn=sqlite3.connect('Feedback.db')
    #conn.execute("Create table M(x text)")
    conn.execute("Insert into M(x) values(?)",(N))
    z=conn.execute("Select * from M")
    for i in z:
        print(i)





button=Button(root,text="w",bg="black",width=3,fg="yellow")
def a():
    print("WET")
    button.configure(bg="red")
    button2.configure(bg="red")
    button3.configure(bg="red")
button.config(command=a)
button.grid(row=0, column=0)

button2=Button(root,text="e",bg="black",width=3,fg="yellow")


button2.grid(row=1, column=0)


button3=Button(root,text="t",bg="black",width=3,fg="yellow")


button3.grid(row=2, column=0)



button4=Button(root,text="w",bg="black",width=3,fg="yellow")
def d():
    print("WHALE ")
    button4.configure(bg="blue")
    button9.configure(bg="blue")
    button14.configure(bg="blue")
    button19.configure(bg="blue")
    button24.configure(bg="blue")
button4.config(command=d)
button4.grid(row=3, column=0)


button5=Button(root,text="b",bg="black",width=3,fg="yellow")
def e():
    print("BLUE")
    button5.configure(bg="yellow")
    button10.configure(bg="yellow")
    button15.configure(bg="yellow")
    button20.configure(bg="yellow")
button5.config(command=e)
button5.grid(row=4, column=0)



button6=Button(root,text="f",bg="black",width=3,fg="yellow")
def f():
    print("FISH ")
    button6.configure(bg="purple")
    button7.configure(bg="purple")
    button8.configure(bg="purple")
    button9.configure(bg="purple")
button6.config(command=f)
button6.grid(row=0, column=1)


button7=Button(root,text="i",bg="black",width=3,fg="yellow")


button7.grid(row=1, column=1)



button8=Button(root,text="s",bg="black",width=3,fg="yellow")
def h():
    print("SEA ")
    button8.configure(bg="green")
    button13.configure(bg="green")
    button18.configure(bg="green")
button8.config(command=h)
button8.grid(row=2, column=1)



button9=Button(root,text="h",bg="black",width=3,fg="yellow")
button9.grid(row=3, column=1)



button10=Button(root,text="l",bg="black",width=3,fg="yellow")

button10.grid(row=4, column=1)



button11=Button(root,text="b",bg="black",width=3,fg="yellow")

button11.grid(row=0, column=2)



button12=Button(root,text="r",bg="black",width=3,fg="yellow")

button12.grid(row=1, column=2)


button13=Button(root,text="e",bg="black",width=3,fg="yellow")

button13.grid(row=2, column=2)


button14=Button(root,text="a",bg="black",width=3,fg="yellow")

button14.grid(row=3, column=2)



button15=Button(root,text="u",bg="black",width=3,fg="yellow")

button15.grid(row=4, column=2)


button16=Button(root,text="s",bg="black",width=3,fg="yellow")
def p():
    print("SEAL ")
    button16.configure(bg="brown")
    button17.configure(bg="brown")
    button18.configure(bg="brown")
    button19.configure(bg="brown")
button16.config(command=p)
button16.grid(row=0, column=3)


button17=Button(root,text="e",bg="black",width=3,fg="yellow")

button17.grid(row=1, column=3)


button18=Button(root,text="a",bg="black",width=3,fg="yellow")

button18.grid(row=2, column=3)


button19=Button(root,text="l",bg="black",width=3,fg="yellow")

button19.grid(row=3, column=3)


button20=Button(root,text="e",bg="black",width=3,fg="yellow")

button20.grid(row=4, column=3)


button21=Button(root,text="w",bg="black",width=3,fg="yellow")
def u():
    print("WATER ")
    button21.configure(bg="orange")
    button22.configure(bg="orange")
    button23.configure(bg="orange")
    button24.configure(bg="orange")
    button25.configure(bg="orange")
button21.config(command=u)
button21.grid(row=0, column=4)


button22=Button(root,text="a",bg="black",width=3,fg="yellow")

button22.grid(row=1, column=4)


button23=Button(root,text="t",bg="black",width=3,fg="yellow")

button23.grid(row=2, column=4)



button24=Button(root,text="e",bg="black",width=3,fg="yellow")

button24.grid(row=3, column=4)


button25=Button(root,text="r",bg="black",width=3,fg="yellow")

button25.grid(row=4, column=4)



button26=Button(root,text='Reset',width=7)
def z():
    print("Puzzle has been reset")
    button.configure(bg="black")
    button2.configure(bg="black")
    button3.configure(bg="black")
    button4.configure(bg="black")
    button5.configure(bg="black")
    button6.configure(bg="black")
    button7.configure(bg="black")
    button8.configure(bg="black")
    button9.configure(bg="black")
    button10.configure(bg="black")
    button11.configure(bg="black")
    button12.configure(bg="black")
    button13.configure(bg="black")
    button14.configure(bg="black")
    button15.configure(bg="black")
    button16.configure(bg="black")
    button17.configure(bg="black")
    button18.configure(bg="black")
    button19.configure(bg="black")
    button20.configure(bg="black")
    button21.configure(bg="black")
    button22.configure(bg="black")
    button23.configure(bg="black")
    button24.configure(bg="black")
    button25.configure(bg="black")
button26.config(command=z)
button26.grid(row=7, columnspan=2)

button27=Button(root,text="Close",bg="red",width=7)
button27.config(command=root.destroy)
button27.grid(row=7,column=3, columnspan=2)


feedbacklabel=Label(root,text='Rate',width=3)
feedbacklabel.grid(row=9,column=0,sticky=E)
feedbacklabe=Label(root,text='Us',width=3)
feedbacklabe.grid(row=9,column=1,sticky=W)
feedbackentry=Entry(root,textvar=x,fg="red",width=3).grid(row=9,column=2)
b1=Button(root,text=":)",bg="green",fg="yellow",command=db,width=3)
b1.grid(row=10,column=2)
root.mainloop()   

