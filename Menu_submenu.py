from tkinter import *
root=Tk()
root.title("My Project ")
root.geometry("600x400")

mainmenu=Menu(root)
m1=Menu(mainmenu)
m1.add_command(label="New")
m1.add_command(label="Open")
m1.add_command(label="Save")
m1.add_command(label="Save As")
m1.add_separator()
m1.add_command(label="Exit", command=quit)

mainmenu.add_cascade(label="File", menu=m1)

#Second Menu
m2=Menu(mainmenu)
m2.add_command(label="Undo")
m2.add_command(label="Redo")
m2.add_command(label="Save")
m2.add_command(label="Save As")

mainmenu.add_cascade(label="Edit", menu=m2)

#Third Menu
m3=Menu(mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)

root.config(menu=mainmenu)
root.mainloop()