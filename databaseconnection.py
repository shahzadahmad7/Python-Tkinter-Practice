from tkinter import *
import pymysql
import tkinter.messagebox as tmsg

# connection=pymysql.Connect(host='localhost', user='root', password='', db='practice')
# mycursor= connection.cursor()
# mycursor.execute("INSERT INTO `employees`(`id`, `name`, `fatherName`, `address`) VALUES (1,'Shahzad','Riaz','MBDin')")
# connection.commit()
# connection.close()

# Create the main window
root = Tk()
root.title("Database Connection")
root.geometry("600x400")
#Main MYSQL function for Insert, Delete, Update
def mainSql(query, data):
    connection=pymysql.Connect(host='localhost', user='root', password='', db='practice')
    mycursor= connection.cursor()
    n=mycursor.execute(query, data)
    connection.commit()
    connection.close()
    return n
#Function Definition
def insert():
    try:
        empId=entry1.get()
        name=entry2.get()
        fatherName=entry3.get()
        address=entry4.get()
        query="INSERT INTO `employees`(`id`, `name`, `fatherName`, `address`) VALUES (%s, %s, %s, %s)"
        n=mainSql(query, (empId, name, fatherName, address))
        if n==1:
            tmsg.showwarning("Message", "Data has been inserted successfully...")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

def Modify():
    try:
        empId=entry1.get()
        name=entry2.get()
        fatherName=entry3.get()
        address=entry4.get()
        query="UPDATE `employees` SET `name`=%s,`fatherName`=%s,`address`=%s WHERE `id`=%s"
        n=mainSql(query, ( name, fatherName, address, empId))
        if n==1:
            tmsg.showwarning("Message", "Data has been updated successfully...")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

def Delete():
    try:
        empId=entry1.get()
        query="DELETE FROM `employees` WHERE `id`=%s"
        n=mainSql(query, (empId))
        if n==1:
            tmsg.showwarning("Message", "Data has been deleted successfully...")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

def Select():
    pass
    #Need to check code
    # try:
    #     empId=entry1.get()
    #     query="SELECT `name`, `fatherName`, `address` FROM `employees` WHERE id=%s", (empId)
    #     mainSql(query, (empId))
    # except Exception as e:
    #     print(f"Error: {e}")

#Main GUI
lb1=Label(root, text="Enter Employee ID")
lb1.place(x=100, y=50)
empId=IntVar()
entry1=Entry(root, font=("Arial", 14))
entry1.place(x=300, y=50)

lb2=Label(root, text="Enter Employee Name")
lb2.place(x=100, y=100)
name=StringVar()
entry2=Entry(root, font=("Arial", 14), textvariable=name)
entry2.place(x=300, y=100)

lb3=Label(root, text="Enter Father Name")
lb3.place(x=100, y=150)
fatherName=StringVar()
entry3=Entry(root, font=("Arial", 14))
entry3.place(x=300, y=150)

lb4=Label(root, text="Enter Employee Address")
lb4.place(x=100, y=200)
Address=StringVar()
entry4=Entry(root, font=("Arial", 14))
entry4.place(x=300, y=200)

btn1=Button(root, text="Insert", bg="Grey", bd=1, fg="White", font=("Arial", 14), padx=10, pady=10, command=insert)
btn1.place(x=100,y=250)

btn2=Button(root, text="Update", bg="Grey", bd=1, fg="White", font=("Arial", 14), padx=10, pady=10, command=Modify)
btn2.place(x=200,y=250)

btn3=Button(root, text="Delete", bg="Grey", bd=1, fg="White", font=("Arial", 14), padx=10, pady=10, command=Delete)
btn3.place(x=300,y=250)

btn4=Button(root, text="Select", bg="Grey", bd=1, fg="White", font=("Arial", 14), padx=10, pady=10, command=Select)
btn4.place(x=400,y=250)

txtBox=Text(root, width=60, height=10)
txtBox.place(x=100, y=320)


root.mainloop()