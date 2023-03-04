import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

notebook=ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1=ttk.Frame(notebook, width=400, height=280)
frame1.pack(fill='both', expand=True)

frame2=ttk.Frame(notebook, width=400, height=280)
frame2.pack(fill='both')

notebook.add(frame1, text="File")
notebook.add(frame2, text="Edit")


root.mainloop()