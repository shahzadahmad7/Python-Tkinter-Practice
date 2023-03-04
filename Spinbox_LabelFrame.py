from tkinter import *

root= Tk()
root.title("Spinbox &  LabelFrame Tutorial ")
root.geometry("600x450")

sb=Spinbox(root, from_=0, to=10)
sb.pack()

labelframe = LabelFrame(root, text="This is a LabelFrame", font="arial 8 bold")
labelframe.pack()

 
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

root.mainloop()