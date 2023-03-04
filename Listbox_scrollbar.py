from tkinter import *
import tkinter.messagebox as tmsg

root= Tk()
root.title("Radiobutton Tutorial ")
root.geometry("600x450")

Label(root, text="Select your grade").pack()
#To set scrollbar along with Listbox
scrollbar = Scrollbar()
scrollbar.pack(side=RIGHT, fill = Y )
#Default width of Listbox is 20
#set yscrollcommand=scrollbar for attach
lbx=Listbox(root, width=10, yscrollcommand=scrollbar.set)
lbx.pack()
lbx.insert(END, "First")
lbx.insert(END, "Second")
lbx.insert(END, "Third")
for i in range(4,13):
	lbx.insert(END, i)
	i+=1
#to activate scrollbar with list
scrollbar.config(command=lbx.yview)
lbx.config(yscrollcommand=scrollbar.set)

def delete():
	lbx.delete(ANCHOR)
btn=Button(root, text="Delete", bg='#404040', fg='white', bd=2, command=delete)
btn.pack(padx=10, pady=10)
root.mainloop()