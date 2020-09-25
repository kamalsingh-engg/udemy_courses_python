from  tkinter import *
import backend





def get_selected_row(event):
    try:
        global select_tuple
        index =lt1.curselection()[0]
        select_tuple = lt1.get(index)
        e1.delete(0,END)
        e1.insert(END,select_tuple[1])
        e2.delete(0, END)
        e2.insert(END, select_tuple[2])
        e3.delete(0, END)
        e3.insert(END, select_tuple[3])
        e4.delete(0, END)
        e4.insert(END, select_tuple[4])


    except IndexError:
        pass






def view_all():
    lt1.delete(0,END)
    for row in backend.view():

        lt1.insert(END,row)

def search_command():
    lt1.delete(0, END)
    for row in backend.Search(Title_text.get(),Year_text.get(),Author_text.get(),ID_text.get()):
        lt1.insert(END, row)

def add_command():

    backend.insert(Title_text.get(), Year_text.get(), Author_text.get(), ID_text.get())
    lt1.delete(0, END)
    lt1.insert(END, (Title_text.get(), Year_text.get(), Author_text.get(), ID_text.get()))


def delete_command():
    backend.delete(select_tuple[0])

def update_command():
    backend.update(select_tuple[0],Title_text.get(), Year_text.get(), Author_text.get(), ID_text.get())


window =Tk()

l1 =Label(window,text = "Title")
l1.grid(row = 0,column = 0)

l2 =Label(window,text = "Year")
l2.grid(row = 1,column = 0)

l3 =Label(window,text = "Author")
l3.grid(row = 0,column = 2)

l4 =Label(window,text = "ISBN")
l4.grid(row = 1,column = 2)

Title_text = StringVar()
e1 =Entry(window,textvariable=Title_text)
e1.grid(row = 0,column=1 )

Year_text = StringVar()
e2 =Entry(window,textvariable=Year_text)
e2.grid(row = 1,column=1 )

Author_text = StringVar()
e3 =Entry(window,textvariable=Author_text)
e3.grid(row = 0,column=3 )

ID_text = StringVar()
e4 =Entry(window,textvariable=ID_text)
e4.grid(row = 1,column=3 )

lt1 =Listbox(window,height=6,width=35)
lt1.grid(row=2,columns=1,rowspan=6,columnspan=2)
lt1.bind('<<ListboxSelect>>',get_selected_row)
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
lt1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lt1.yview)

b1 = Button(window,text="View All",width=12,command=view_all)
b1.grid(row=2,column=3)
b2 = Button(window,text="Search entry",width=12 ,command=search_command)
b2.grid(row=3,column=3)
b3 = Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)
b4 = Button(window,text="update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)
b5 = Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)










window.mainloop()




