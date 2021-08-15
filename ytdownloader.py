from tkinter import *
from tkinter import ttk
import pytube
import time
from pytube.__main__ import YouTube
from tkinter.ttk import Progressbar


win = Tk()
win.geometry("500x200")
win.resizable(0,0)
win.title("Youtube Downloader")

Label(win,text="Youtube Video Downloader",font=("Aerial",20,"bold"),fg="maroon").pack()

link = StringVar()
Label(win,text="Paste link here:",font="Aerial 15 bold").place(x=160,y=60)
link_enter = Entry(win,textvariable=link,width=70,bg="grey").place(x=32,y=90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download() 
    progressbar = ttk.Progressbar(win,orient ="horizontal",length = 200, mode ="determinate")
    progressbar.pack()
    progressbar["maximum"] = 100
    progressbar["value"] = 100
    Label(win,text="DOWNLOADED",font="Aerial 15").place(x=180,y=210)
Button(win,text="Download",font="Aerial 15 bold",bg="white",fg="black",padx=2,command=Downloader).place(x=180,y=150)

win.mainloop()

