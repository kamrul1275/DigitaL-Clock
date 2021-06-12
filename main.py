from tkinter import *
import time

root = Tk()

def times():
    timevar= time.strftime('%I: %M: %S ')
    Label.config(text=timevar)
    Label.after(200, times)


Label = Label(root, text='Clock' , font=("DS-Digital", 100), bg='black' , fg='red' )
Label.pack()
times()

root.mainloop()
