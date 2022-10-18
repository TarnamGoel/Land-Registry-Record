from SortingData import *
from tkinter import *

root=Tk()

userid_var=IntVar()
name_var=StringVar()

def check():
    global d
    name=name_var.get()
    userid=userid_var.get()

    l=d[name[0].upper()]

    if len(l)==0:
        print("No data exist")
    else:
        for i in range(len(l)):
            if l[i][1]==name and l[i][0]==userid:
                val1=Label(root,text=f'Registry number: {l[i][0]}',font='Arial 15 bold')
                val1.grid(row=3,column=1)
                val2=Label(root,text=f'Registry id: {l[i][1]}',font='Arial 15 bold')
                val2.grid(row=4,column=1)
                val3=Label(root,text=f'First name: {l[i][2]}',font='Arial 15 bold')
                val3.grid(row=5,column=1)
                val4=Label(root,text=f'Last name: {l[i][3]}',font='Arial 15 bold')
                val4.grid(row=6,column=1)
                val5=Label(root,text=f'Gender: {l[i][4]}',font='Arial 15 bold')
                val5.grid(row=7,column=1)
                val6=Label(root,text=f'Status: {l[i][6]}',font='Arial 15 bold')
                val6.grid(row=8,column=1)

userid=Label(root, text='Registry Number:',font='Lucida 15')
userid.grid(row=0,column=0,padx=20,pady=30)

userid_entry=Entry(root,textvariable=userid_var,font='Arial 15 bold')
userid_entry.grid(row=0,column=1)

name=Label(root,text='First Name:',font='Lucida 15')
name.grid(row=1,column=0)

name_entry=Entry(root,textvariable=name_var,font='Arial 15 bold')
name_entry.grid(row=1,column=1)

button=Button(root,text='Submit',command=check,padx=20,pady=5,background="black",foreground='white',font='Arial 15 bold')
button.grid(row=2,column=1,pady=20)

root.geometry('350x350')
root.title('Land Registry - Data Searching Portal')

root.mainloop()

