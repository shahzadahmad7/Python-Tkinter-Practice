from tkinter import *
import tkinter.messagebox as tmsg

root= Tk()
root.title("Message Box Tutorial ")
root.geometry("400x250")
def hello():
   tmsg.showinfo("Question about Love", "Yes, you are lover.")
def name():
	a=tmsg.askquestion(" Name", "Will you tell me her name?")
	if a=='yes':
		tmsg.showwarning("Alert", "Thank you!, but don't tell it to others")
	else:
		tmsg.askokcancel("Thanks!", "No issue...")

B1 = Button(root, text = "Lover", command = hello)
B1.pack()


B2 = Button(root, text = "Name", command = name)
B2.pack()

root.mainloop()