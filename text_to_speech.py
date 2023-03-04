from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
root.title("Text to Speech")
root.geometry("600x500")
root.config(bg="#404040")

top_frame= Frame(root, width=600, height=70, bg="pink")
top_frame.place(x=0, y=0)

lbl=Label(top_frame, text="Text to Speech", font="arial 16 bold")
lbl.place(x=100, y=30)

txt=Text(root, width=40, height=24, bg="grey")
txt.place(x=10, y=100)

lbl1=Label(root, text="Select Gender")
lbl.place(x=200, y=100)

root.mainloop()