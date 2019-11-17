from tkinter import *
from tkinter import ttk
def button_click():
    label.configure(text="Hello World")
if __name__ == "__main__":
    win = Tk()
    win.title("Test Program")
    label = Label(win)
    label.grid()
    button = Button(win,text="press",width=20,command=button_click)
    button.grid()
    win.mainloop()
