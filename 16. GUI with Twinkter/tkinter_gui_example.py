""""
lets see that how we can create GUI
it always returns a name what i am written in it

"""
from tkinter import *
window = Tk()
def my_gui():
    print(b2_value.get())
    b3.delete(1.0,END)
    b3.insert(END,b2_value.get())


b1 = Button(window,text='execute',command=my_gui)
b1.grid(row=0,column=0)

b2_value = StringVar()
b2 =Entry(window,textvariable=b2_value)
b2.grid(row=0,column=1)


b3 = Text(window,height=1,width=20)
b3.grid(row =0 ,column =2)



window.mainloop()

""""
from first line it is import the tkinter so import all 
2. next we create the windows which is blank 
3. create a button having name of 'execute' and it execute the function which is writteen
4. crate  a entry point which is used to provide input  
5. grid is the way by which we can define its position 
6. StringVar() is the command for getting the value of which we enter in it 
6. create a text entry and by default it is degfined its position through its height and weight
7.function is defined and collecting its value from entry and return to text
"""