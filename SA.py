import Class
import Hillclimber
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Dit laat zien hoe een cooling scheme er uit ziet
# t0 is de start temperatuur, tn de eindtemperatuur, en N het aantal iteraties
# het 'coolingscheme' argument is simpelweg de naam van een functie
# Voorbeeld: plotCooling(sigmoidalCooling, 1000, 10, 50)
def plotCooling(coolingScheme, title, t0, tn, N):
    data = []
    if coolingScheme == exponentialCooling:
        for i in range(N):
            try:
                data.append(t0 * pow((tn / t0), (i / N)))
            except OverflowError:
                data.append(tn)
    elif coolingScheme == linearCooling:
        for i in range(N):
            try:
                data.append(t0 - i * (t0 - tn)/N)
            except OverflowError:
                data.append(tn)
    elif coolingScheme == sigmoidalCooling:
        for i in range(N):
            try:
                data.append(tn + (t0 - tn)/(1+math.exp(0.003*(i-N/2))))
            except OverflowError:
                data.append(tn)
    elif coolingScheme == gemanCooling:
        for i in range(N):
            try:
                data.append(t0 / float((math.log(i + 1, 10) + tn)))
            except OverflowError:
                data.append(tn)
    x = range(N)
    y = data
    plt.title(title)
    plt.xlabel('Iteraties')
    plt.ylabel('Temperatuur')
    plt.plot(x, y)
    plt.show()

# t0 is de begintemperatuur
# tn is de eindtemperatuur
# Dit zijn de twee parameters die je aan kan passen
def exponentialCooling(i, verkeerd, itNR, t0, tn):
    N = itNR
    try:
        temp = t0 * pow((tn/t0),(i/N))
    except OverflowError:
        temp = tn
    chance = math.exp(float(verkeerd) / float(temp))
    return random.random() < chance

def linearCooling(i, verkeerd, itNR, t0, tn):
    N = itNR
    try:
        temp = t0 - i * (t0 - tn)/N
    except OverflowError:
        temp = tn
    chance = math.exp(float(verkeerd) / float(temp))
    result = random.random() < chance
    return result

def sigmoidalCooling(i, verkeerd, itNR, t0, tn):
    N = itNR
    try:
        temp = tn + (t0 - tn)/(1 + (math.exp(0.003*(i-N/2))))
    except OverflowError:
        temp = tn
    chance = math.exp(float(verkeerd) / float(temp))
    result = random.random() < chance
    return result

# c en d zijn de aanpasbare variabelen
def gemanCooling(i, verkeerd, itNR, c, d):
    try:
        temp = c/float((math.log(i + 1,2) + d))
    except OverflowError:
        temp = tn
    chance = math.exp(float(verkeerd) / float(temp))
    result = random.random() < chance
    return result

def SA(coolingScheme, t0, tn, houseList, goal, itNR, changeNum, maisonStrat, randomChangeNum=False):
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
        if randomChangeNum:
            lowerX, higherX = (oldX - random.randint(1, changeNum)), (oldX + random.randint(1, changeNum))
            lowerY, higherY = (oldY - random.randint(1, changeNum)), (oldY + random.randint(1, changeNum))
        else:
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
            if (newValue > value or coolingScheme(i, newValue - value, itNR, t0, tn))and not Class.overlapFinalBoss(houseList):
                #winst += newValue - value
                #counter += 1
                all_values.append(newValue)
            else:
                houseList[house].x = oldX
                houseList[house].y = oldY
                Class.update_dist_list(houseList, distList, house - 4)
                all_values.append(value)
        else:
            all_values.append(value)

    #print("winst =", winst)
    #print("NR verplaatsingen =", counter)
    return all_values, houseList


