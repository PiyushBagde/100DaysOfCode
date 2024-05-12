from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)


def miles_to_km():
    miles = float(input_mile.get())
    new_km = 1.609344 * miles
    converted_value.config(text=round(new_km, 2))


# input in mile
input_mile = Entry(width=10)
input_mile.grid(row=0, column=1)

# show miles

mile = Label(text='Miles')
mile.grid(row=0, column=2)

# show is equal to

equal_to = Label(text='is equal to')
equal_to.grid(row=1, column=0)

# show Km label

km = Label(text='Km', width=10)
km.grid(row=1, column=2)

# show converted value

converted_value = Label(text='0')
converted_value.config(padx=10, pady=10)
converted_value.grid(row=1, column=1)

# calculate
button = Button(text='Calculate', command=miles_to_km, font=('Aerial', 10, 'bold'))
button.grid(row=2, column=1)

window.mainloop()
