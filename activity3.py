from tkinter import *

root = Tk()
root.geometry('400x600')
root.title("Activity3")

def topwin():
    top=Toplevel()
    top.title("toplevel")
    top.geometry('300x400')
    a=Label(top,text="top")

    a.pack()
    top.mainloop()


b=Label(root, text="click here to enter in topwin website")
btn=Button(root,text="cliclere",commmand=topwin)

b.pack()
btn.pack()






root.mainloop()