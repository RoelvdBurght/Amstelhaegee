from tkinter import *
import tkinter
import Class

def scale(x):
    return x * 3

canvas = Canvas(width=scale(160), height=scale(180), bg='white')
canvas.pack(expand=YES, fil=BOTH)

#legend = Label(canvas, text='red = Maison | blue = Bungalow | green = single', fg='black', bg='white')
#legend.pack()

#draws 2 squares, first one is the free space needed, second is the single
def addSingle(x,y):
    width = scale(x)
    height = scale(y)
    canvas.create_rectangle(width - scale(2), height - scale(2), (width + scale(8)) + scale(2),
                            (height + scale(8)) + scale(2), fill='black')
    canvas.create_rectangle(width, height, (width + scale(8)), (height + scale(8)), fill='green')

#draws 2 squares, first one is the free space, second is the bungalow
def addBungalow(x,y):
    width = scale(x)
    height = scale(y)
    canvas.create_rectangle(width - scale(3), height - scale(3), (width + scale(10)) + scale(3),
                            (height + scale(7.5)) + scale(3), fill='black')
    canvas.create_rectangle(width, height, (width + scale(10)), (height + scale(7.5)), fill='purple')


#draws 2 squares, first one is the free space needed, second is the maison
def addMaison(x, y):
    width = scale(x)
    height = scale(y)
    canvas.create_rectangle(width - scale(6), height - scale(6), (width + scale(11)) + scale(6),
                            (height + scale(10.5)) + scale(6), fill='black')
    canvas.create_rectangle(width, height, (width+scale(11)), (height+scale(10.5)), fill='red')


x = Class.SingleHouse(10,30)
y = Class.SingleHouse(20,40)

print(Class.distanceBetweenQuick(x,y))
addSingle(x.x,x.y)
addSingle(y.x,y.y)
mainloop()