from tkinter import *
import tkinter
import Class
import Canvas
import Hillclimber
import Graphs
import random
import time
random.seed(123)

start = time.time()
# depthFirstSearch(trails, goal, waterTact, maisonTact)
# verplaatser(map, goal, iterations, change_pixel, maisonTact)
values, p = Class.depthFirstSearch(500, 40, 1, 0)
distlist = Class.initDistList(p)
Class.mapFinalCheck(p,distlist)
print(time.time() - start)
Canvas.addHouse(p)
mainloop()
# climbed = Hillclimber.verplaatser(p, 40, 500, 1, 0)

