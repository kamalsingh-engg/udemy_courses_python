""""
lets see that how we can create GUI
it always convert the value in mile to km

"""
from tkinter import *

window = Tk()


def Mile_to_km():
    print(b2_value.get())
    km = float( b2_value.get())*1.6
    b3.delete(1.0,END)
    b3.insert(END, km)


b1 = Button(window, text='execute', command=Mile_to_km)
b1.grid(row=0, column=0)

b2_value = StringVar()
b2 = Entry(window, textvariable=b2_value)
b2.grid(row=0, column=1)

b3 = Text(window, height=1, width=20)
b3.grid(row=0, column=2)

window.mainloop()