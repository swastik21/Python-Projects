from tkinter import *
import string,random
import pyperclip

win = Tk()
win.geometry("400x200")
win.resizable(0,0)
win.title("Password Generator")

Label(win,text="Password Generator",font="Arial 15 bold").pack()
Label(win,text="Password Length",font='Arial 10 bold').pack()
pass_len = IntVar()
Spinbox(win,from_=8, to_=32,width=15,textvariable=pass_len).pack()

pass_str = StringVar()
def generator():
    password=''
    for i in range(0,4):
        password=random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
    for i in range(pass_len.get()-4):
        password=password+random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
    pass_str.set(password)

Button(win,text="Generate",command=generator).pack(pady=5)
Entry(win,textvariable=pass_str).pack()

def copy():
    pyperclip.copy(pass_str.get())
Button(win,text="Copy to clipboard",command=copy).pack(pady=5)

win.mainloop()