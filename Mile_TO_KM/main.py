from tkinter import *


def button_clicked():
    print("I got clicked")
    miles = input_miles.get()
    print(miles)
    km=int(miles)*1.609
    print(km)
    my_label_1 = Label(text=km, font=("Arial", 20))
    my_label_1.grid(column=1, row=1)

window = Tk()
window.title("Miles To Km")
window.minsize(width=300, height=100)
# window.config(padx=100, pady=200)

#Label
my_label = Label(text="Miles", font=("Arial", 10 ))
my_label.grid(column=2, row=0)
# my_label.config(padx=10, pady=10)

my_label_km = Label(text="Km", font=("Arial", 10))
my_label_km.grid(column=2, row=1)
# my_label_km.config(padx=10, pady=10)


my_label_2 = Label(text="is equal to", font=("Arial", 10 ))
my_label_2.grid(column=0, row=1)
# my_label_2.config(padx=10, pady=10)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input_miles = Entry(width=15)
print(input_miles.get())
input_miles.grid(column=1, row=0)


window.mainloop()