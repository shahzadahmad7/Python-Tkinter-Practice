from tkinter import *
root=Tk()
root.title("CheckButton")
root.config(bg="#202020")
root.iconbitmap('1964.ico')
root.geometry('644x420')
root.resizable(False, False)
#function of submit button command
def getvalue():
    print(namevalue.get())
    print(phonevalue.get())
 
    if gendervalue==1:
        print(gendervalue.set('Male'))
    if gendervalue==0:
        print(gendervalue.set('Female'))
    else:
        print("Error")
    print(emailvalue.get())
    print(schoolvalue.get())
    if referenceentry:
        print(referencevalue.get())
    else:
        print(0)

#lable for forms
name=Label(root, text="Name: ", font=("times new roman", 20, 'bold'), bg="#202020", fg='white')
phone=Label(root, text="Cell No.: ", font=("times new roman", 20, 'bold'), bg="#202020", fg='white')
gender=Label(root, text="gender: ", font=("times new roman", 20, 'bold'), bg="#202020", fg='white')
email=Label(root, text="email: ", font=("times new roman", 20, 'bold'), bg="#202020", fg='white')
school=Label(root, text="school: ", font=("times new roman", 20, 'bold'), bg="#202020", fg='white')
#packing of variables
name.grid(row=1,column=2)
phone.grid(row=2 ,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)
school.grid(row=5,column=2)
#assign value type of variable
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emailvalue=StringVar()
schoolvalue=StringVar()
referencevalue=IntVar()

#Entry form for value
nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
Radiobutton(root, text="Male", variable=gendervalue, value=1, bg="#202020", fg='white').grid(row=3, column=3)
Radiobutton(root, text="Female", variable=gendervalue, value=0, bg="#202020", fg='white').grid(row=3, column=4)
emailentry=Entry(root, textvariable=emailvalue)
schoolentry=Entry(root, textvariable=schoolvalue)
referenceentry=Checkbutton(root, text="Have any reference", variable=referencevalue, bg="#202020", fg='white')
#packing of entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=4, column=3)
schoolentry.grid(row=5, column=3)
referenceentry.grid(row=6, column=3)

Button(root,text='Submit', command=getvalue, padx=5, pady=5).grid(row=8, column=3)



root.mainloop()