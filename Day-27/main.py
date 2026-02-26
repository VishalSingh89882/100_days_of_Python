
import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="New Text", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    #print("I got clicked")
    #my_label.config(text="Button Got Clicked")
    input_text = input.get()
    my_label.config(text=input_text)


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()


input = tk.Entry(width=10)
input.pack()







window.mainloop()
