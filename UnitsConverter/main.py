from tkinter import *

window = Tk()
window.title("Fahrenheit to Celcius Converter")
window.minsize(width=400, height=100)

fahrenheit_label = Label(text="Fahrenheit", font=("Arial", "16"))
fahrenheit_label.grid(column=2, row=0)
equal_label = Label(text="is equal to", font=("Arial", "16"))
equal_label.grid(column=0, row=1)         
result_label = Label(text="0", font=("Arial", "16"))
result_label.grid(column=1, row=1)
celsius_label = Label(text="Celsius", font=("Arial", "16"))
celsius_label.grid(column=2, row=1)

input = Entry()
input.grid(column=1, row=0)

def calculate():
    F = float(input.get())
    C = (F - 32) / 1.8
    result_label["text"] = str("%.2f" % C)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()