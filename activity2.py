from tkinter import*
from tkinter import messagebox

root=Tk()
root.title('Message box')
root.geometry('500x600')

def msg():
    messagebox.showwarning('Alert','Virus Detected')

b=Button(root,text='Scan',command=msg)
b.place(x=50,y=30)

root.mainloop()