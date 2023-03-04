from tkinter import *
root=Tk()
root.title("Calculator Devloped by Shahzad Ahmad")
#GUI logic
# to set geometry(Width x height) for main GUI Screen
root.geometry("570x600+60+60")
root.resizable(False, False)
root.config(bg="#202020")

equation=' '
def clear():
    global equation
    equation=""
    lbl.config(text=equation)

def show(value):
    global equation
    equation+=value
    lbl.config(text=equation)

def calculate():
    global equation
    result=''
    if equation != '':
        try:
            result=eval(equation)
        except:
            result='error'
            equation=''
    lbl.config(text=result)

lbl=Label(root, text=' ', width=25, height=2, font=("Arial", 30), bg="#E0E0E0")
lbl.pack()
Button(root, text='C', font=("Arial", 30, "bold"), bd=1, bg="#0080ff", fg="#fff", width=5, height=1, command=lambda: clear()).place(x=10, y=110)
Button(root, text='/', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('/')).place(x=150, y=110)
Button(root, text='%', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('%')).place(x=290, y=110)
Button(root, text='*', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('*')).place(x=430, y=110)

Button(root, text='9', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('9')).place(x=10, y=210)
Button(root, text='8', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('8')).place(x=150, y=210)
Button(root, text='7', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('7')).place(x=290, y=210)
Button(root, text='-', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('-')).place(x=430, y=210)

Button(root, text='6', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('6')).place(x=10, y=310)
Button(root, text='5', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('5')).place(x=150, y=310)
Button(root, text='4', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('4')).place(x=290, y=310)
Button(root, text='+', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('+')).place(x=430, y=310)

Button(root, text='3', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('3')).place(x=10, y=410)
Button(root, text='2', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('2')).place(x=150, y=410)
Button(root, text='1', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('1')).place(x=290, y=410)

Button(root, text='0', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=11, height=1, command=lambda: show('0')).place(x=10, y=510)
Button(root, text='.', font=("Arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", width=5, height=1, command=lambda: show('.')).place(x=290, y=510)
Button(root, text='=', font=("Arial", 30, "bold"), bd=1, bg="#990000", fg="#fff", width=5, height=3, command=lambda: calculate()).place(x=430, y=410)

root.mainloop()