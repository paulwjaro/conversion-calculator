from tkinter import *

window = Tk()
window.title("Fahrenheit to Celsius Converter")
window.config(padx=20, pady=10)


equal_label = Label(text="is equal to:")
equal_label.grid(row=2, column=1)
equal_label.config(padx=10, pady=10)
cels_label = Label(text="Celsius")
cels_label.grid(row=2, column=3)
cels_label.config(padx=10, pady=10)
far_label = Label(text="Fahrenheit")
far_label.grid(row=1, column=3)
far_label.config(padx=10, pady=10)
conversion_label = Label(text=str(0))
conversion_label.grid(row=2, column=2)
conversion_label.config(padx=10, pady=10)

e = Entry()
e.grid(row=1, column=2)
e.config(width=10)


def temp_conversion():
    global e
    cel = ((int(e.get()) - 32) * 5/9)
    conversion_label["text"] = int(cel)


button = Button(text="Convert", command=temp_conversion)
button.grid(row=3, column=2)

window.mainloop()
