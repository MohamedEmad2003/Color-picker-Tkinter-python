
from tkinter import *
from tkinter import colorchooser

window=Tk()
window.geometry('500x200+200+200')
window.title('Color Picker')
window.resizable(FALSE,FALSE)


color_pick=StringVar()
color_pick.set(colorchooser.askcolor())

txtlb = Label(window,text="Your color name in \nRGB and  Hexadecimal form is:",font="arial 15 bold").pack()
show = Label(window,textvariable=color_pick,font="arial 15 bold",fg="blue").pack()

window.mainloop()
