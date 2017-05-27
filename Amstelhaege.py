from tkinter import *
import tkinter
import Class
import Canvas
import Hillclimber
import SA
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import math
import copy

values, max_map = Class.depthFirstSearch(10, 40, 3, True)
Canvas.addHouse(max_map)
mainloop()
#original_map = copy.deepcopy(max_map)
#climb_values1, map1 = Hillclimber.verplaatser(max_map, 40, 1000, 3, True)
#climb_values2, map2 = Hillclimber.houseSwapper(map1, 40, 2500)
#climb_values3, final_map = Hillclimber.verplaatser(map2, 40, 1000, 3, True)
#SA_values, final_SA_map = SA.SA(SA.sigmoidalCooling, original_map, 40, 4500, 3, True)
#climb_values = climb_values1+climb_values2+climb_values3
#x1 = climb_values
#x2 = SA_values
#y = range(len(SA_values))
#plt.plot(y, x2,color="blue")
#plt.plot(y, x1,color="red")
#plt.show()
#Canvas.addHouse(final_map)




def codeHouseList(houseList):
    codedHouselist = []
    for object in houseList:
        codedHouselist.append((object.x, object.y, object.width, object.height, object.freespace))
    return codedHouselist

def decodeHouseList(codedHouseList):
    houseList = []
    for tuple in codedHouseList:
        if tuple[4] == 0:
            houseList.append(Class.Water(tuple[0], tuple[1], tuple[2], tuple[3], 1))
        elif tuple[4] == 2:
            houseList.append(Class.SingleHouse(tuple[0], tuple[1]))
        elif tuple[4] == 3:
            houseList.append(Class.Bungalow(tuple[0], tuple[1]))
        elif tuple[4] == 6:
            houseList.append(Class.Maison(tuple[0], tuple[1]))
    return houseList