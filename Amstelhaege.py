from tkinter import *
import tkinter
import Class
import Canvas
import Hillclimber
import Graphs
import time
import cProfile
import random

random.seed(123)
values,p = Canvas.mapStats(100)
# map, value = Hillclimber.verplaatser(p, 40, 50, 5)
# Graphs.lineGraph(value)
Canvas.addHouse(p)
#print(time.time()-start_time)
mainloop()

