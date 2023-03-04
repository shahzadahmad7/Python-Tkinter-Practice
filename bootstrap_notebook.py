import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#root=Tk()
root=ttk.Window(themename='vapor')
#solar, vapor, cosmo, superhero, flatly, minty, cyborg, darkly
root.geometry('600x400')

notebook=ttk.Notebook(root, bootstyle="danger")
# bootstyle="info-outline"
# bootstyle="info outline"
# bootstyle=("info", "outline")
# bootstyle=(INFO, OUTLINE)
notebook.pack(padx=10, pady=5)

frame1=ttk.Frame(notebook, width=550, height=300)
frame1.pack(padx=10, fill='both')

frame2=ttk.Frame(notebook, width=550, height=300)
frame2.pack(padx=10, fill='both')

frame3=ttk.Frame(notebook, width=550, height=300)
frame3.pack(padx=10, fill='both')

notebook.add(frame1, text='File')
notebook.add(frame2, text='Info')
notebook.add(frame3, text='Help')

btn=ttk.Button(root, text='Submit', bootstyle='danger outline', takefocus=True)
btn.pack(side=BOTTOM, padx=10,pady=10)


root.mainloop()