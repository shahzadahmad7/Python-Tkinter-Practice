from tkinter import *

root= Tk()
root.title("Statusbar Tutorial ")
root.geometry("600x450")

def upload():
	statusvar.set("Busy...")
	sbar.update()
	#Import time module to change status bar
	import time
	time.sleep(2)
	statusvar.set("Ready Now")
#Set status variable as StringVar() and set initial value	
statusvar=StringVar()
statusvar.set("Ready")
#Status bar is a label with some attribute
sbar=Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill="x")
Button(root, text="Update ", command=upload).pack()
root.mainloop()