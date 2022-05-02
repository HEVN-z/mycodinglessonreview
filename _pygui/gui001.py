from tkinter import *
from turtle import left

root = Tk()
root.title("GUI 001")
root.resizable(width=False, height=False)

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="I am HEVNz")
myLabel3 = Label(root, text="           ")
myLabel1.grid(row=0, column=0,pady=10, padx=10)
myLabel2.grid(row=1, column=2,pady=10, padx=10)
myLabel3.grid(row=1, column=1,pady=10, padx=10)

root.mainloop()