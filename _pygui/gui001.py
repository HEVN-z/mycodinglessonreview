from tkinter import *
from turtle import left

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="I am HEVNz")
myLabel3 = Label(root, text="           ")
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=1, column=1)

root.mainloop()