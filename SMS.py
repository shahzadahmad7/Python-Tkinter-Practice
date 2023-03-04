import tkinter as tk
import mysql.connector

# Define the connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="",
  password="root",
  database="myschool"
)

# Define a cursor to execute the SQL commands
mycursor = mydb.cursor()

# Define the main window for the school management system
root = tk.Tk()
root.title("School Management System")

# Define a function to show the student information
def show_student():
    # Clear the text widget
    text.delete('1.0', tk.END)

    # Get the student ID from the entry widget
    student_id = entry_student_id.get()

    # Execute the SQL command to retrieve the student information
    mycursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = mycursor.fetchone()

    # Check if the student exists
    if student is not None:
        # Display the student information
        text.insert(tk.END, "Name: " + student[1] + "\n")
        text.insert(tk.END, "Age: " + str(student[2]) + "\n")
        text.insert(tk.END, "Class: " + student[3] + "\n")
        text.insert(tk.END, "Fees: " + str(student[4]) + "\n")
    else:
        # Display an error message if the student does not exist
        text.insert(tk.END, "Student not found")

# Define a function to update the student fees
def update_fees():
    # Get the student ID and the new fees from the entry widgets
    student_id = entry_student_id.get()
    new_fees = entry_fees.get()

    # Execute the SQL command to update the student fees
    mycursor.execute("UPDATE students SET fees = %s WHERE id = %s", (new_fees, student_id))
    mydb.commit()

    # Display a message to confirm the update
    text.insert(tk.END, "Fees updated")

# Create the widgets for the school management system
label_student_id = tk.Label(root, text="Student ID:")
entry_student_id = tk.Entry(root)
button_show_student = tk.Button(root, text="Show Student", command=show_student)

label_fees = tk.Label(root, text="Fees:")
entry_fees = tk.Entry(root)
button_update_fees = tk.Button(root, text="Update Fees", command=update_fees)

text = tk.Text(root)

# Pack the widgets to the main window
label_student_id.pack()
entry_student_id.pack()
button_show_student.pack()

label_fees.pack()
entry_fees.pack()
button_update_fees.pack()

text.pack()

# Start the main loop of the school management system
root.mainloop()