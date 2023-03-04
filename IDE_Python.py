from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root=Tk()
root.geometry("800x600+80+80")
root.title("Python IDE")

def open():
	global file
	file = askopenfilename(defaultextension=".py", filetypes=[("All Files", "*.*"), ("Python File", "*.py")])
	if file == "":
		file = None
	else:
		root.title(os.path.basename(file) + " - Python")
		lbx1.delete(1.0, END)
		f = open(file, "r")
		TextArea.insert(1.0, f.read())
		f.close()

def save():
	global file
	if file == None:
		file = asksaveasfilename(initialfile ="Untitled.py", defaultextension=".py", filetypes=[("All Files", "*.*"), ("Python File", "*.py")])
		if file =="":
			file = None
		else:
			#Save as a new file
			f = open(file, "w")
			f.write(lbx1.get(1.0, END))
			f.close()
			
			root.title(os.path.basename(file) + " - Python")
			print("File Saved")
	else:
		# Save the file
		f = open(file, "w")
		f.write(TextArea.get(1.0, END))
		f.close()
	
def run():
	global file
	if file=="":
		messagebox.showerror("Python IDE", "Save your code")
	return 
	command=f'python{file}'
	process=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	code_output.insert(1.0, output)
	code_output.insert(1.0, error)

#GUI
lbx1=Text(root, width=40, height=35)
lbx1.place(x=120, y=15)

lbx2=Text(root, width=40, height=35, bg="#404040", fg="lightgreen")
lbx2.place(x=460, y=15)

file='';
btn1=Button(root, text="Open", bd=2, bg="Green", fg="white", padx=15, pady=5, font=("arial", 14, "bold"), activebackground="yellow", command=open)
btn1.place(x=10, y=40)

btn2=Button(root, text="Save", bd=2, bg="lightblue", fg="#202020", padx=15, font=("arial", 14, "bold"),pady=5,activebackgroun="purple", command=save)
btn2.place(x=10, y=110)

btn3=Button(root, text="Run", bd=2, bg="red", fg="#202020", padx=20, pady=5, font=("arial", 14, "bold"),activebackground="pink", command=run)
btn3.place(x=10, y=185)

root.mainloop()