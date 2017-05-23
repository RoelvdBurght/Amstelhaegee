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
test = []
for i in range(1000):
    test.append(math.exp(float(-5) / (1000 / float(i + 1))))

x = range(len(test))
y = test
plt.plot(x, y)
plt.show()