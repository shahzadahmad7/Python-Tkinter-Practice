from tkinter import *
root=Tk()
root.title("Frames & Button")
root.config(bg="#202020")
root.iconbitmap('1964.ico')
root.geometry('644x420')
root.resizable(False, False)

def getvalue():
    print(usernamevalue.get())
    print(passwordvalue.get())

# f1=Frame(bg="grey", borderwidth=5)
# f1.pack(side=TOP, fill='x' )

username=Label(root, text="Username: ", font=("times new roman", 20, 'bold'), bg="#202020", fg='white')
password=Label(root, text="Password: ", font=("times new roman", 20, 'bold'),bg="#202020", fg='white')
username.grid()
# password.grid()
password.grid(row=1)

usernamevalue=StringVar()
passwordvalue=StringVar()

userentry=Entry(root, textvariable=usernamevalue)
passentry=Entry(root, textvariable=passwordvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(root,text='Submit', command=getvalue, padx=5, pady=5).grid()



root.mainloop()