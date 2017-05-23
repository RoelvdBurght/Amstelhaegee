from tkinter import *
import tkinter
import Class
import Canvas
import Hillclimber
import SimulatedAnnealing
import Graphs
import random
import time

p = Class.makeMap(20, 1, True)
graph, climbed = SimulatedAnnealing.SA(SimulatedAnnealing.exponentialCooling,p, 20, 1000, 1, 1)
print(graph)
Canvas.addHouse(climbed)
mainloop()