from tkinter import *
import tkinter
import Class
import Hillclimber
import time
import cProfile

start_time = time.time()


def scale(x):
    return x * 3

canvas = Canvas(width=scale(160), height=scale(180), bg='white')
canvas.pack(expand=YES, fil=BOTH)

#legend = Label(canvas, text='red = Maison | blue = Bungalow | green = single', fg='black', bg='white')
#legend.pack()
def addWater(x,y, width, height):
    canvas.create_rectangle(scale(x), scale(y), scale(x) + scale(width), scale(y) + scale(height), fill='blue')

#draws 2 squares, first one is the free space needed, second is the single
def addSingle(x,y):
    width = scale(x)
    height = scale(y)
   # canvas.create_rectangle(width - scale(2), height - scale(2), (width + scale(8)) + scale(2),
    #                        (height + scale(8)) + scale(2), fill='black')
    canvas.create_rectangle(width, height, (width + scale(8)), (height + scale(8)), fill='green')

#draws 2 squares, first one is the free space, second is the bungalow
def addBungalow(x,y):
    width = scale(x)
    height = scale(y)
   # canvas.create_rectangle(width - scale(3), height - scale(3), (width + scale(10)) + scale(3),
    #                       (height + scale(7.5)) + scale(3), fill='black')
    canvas.create_rectangle(width, height, (width + scale(10)), (height + scale(7.5)), fill='purple')


#draws 2 squares, first one is the free space needed, second is the maison
def addMaison(x, y):
    width = scale(x)
    height = scale(y)
    #canvas.create_rectangle(width - scale(6), height - scale(6), (width + scale(11)) + scale(6),
     #                       (height + scale(10.5)) + scale(6), fill='black')
    canvas.create_rectangle(width, height, (width+scale(11)), (height+scale(10.5)), fill='red')

# voegt nummer toe aan huizen op canvas
def addNumber(i, list):
    canvas.create_text(scale(list.x), scale(list.y), fill="black", font="Times 10 bold",text= i)

#zet het water vooraan in de lijst
def sortList(houseList):
    for i in range(len(houseList)):
        if houseList[i].width == 0:
            houseList.insert(0, houseList[i])
    return houseList

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
        elif list[i].freespace == 0:
            addWater(list[i].x, list[i].y, list[i].width, list[i].height)
        else:
            raise TypeError ("Item in list in not a House")

def mapStats(trails):
    max = 0
    max_map = None
    total = 0
    allValues = []
    for i in range(trails):
        p = Class.makeMap(40,1)
        value = Class.valueOfMap(p)
        total += value
        allValues.append(value)
        if Class.valueOfMap(p) > max:
            max = Class.valueOfMap(p)
            max_map = p
    print("initial map is done")
    return allValues,max_map

""""
Dit doet het nog niet
"""
def hillClimberMultiple(trails, map, goal, itNR, moveNR):
    max = 0
    max_map = NONE
    for i in range(trails):
        q = Hillclimber.verplaatser(map, goal, itNR, moveNR)
        value = Class.valueOfMap(q)
        if value > max:
            max = value
            max_map = q
    return max_map

def startFunction():
    q = Class.makeMap(40, 1)
    z = Hillclimber.verplaatser(q, 40, 100, 3)
    c = Hillclimber.houseSwapper(z, 40, 100)


map = Class.makeMap(40, 1)
distList = Class.initDistList(map)
print(Class.valueOfMap(map))
print(Class.valueOfMapFast(map, distList))
addHouse(map)
mainloop()
#cProfile.run('startFunction()')