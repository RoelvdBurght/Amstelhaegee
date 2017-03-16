from tkinter import *
import tkinter
import Class


canvas = Canvas(width=600, height=600, bg='white')
canvas.pack(expand=YES, fil=BOTH)

canvas.create_rectangle(200, 200, 300, 300, width=5, fill='red')


def addMaison(x, y):
    newMaison = canvas.create_rectangle(x, y, (x + 11), (y + 10.5))

def add
addMaison(2,6)
mainloop()