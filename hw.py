from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Password Checker")
root.geometry("500x500")
lbl = Label(root, text = "Oh hello! Check the strength of ur password from our site!")
label = Label(root, text = "Pls enter ur password here:-")
l1 = Entry(root)
label.place(x=140, y=50)
lbl.place(y = 0, x = 90)
l1.place(y = 90, x = 140)
def entry():
    try:
        if (l1 < 5):
            lbl1 = Label(entry, text = "The password is too weak")
        if (l1 > 5):
            lbl2 = Label(entry, text = "This password is medium")
        if (l1 > 8):
            lbl3 = Label(entry, text = "This is a very strong password")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
    lbl1.place(x = 140, y = 140)
    lbl2.place(x=140, y  = 140)
    lbl3.place(x = 140, y = 140)
btn = Button(root, text="Tell strength of password", command=entry, bg="brown", fg="white")
btn.place(x = 140, y = 110)
root.mainloop()