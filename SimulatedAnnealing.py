import Class
import Hillclimber
import random
import math
import numpy as np

def exponentialCooling(i, verkeerd):
    chance = math.exp(float(verkeerd) / (1 / float(i + 1)))
    return random.random() < chance

def SA(coolingScheme, houseList, goal, itNR, changeNum, maisonStrat):
    counter = 0
    winst = 0
    all_values = []
    distList = Class.initDistList(houseList)
  #--------------------1-------------------------#
    for i in range(itNR):
        value = Class.valueOfMapFast(houseList, distList)
        house = Hillclimber.getIndex(goal, maisonStrat)
 #--------------------2--------------------------#
        oldX = houseList[house].x
        oldY = houseList[house].y
        lowerX, higherX = (oldX - changeNum), (oldX + changeNum)
        lowerY, higherY = (oldY - changeNum), (oldY + changeNum)
        newX = random.randint(round(lowerX), round(higherX))
        newY = random.randint(round(lowerY), round(higherY))
 #--------------------3--------------------------#
        if not Hillclimber.checkHouseOutOfBounds(houseList[house], newX, newY):
            houseList[house].x = newX
            houseList[house].y = newY
            Class.update_dist_list(houseList, distList, house - 4)
            newValue = Class.valueOfMapFast(houseList, distList)
            if (newValue > value or coolingScheme(i, newValue - value)) and not Class.overlapFinalBoss(houseList):
                print("--------")
                print(value, "old")
                print(newValue, "new")
                winst += newValue - value
                counter += 1
            else:
                houseList[house].x = oldX
                houseList[house].y = oldY
                Class.update_dist_list(houseList, distList, house - 4)
            all_values.append(value)
    print("winst =", winst)
    print("NR verplaatsingen =", counter)
    return all_values, houseList