import tkinter
from PIL import Image,ImageTk
import random

win = tkinter.Tk()
win.geometry('400x400')
win.title("Roll the Dice")

blankline = tkinter.Label(win,text="")
blankline.pack()

heading = tkinter.Label(win,text="Welcome!",
                        fg="light green",
                        bg="dark green",
                        font="Helvetica 16 bold italic")
heading.pack()

dice = ["die1.png","die2.png","die3.png","die4.png","die5.png","die6.png"]
diceimg = ImageTk.PhotoImage(Image.open(random.choice(dice)))

imagelabel = tkinter.Label(win,image=diceimg)
imagelabel.image = diceimg
imagelabel.pack(expand=True)

def roll():
    diceimg = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    imagelabel.configure(image=diceimg)
    imagelabel.image = diceimg

button = tkinter.Button(win,text="Roll the dice",fg= "white",bg="black",height=2,command=roll)
button.pack()

blankline = tkinter.Label(win,text="")
blankline.pack()

win.mainloop()