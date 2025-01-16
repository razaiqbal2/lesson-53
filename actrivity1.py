from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title('Image in python')
root.geometry('800x700')

upload=Image.open('demon.jpeg')
image=ImageTk.PhotoImage(upload)

l=Label(root,image=image,height=300,width=400)
l.place(x=200,y=500)

b=Button(root,image=image,height=300,width=400)
b.place(x=200,y=100)

root.mainloop()