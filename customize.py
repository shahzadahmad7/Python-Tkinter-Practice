import tkinter
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")
# customtkinter.set_appearance_mode("Light")
# customtkinter.set_appearance_mode("Dark")

def button_function():
    print("button pressed")

label = customtkinter.CTkLabel(master=root_tk,
                               text="Welcome to Mandi Bahauddin",
                               width=300,
                               height=25,
                               corner_radius=8)
label.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=root_tk,
                               width=120,
                               height=25,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

text = entry.get()

# Use CTkButton instead of tkinter Button
#fg_color=("black", "lightgray"),  # <- tuple color for light and dark theme
button = customtkinter.CTkButton(master=root_tk, corner_radius=10,fg_color=("blue", "lightgray"), command=button_function)
button.place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)

root_tk.mainloop()