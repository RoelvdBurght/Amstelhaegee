from tkinter import *
import tkinter
import Class

scale = 3
canvas = Canvas(width=160*scale, height=180*scale, bg='white')
canvas.pack(expand=YES, fil=BOTH)

def addMaison(x, y):
    canvas.create_rectangle(x, y, (x + 11), (y + 10.5))

def addBungalow(x,y):
    canvas.create_rectangle(x, y, (x + 10), (y + 7.5))

def addSingle(x,y):
    canvas.create_rectangle(x, y, (x + 8), (y + 8))


mainloop()