from tkinter import *
from textblob import TextBlob


root=Tk()
root.title("Spell Checker")
root.geometry("550x400")

def correct_spelling():
    txt=entry.get()
    to_correct=TextBlob(txt)
    to_correct.correct()
    corrected=to_correct.correct()
    lbl=Label(root, text=corrected, font="arial 16")
    lbl.place(x=250, y=190)

lbl=Label(root, text="Spell Checker", font="arial 16 bold")
lbl.place(x=100, y=20)

entry= Entry(root, font="arial 16")
entry.place(x=150, y=80)
entry.focus()

btn=Button(root, text='Check', font="arial 16 bold", command=correct_spelling)
btn.place(x=170, y=130)

spelling=Label(root, text="Correct Spelling are: ", font="arial 16")
spelling.place(x=30, y=190)
root.mainloop()