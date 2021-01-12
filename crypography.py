import onetimepad
from tkinter import *
#import tkinter

root= Tk()
root.title("Cryptography app")

def encryptMessage():
    a=var.get()
    #razual
    ct=onetimepad.encrypt(a,"Assignments")
    print("Working",ct)
    
    e2.delete(0,END)
    e2.insert(END,ct)
    
def dycryptMessage():
    a=var2.get()
    #razual
    ct=onetimepad.decrypt(a,"Assignments")
    print("Working",ct)
    
    e4.delete(0,END)
    e4.insert(END,ct)
    

l1=Label(root, text="Plain Text")
l1.grid(row=0, column=0)

l3=Label(root, text="Encrypted Text")
l3.grid(row=0, column=2)
var=StringVar()
e1= Entry(root, textvariable=var)
e1.grid(row=0,column=1)
var2=StringVar()
e3= Entry(root, textvariable=var2)
e3.grid(row=0,column=3)
l2=Label(root, text="Encrypted Text")
l2.grid(row=1, column=0)
l4=Label(root, text="Plain Text")
l4.grid(row=1, column=2)

e2= Entry(root)
e2.grid(row=1,column=1)

e4= Entry(root)
e4.grid(row=1,column=3)

b1= Button(root, text="Encryption", bg="turquoise", fg="Red", command=encryptMessage)
b1.grid(row=2, column=1)

b2= Button(root, text="Dycryption", bg="turquoise", fg="Red", command=dycryptMessage)
b2.grid(row=2, column=3)



root.mainloop()


