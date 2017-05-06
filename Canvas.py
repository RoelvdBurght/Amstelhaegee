from tkinter import *
import tkinter
import Class
import Hillclimber

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
        p = Class.makeMap(20,1)
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



valuelist, p = mapStats(25)
print("Oude waarde =               ", Class.valueOfMap(p))
map1 = Hillclimber.houseSwapper(p, 20, 500)
print("Waarde na swappen =         ", Class.valueOfMap(map1))
map2 = Hillclimber.verplaatser(map1, 20, 1000, 2)
print("Waarde na verplaatsen =     ", Class.valueOfMap(map2))
map3 = Hillclimber.houseSwapper(map2, 20, 500)
print("Waarde na 2e X swappen =    ", Class.valueOfMap(map3))
map4 = Hillclimber.verplaatser(map3, 20, 1000, 3)
print("Waarde na 2e X verplaatsen= ", Class.valueOfMap(map4))
map5 = Hillclimber.verplaatser(map4, 20, 1000, 5)
print("Waarde na 3e X verplaatsen= ", Class.valueOfMap(map5))
map6 = Hillclimber.verplaatser(map5, 20, 1000, 10)
print("Waarde na 4e X verplaatsen= ", Class.valueOfMap(map6))
map7 = Hillclimber.verplaatser(map6, 20, 1000, 15)
print("Waarde na 5e X verplaatsen= ", Class.valueOfMap(map7))
map8 = Hillclimber.verplaatser(map7, 20, 1000, 3)
print("Waarde na 6e X verplaatsen= ", Class.valueOfMap(map8))
map9 = Hillclimber.houseSwapper(map8, 20, 500)
print("Waarde na laatse X swappen =", Class.valueOfMap(map9))


addHouse(map9)
mainloop()
