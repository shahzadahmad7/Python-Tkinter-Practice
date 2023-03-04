from tkinter import *
import tkinter.messagebox as tmsg

root= Tk()
root.title("Radiobutton Tutorial ")
root.geometry("600x450")

def gender():
	tmsg.showinfo("Gender", f"The gender of {a.get()} is {var.get()}")
var=StringVar()
var.set(" ")

Label(root, text="Name of your friend:", font="arial 10 bold").pack()
a=Entry (root)
a.pack()
Label(root, text="Tell us the gender of your friend...", font="arial 10 bold").pack()

Radiobutton(root, text="Male", variable=var, value="Male").pack()

Radiobutton(root, text="Female", variable=var, value="Female").pack()

Radiobutton(root, text="Others", variable=var, value="Others").pack()

Button (root, text="Are you sure?", bg="#404040", fg="white", bd=6,command=gender).pack()
root.mainloop()