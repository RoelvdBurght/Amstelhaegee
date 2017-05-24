from tkinter import *
import tkinter
import Class
import Canvas
import Hillclimber
import SimulatedAnnealing
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import math

#p = Class.makeMap(20, 1, True)
#values, climbed = SimulatedAnnealing.SA(SimulatedAnnealing.exponentialCooling,p, 20, 1000, 1, 1)
#test = []
#for i in range(1000):
#    test.append(math.exp(float(-5) / (1000 / float(i + 1))))
""""
p = Class.depthFirstSearch(500,40,0,1)
q = Hillclimber.verplaatser(p,40,10000,15,1)
q2 = Hillclimber.verplaatser(p,40,10000,10,1)
q3 = Hillclimber.verplaatser(p,40,10000,5,1)
q4 = Hillclimber.verplaatser(p,40,10000,3,1)
q5 = Hillclimber.verplaatser(p,40,10000,2,1)
finalmap = Hillclimber.verplaatser(p,40,10000,1,1)
"""
eindwaarde = 0
finalBoss = []
maxEindwaarde = 0
for i in range(250):
    print("----------------")
    varList, p = Class.depthFirstSearch(500, 40, 1, True)
    distlist = Class.initDistList(p)
    beginwaarde = Class.valueOfMapFast(p, distlist)
    print("initial value", beginwaarde)
    q1 = Hillclimber.verplaatser(p,40,10000,15,2)
    q2 = Hillclimber.houseSwapper(q1, 40, 1000)
    q3 = Hillclimber.verplaatser(q2,40,10000,8,2)
    q4 = Hillclimber.houseSwapper(q3, 40, 1000)
    q5 = Hillclimber.verplaatser(q4,40,10000,3,2)
    q6 = Hillclimber.houseSwapper(q5, 40, 1000)
    finalmap = Hillclimber.verplaatser(q6,40,10000,1,2)
    newdistlist = Class.initDistList(finalmap)
    eindwaarde = Class.valueOfMapFast(finalmap, newdistlist)
    print("totale winst =",eindwaarde - beginwaarde)
    if eindwaarde > maxEindwaarde:
        maxEindwaarde = eindwaarde
        finalBoss = finalmap
        print("***********")
        print("Boss", eindwaarde)
        print("***********")

Canvas.addHouse(finalBoss)
mainloop()

#x = range(len(test))
#y = test
#plt.plot(x, y)
#plt.show()