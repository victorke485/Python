from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

def miles_to_km():    
    results.config(text=f"{int(float(input.get()) * 1.60934)}")
    results.grid(column=1, row=1)

# empty_label = Label()
# empty_label.grid(column=0, row=0)

input = Entry()
input.config(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

results = Label()

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)

window.mainloop()