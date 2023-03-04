from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Scale/slider")
root.geometry("550x400")

def myfunc():
	Selection="Value: "+str(var.get())
	tmsg.showinfo("Range", Selection)
	label.config(text=Selection)
#Initialize variable
var=IntVar()
#By default from=0, to=100 Scale
slider1=Scale (root, orient=HORIZONTAL, variable=var)
#to set default value, we use set()
slider1.set(34)
slider1.pack()

Button(root, text="Enter your range", command=myfunc).pack()

label=Label(root)
label.pack()
root.mainloop()