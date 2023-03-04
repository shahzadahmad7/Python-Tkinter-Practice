from tkinter import *
root=Tk()

#GUI logic
# to set geometry(Width x height) for main GUI Screen
root.geometry("644x320")
# to set minsize(Width, height) for main GUI Screen
root.minsize(250,150)
# to set maxsize(Width, height) for main GUI Screen
root.maxsize(644,450)
#Show text on main screen, we will introduce new label as lbl
#if variable.pack() is not used, no output will be shown pack() can be used at the end or along the label
lbl=Label(root, text="Welcome, to the world of python\n").pack()
lbl1=Label(text="Are you here to learn and practice", relief=RAISED, bg="RED", bd=15).pack()
lbl2=Label(text="Are you here to learn and practice", relief=GROOVE, font=("Arial", 30), fg="BLUE", bg="green").pack(side=BOTTOM)
lbl3=Label(text="Are you here to learn and practice", relief=SUNKEN, fg="BLUE", bg="Yellow", bd=15).pack()
lbl4=Label(text="Are you here to learn and practice", relief=RIDGE, fg="BLUE", bg="Pink", bd=15).pack(anchor=W)
lbl5=Label(text="Are you here to learn and practice Python", relief=RAISED, bg="RED", bd=1, anchor='se').pack(anchor=NE)
btn=Button(root, text="Submit", bg="Grey", bd=1, fg="White", font=("Arial", 20, "bold"), padx=20, pady=10).pack(anchor=SE)
# lbl.pack()
# lbl1.pack()
# lbl2.pack()
# lbl3.pack()
# lbl4.pack()
# lbl5.pack()
root.mainloop()