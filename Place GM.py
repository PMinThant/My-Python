from tkinter import *
win = Tk()
win.resizable(0,0)
Button(win,text='Absolute').place(x=70,y=10)
Button(win,text="Relative").place(relx=0.7,rely=0.4,relwidth=0.4,relheight=0.3,width=1,anchor=E)
win.mainloop()
