from tkinter import *
root=Tk()
root.title("Frames & Button")
root.config(bg="#202020")
root.iconbitmap('1964.ico')
root.geometry('644x420')
# root.resizable(False, False)

def teacher():
    print("Welcome Teacher")
def fee():
    print("You must have to pay")

f2=Frame(root, bg="Grey", relief=SUNKEN, borderwidth=8)
f2.pack(side=TOP, fill='x')

lbl=Label(f2, text="Welcome", bg='grey', fg='white', font=("times new roman", 30, "bold"))
lbl.pack(pady=50)

f1=Frame(root, bg="Grey", borderwidth=8, relief=SUNKEN)
f1.pack(side=LEFT, fill='y')

btn1=Button(f1, text='Students', font=("times new roman", 20, "bold"))
# btn1.place(x=5, y=250)
btn1.pack(padx=5, pady=5) # need to check why is it neccessary

btn2=Button(f1, text='Teacher', font=("times new roman", 20, "bold"), borderwidth=4, command=teacher)
# btn2.place(x=5, y=100)
btn2.pack(padx=5, pady=5)

btn3=Button(f1, text='Fees', font=("times new roman", 20, "bold"), borderwidth=4, command=fee)
btn3.pack(padx=5, pady=5)


root.mainloop()