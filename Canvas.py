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

# voegt nummer toe aan huizen op canvas
def addNumber(i, list):
    canvas.create_text(scale(list.x), scale(list.y), fill="white", font="Times 10 bold",text= i)

# tieft die huizen op de canvas
# input: lijst gemaakt door makeMap
def addHouse(list):
    for i in range(len(list)):
        if list[i].width == 8:
            addSingle(list[i].x, list[i].y)
            addNumber(i, list[i])
        elif list[i].width == 10:
            addBungalow(list[i].x, list[i].y)
            addNumber(i, list[i])
        elif list[i].width == 11:
            addMaison(list[i].x, list[i].y)
            addNumber(i, list[i])
        else:
            raise TypeError ("Item in list in not a House")


p = Class.makeMap(20)
Class.closestTo(Class.distToAll(p))

# dit was om een begin te maken om waarde te berekenen
for i in p:
   print(type(i))
   if type(i) == Class.Maison:
       print("jes")

#Class.closestTo(Class.distToAll(p))

print(p)
"""
for i in range(len(p) - 1):
    dist = []
    dist.append(p[i].distanceTo(p[i+1]))
    print("distance between house", i, 'and house', i + 1, "=", dist)
#for i in range(len(p)):
"""
addHouse(p)
mainloop()