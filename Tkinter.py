from tkinter import *
win = Tk()
win.title("First GUI with Py")
label = Label(win,text = "Label Test Program", bg = 'red', fg = 'white')
label.pack()

button = Button(win, text= 'Press', width=10)
button.pack()

ck = Checkbutton(win,text = "Remember Me", variable = v, v = True)
ck.pack()
win.mainloop()
