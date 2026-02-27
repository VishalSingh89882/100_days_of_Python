
from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(window, width=10)
miles_input.grid(column=1, row=0)


miles_label = Label(window, text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(window, text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(window, text="0")
km_result_label.grid(column=1, row=1)


km_label = Label(window, text="Km")
km_label.grid(column=2, row=1)


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

button = Button(window, text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()