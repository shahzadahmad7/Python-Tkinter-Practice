from tkinter import *
from PIL import Image, ImageTk
root=Tk()
#to change title from tk to MyProject
root.title("MyProject")
#to set icon along with project
root.iconbitmap('1964.ico')
# to set geometry(Width x height) for main GUI Screen
root.geometry("1080x680")
# to set minsize(Width, height) for main GUI Screen
root.minsize(250,150)
# to set maxsize(Width, height) for main GUI Screen
root.maxsize(1080,680)
#to add a png image, we also use label
# photo=PhotoImage(file="ghubara.png")
# to add other type of images like jpg, we have to use pillow library
a=Image.open("1.jpg")
photo=ImageTk.PhotoImage(a)

lbl=Label(root, image=photo)
lbl.pack()
root.mainloop()