from pl.forms import register
from customtkinter import *
from tkinter import *




if __name__=="__main__":


    screen= Tk()
    screen.geometry("%dx%d+%d+%d" % (350, 190, 600, 200))
    Pageme=register.App(screen,)
    screen.mainloop()


