from tkinter import *
import tkinter
import Class


canvas = Canvas(width=600, height=600, bg='white')
canvas.pack(expand=YES, fil=BOTH)

canvas.create_rectangle(200, 200, 300, 300, width=5, fill='red')


def addMaison(x, y):
    canvas.create_rectangle(x, y, (x + 11), (y + 10.5))

def addBungalow(x,y):
    canvas.create_rectangle(x, y, (x + 10), (y + 7.5))

def addSingle(x,y):
    canvas.create_rectangle(x, y, (x + 8), (y + 8))


mainloop()