from tkinter import *

root = Tk()
root.title("My Project")
root.geometry("600x400")
#Canvas Widget
canv_widget=Canvas(root, height=300, width=500, bg="red")
canv_widget.pack()
#Creation of shapes in canvas
canv_widget.create_line(0,0,300,400)
canv_widget.create_arc(10,50,240,210, fill="blue")
canv_widget.create_rectangle(10,50,240,210)
canv_widget.create_oval(20,100,200,210)
canv_widget.create_polygon(200,150,200,200,300,250,350,300, 500,400)
#Run Forever
root.mainloop()
