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
import xlsxwriter
workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()
import copy


varList, p = Class.depthFirstSearch(500, 40, 0, False)
distlist = Class.initDistList(p)
q1 = Hillclimber.verplaatser(p, 40, 10000, 15, False)
distlist = Class.initDistList(q1)
worksheet.write(0,0, Class.valueOfMapFast(q1, distlist))
worksheet.write(0,1, str(q1))
q2 = Hillclimber.houseSwapper(q1, 40, 2500)
distlist = Class.initDistList(q2)
worksheet.write(1,0, Class.valueOfMapFast(q2, distlist))
worksheet.write(1,1, str(q2))
q3 = Hillclimber.verplaatser(q2, 40, 1000, 5, False)
distlist = Class.initDistList(q3)
worksheet.write(2,0, Class.valueOfMapFast(q3, distlist))
worksheet.write(2,1, str(q3))

"""
q4 = Hillclimber.houseSwapper(q3, 40, 2500)
q5 = Hillclimber.verplaatser(q4, 40, 100000, 3, False)
q6 = Hillclimber.houseSwapper(q5, 40, 2500)
finalBoss = Hillclimber.verplaatser(q6, 40, 100000, 1, False)
"""
Canvas.addHouse(q3)
mainloop()

#x = range(len(test))
#y = test
#plt.plot(x, y)
#plt.show()



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