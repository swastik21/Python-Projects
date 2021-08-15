from tkinter import *
import datetime
import winsound

def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print(f"The set date is: {date}")
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break
def actual():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock,text="Enter time in 24hour format",fg="red",bg="black",font="Aerial").place(x=60,y=120)
addtime = Label(clock,text="Hour    Min      Sec",font=60).place(x=110)
setyouralarm = Label(clock,text="When to wake you up",fg="blue",relief="solid",font=("Helevetica",7,"bold")).place(y=29)
hour = StringVar()
min = StringVar()
sec = StringVar()
hourentry = Entry(clock,textvariable=hour,bg="pink",width=15).place(x=110,y=30)
minentry = Entry(clock,textvariable=min,bg="pink",width=15).place(x=150,y=30)
secentry = Entry(clock,textvariable=sec,bg="pink",width=15).place(x=200,y=30)
submit = Button(clock,text="Set alarm",fg="red",width=10,command=actual).place(x=110,y=70)
clock.mainloop()

