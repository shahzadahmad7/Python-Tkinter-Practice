import tkinter as tk
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="dhldb"
)

# Create cursor
mycursor = mydb.cursor()

# Create tkinter window
window = tk.Tk()
window.title("Courier Management System - Print Bill")

# Create labels and entry fields
tk.Label(window, text="Enter Customer Reference No. :").grid(row=0, column=0)
customer_no_entry = tk.Entry(window)
customer_no_entry.grid(row=0, column=1)

# Create text widget for displaying bill details
bill_details_text = tk.Text(window)
bill_details_text.grid(row=1, column=0, columnspan=2)

# Define print bill function
def print_bill():
    # Get bill number from entry field
    customer_no = customer_no_entry.get()

    # Retrieve bill details from database
    sql = "SELECT * FROM `shipments` WHERE customer_no = %s"
    val = (customer_no,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Display bill details in text widget
        bill_details_text.delete('1.0', tk.END)
        bill_details_text.insert(tk.END, f"Customer Reference No.: {result[0]}\n")
        bill_details_text.insert(tk.END, f"Customer Name: {result[1]}\n")
        bill_details_text.insert(tk.END, f"Customer Address: {result[2]}\n")
        bill_details_text.insert(tk.END, f"Courier Weight: {result[5]} kg\n")
        bill_details_text.insert(tk.END, f"Total Amount: Rs.{result[6]} \n")
        
    else:
        # Display error message
        bill_details_text.delete('1.0', tk.END)
        bill_details_text.insert(tk.END, "Invalid bill number.")
    
# Create print button
tk.Button(window, text="Find", command=print_bill).grid(row=2, column=0, columnspan=2)

# Run tkinter main loop
window.mainloop()