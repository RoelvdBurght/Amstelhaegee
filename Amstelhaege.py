#import Class
from tkinter import *
import Class
import Canvas
import Hillclimber
import Graphs


value, p = Canvas.mapStats(1, 1, TRUE)
Class.distForAll(p)

list = [[20], 20]
print(list)


'''
#valuelist, p = Canvas.mapStats(1)
#map, value = Hillclimber.verplaatser(p, 20, 10, 5)

valuelist, p = Canvas.mapStats(100,1,True)
resultsclimb = []
resultsswap = []
for i in range(100):
    q, niks = Hillclimber.verplaatser(p,40,100, 3)
    resultsclimb.append(Class.valueOfMap(q))
    map = Hillclimber.houseSwapper(q, 40, 100)
    resultsswap.append(Class.valueOfMap(map))

data = [resultsclimb, resultsswap]
Graphs.boxPlot(data)






mapValues1, map1 = Canvas.mapStats(100, 1, True)
mapValues2, map2 = Canvas.mapStats(100, 2, True)
mapValues3, map3 = Canvas.mapStats(100, 1, False)
mapValues4, map4 = Canvas.mapStats(100, 2, False)
print(max(mapValues1))
print(max(mapValues2))
print(max(mapValues3))
print(max(mapValues4))
#values, p = Canvas.mapStats(100,1,True)
#map, value = Hillclimber.verplaatser(p, 40, 5000, 5)

#Graphs.lineGraph(value)

#Canvas.addHouse(map)
#mainloop()
'''
'''
valuelist, p = mapStats(23)
print("Oude waarde =               ", Class.valueOfMap(p))
map1 = Hillclimber.houseSwapper(p, 20, 500)
print("Waarde na swappen =         ", Class.valueOfMap(map1))
map2 = Hillclimber.verplaatser(map1, 20, 1000, 2)[0]
print("Waarde na verplaatsen =     ", Class.valueOfMap(map2))
map3 = Hillclimber.houseSwapper(map2, 20, 500)
print("Waarde na 2e X swappen =    ", Class.valueOfMap(map3))
map4 = Hillclimber.verplaatser(map3, 20, 1000, 3)[0]
print("Waarde na 2e X verplaatsen= ", Class.valueOfMap(map4))
map5 = Hillclimber.verplaatser(map4, 20, 1000, 5)[0]
print("Waarde na 3e X verplaatsen= ", Class.valueOfMap(map5))
map6 = Hillclimber.verplaatser(map5, 20, 1000, 10)[0]
print("Waarde na 4e X verplaatsen= ", Class.valueOfMap(map6))
map7 = Hillclimber.verplaatser(map6, 20, 1000, 15)[0]
print("Waarde na 5e X verplaatsen= ", Class.valueOfMap(map7))
map8 = Hillclimber.verplaatser(map7, 20, 1000, 3)[0]
print("Waarde na 6e X verplaatsen= ", Class.valueOfMap(map8))
map9 = Hillclimber.houseSwapper(map8, 20, 500)
print("Waarde na laatse X swappen =", Class.valueOfMap(map9))
addHouse(map9)
'''


#myList = Class.makeMap(20)
#myList = Class.makeMap(20)
#Canvas.addHouse(myList)