from tkinter import *

# To create a class, we will always make child class of Tk
class GUI(Tk):
	#In class, Self will be used in place of root
	def __init__(self):
		super().__init__()
		self.geometry("500x400")
		self.title("Classes & OOPs")
	
	def statusbar(self):
		self.statusvar=StringVar()
		self.statusvar.set("Ready")
#Status bar is a label with some attribute
		self.sbar=Label(textvariable=self.statusvar, relief=SUNKEN, anchor="w")
		self.sbar.pack(side=BOTTOM, fill="x")
	
	def upload (self):
		self.statusvar.set("Busy...")
		self.sbar.update()
	#Import time module to change status bar
		import time
		time.sleep(2)
		self.statusvar.set("Ready Now")
		#print("uploaded")
		
	def createButton(self, inputtext):
		Button(text=self.inputtext, command=self.upload).pack()
		
#Main window for class call
if __name__=='__main__':
	#in main, object will be used in place of root
	window=GUI()
	window.statusbar()
	window.createButton("Submit")
	window.upload()
	window.mainloop()