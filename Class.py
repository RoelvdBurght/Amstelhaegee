import math
import random
import copy
import numpy as np
#random.seed(1)

class House:
    def distanceTo(self, other):
        return minDistanceBetween(self, other)

class SingleHouse(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.value = 285000
        self.freespace = 2
        self.percentage = 0.03

class Bungalow(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 7.5
        self.value = 399000
        self.freespace = 3
        self.percentage = 0.04

class Maison(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 11
        self.height = 10.5
        self.value = 610000
        self.freespace = 6
        self.percentage = 0.06

# Shape 1 is a square, shape 2 is a circle
class Water(House):
    def __init__(self, x, y, width, height, shape):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.freespace = 0
        self.shape = shape

# calculates the distance from from all houses to all houses
def initDistList(houseList):
    houseList = houseList[4:]
    length = len(houseList)
    distList = []
    for i in range(length):
        all_dist_from_i = []
        for j in range(length):
            if i == j:
                all_dist_from_i.append(0)
                continue
            distance = houseList[i].distanceTo(houseList[j])
            all_dist_from_i.append(distance)
        distList.append(all_dist_from_i)
    return distList

# calculate freespace from a house out of the distlist
def freespaceFromDistList(distList):
    freespace = []
    for list in distList:
        freespace.append(min(x for x in list if x > 0))
    return freespace

# calculates value of map with a freespace list
def valueOfMapFast(houseList, freespaceList):
    mapTotal = 0
    for i in range(len(houseList) - 4):
        mapTotal += calculateValue(houseList[i + 4], freespaceList[i])
    return mapTotal

# updates the distances from the moved house to other all other houses
def update_dist_list(houseList, dist_list, houseIndex):
    new = []
    change_list = dist_list[houseIndex]
    for i in range(len(change_list)):
        if i == houseIndex:
            new.append(0)
        else:
            distance = houseList[houseIndex + 4].distanceTo(houseList[i + 4])
            new.append(distance)
            dist_list[i][houseIndex] = distance
    dist_list[houseIndex] = new
    return dist_list

# Berekend de afstand tussen twee punten. De input zijn twee lijsten met beiden twee ints.
def dist(point1, point2):
    height = point1[0] - point2[0]
    width = point1[1] - point2[1]
    return math.sqrt(math.pow(abs(height), 2) + math.pow(abs(width), 2))

def shortestPointPair(h1, h2):
    l1 = [[h1.x, h1.y], [h1.x + h1.width, h1.y], [h1.x + h1.width, h1.y + h1.height], [h1.x, h1.y + h1.height]]
    l2 = [[h2.x + h2.width, h2.y + h2.height], [h2.x, h2.y + h2.height], [h2.x, h2.y], [h2.x + h2.width, h2.y]]
    min = dist(l1[0], l2[0])
    for i in range(1,4):
        if dist(l1[i], l2[i]) < min:
            min = dist(l1[i], l2[i])
    return min

def shortestPointPair2(h1, h2):
    if h1.x > h2.x + h2.width and h1.y > h2.y + h2.height:
        return dist([h1.x, h1.y],[h2.x + h2.width,h2.y + h2.height])
    elif h1.x + h1.width < h2.x and h1.y > h2.y + h2.height:
        return dist([h1.x + h1.width, h1.y], [h2.x, h2.y + h2.height])
    elif h1.x + h1.width < h2.x and h1.y + h1.height < h2.y:
        return dist([h1.x + h1.width, h1.y + h1.height], [h2.x, h2.y])
    else:
        return dist([h1.x, h1.y + h1.height], [h2.x + h2.width, h2.y])

def minDistanceBetween(h1, h2):
    return min(distanceBetween(h1, h2), distanceBetween(h2, h1))

def distanceBetween(h1, h2):
    if (h2.x >= h1.x and h2.x <= h1.x + h1.width) or (h2.x + h2.width >= h1.x and h2.x + h2.width <= h1.x + h1.width):
        if h2.y < h1.y:
            return h1.y - (h2.y + h2.height)
        else:
            return h2.y - (h1.y + h1.height)
    elif (h2.y >= h1.y and h2.y <= h1.y + h1.height) or (h2.y + h2.height >= h1.y and h2.y + h2.height <= h1.y + h1.height):
        if h2.x < h1.x:
            return h1.x - (h2.x + h2.width)
        else:
            return h2.x - (h1.x + h1.width)
    else:
        return shortestPointPair(h1, h2)

# berekent de afstand tussen alle huizen en stopt deze in een lijst
def distToAll(houseList):
    distList = []
    finalList = []
    for i in range(len(houseList)):
        for j in range(len(houseList)):
            dist = houseList[i].distanceTo(houseList[j])
            if dist > 0:
                distList.append(dist)
        finalList.append(min(distList))
        distList = []
    return finalList

def valueOfMapFast(houseList, distList):
    freespace = ['w','w','w','w']
    length = len(houseList)
    freespace.extend([min(x for x in distList[index] if x > 0) for index in range(4, length)])
    mapTotal = 0
    for i in range(4, length):
        mapTotal += calculateValue(houseList[i], freespace[i])
    return mapTotal

def update_dist_list(houseList, dist_list, houseIndex):
    new = []
    change_list = dist_list[houseIndex]
    for i in range(len(change_list)):
        if i == houseIndex:
            new.append(0)
        else:
            distance = houseList[houseIndex].distanceTo(houseList[i])
            new.append(distance)
            dist_list[i][houseIndex] = distance
    dist_list[houseIndex] = new
    #print(dist_list)
    return dist_list

def updateDistList(houseList, distList, house):
    checkList = distList[house]
    for i in range(len(checkList)):
        if i == house:
            distList[house][i] = 0
        else:
            length = houseList[house].distanceTo(houseList[i])
            distList[house][i] = length
            distList[i][house] = length
    return distList

def valueOfMap(houseList):
    houseList = houseList[4:]
    value = 0
    i = 0
    freespace = distToAll(houseList)
    for house in houseList:
        free = freespace[i]
        if house.freespace == 6:
           value += calculateValue(house, free)
        elif house.freespace == 3:
            value += calculateValue(house, free)
        elif house.freespace == 2:
            value += calculateValue(house, free)
        i += 1
    return value


def calculateValue(house, free):
    houseVal = house.value
    addedVal = (house.percentage * math.floor(free - house.freespace)) * houseVal
    houseValue = houseVal + addedVal
    return houseValue



""" check hoeveel van welke huizen op de map staan, check de hoeveelheid vrijstand
    per huis. herbereken de waardes van het huis en tel bij elkaar op.
"""

"""
    houseToComp = houseList[houseNum]
    houseList.remove(houseList[houseNum])
    min = houseToComp.distanceTo(houseList[-1])
    print(min)
    print(houseNum, "house19", houseList[-1])
    for i in range(len(houseList) - 1):
        x = houseToComp.distanceTo(houseList[i])
        if x < min:
            min = x
    return min

def closestTo2(houseList, houseNum):
    print (houseList[houseNum])
    print(houseList[houseNum].x, houseList[houseNum].y)
    houseToComp = houseList[houseNum]
    houseList.remove(houseList[houseNum])
    min = houseToComp.distanceTo(houseList[-1])
    for i in range(len(houseList) - 1):
        x = houseToComp.distanceTo(houseList[i])
        if x < min:
            min = x
    return min
"""
def inWater(houseList):
    h1 = houseList[-1]
    for i in range(4):
        water = houseList[i]
        if h1.distanceTo(water) < 0:
            return True
    return False

def checkOverlap(houseList):
    if inWater(houseList):
        return True
    h1 = houseList[-1]
    for i in range(4, (len(houseList) - 1)):
        h2 = houseList[i]
        if h1.distanceTo(h2) < h1.freespace or h1.distanceTo(h2) < h2.freespace:
            return True
    return False

def checkOverlapMap(houseList):
    for i in range(len(houseList)):
        print("lengte huislijst", len(houseList))
        if checkOverlap(houseList[:i]):
            print("overlap")
            return True
        if inWater(houseList[:i]):
            return True
    return False

def inRange(h1, h2):
    if abs(h1.x  - h2.x) < h1.freespace + h1.width:
        return True
    elif abs(h1.y - h2.y) < h1.freespace+ h1.height:
        return True
    return False

def isMapInvalid(houseList):
    if inWater(houseList):
        return True
    h1 = houseList[-1]
    for i in range(4, (len(houseList) - 1)):
        h2 = houseList[i]
        if inRange(h1, h2):
            if h1.distanceTo(h2) < h1.freespace or h1.distanceTo(h2) < h2.freespace:
                return True
    return False

def overlapFinalBoss(houseList):
    counter = 0
    houseList = houseList[::-1]
    for i in range(len(houseList)):
        h1 = houseList[i]
        houseList.pop(i)
        for j in range(len(houseList)):
            skip = False
            counter += 1
            h2 = houseList[j]
            if h1.freespace == 0 or h2.freespace == 0:
                skip = True
                if h1.freespace == 0:
                    if h1.distanceTo(h2) < 0:
                        return True
            if (h1.distanceTo(h2) < h1.freespace or h1.distanceTo(h2) < h2.freespace) and not skip:
                return True
        houseList.insert(i, h1)
    return False

def overlapFinalBoss2(houseList):
    for i in range(4, (len(houseList))):
        if isMapInvalid(houseList[:i]):
            return True
    return False

def placeWater1():
    list = []
    list.append(Water(17, 17, 38, 38, 1))
    list.append(Water(105, 17, 38, 38, 1))
    list.append(Water(17, 125, 38, 38, 1))
    list.append(Water(105, 125, 38, 38, 1))
    return list

def placeWater2():
    list = []
    list.append(Water(42,52,76,76,1))
    list.append(Water(0,0,0,0,1))
    list.append(Water(0,0,0,0,1))
    list.append(Water(0,0,0,0,1))
    return list

def placeMaison(list):
    x = random.randint(6, 143)
    y = random.randint(6, 163)
    maison = Maison(x, y)
    list.append(maison)
    return maison

def placeBungalow(list):
    x = random.randint(3, 147)
    y = random.randint(3, 167)
    bungalow = Bungalow(x, y)
    list.append(bungalow)
    return bungalow

def placeSingle(list):
    x = random.randint(2, 150)
    y = random.randint(2, 170)
    singleHouse = SingleHouse(x,y)
    list.append(singleHouse)
    return singleHouse

# Plaatst maisons in de hoeken, returnd hoeveel maisons er hierna nog geplaatst moeten worden
def cornerMaisons(numberOfMaisons, houseList):
    houseList.append(Maison(6, 6))
    houseList.append(Maison(143, 163.5))
    houseList.append(Maison(143, 6))
    if numberOfMaisons == 3:
        return 0
    houseList.append(Maison(6, 163.5))
    if numberOfMaisons == 6:
        return 2
    else:
        return 5

# Eerste argument is het aantal te plaatsen huizen
# Tweede argument is de plaatsing van het water. Mogelijkheden zijn 1 of 2.
# Derde (optionele) argument bepaald of de maisons zoveel mogelijk in de hoek worden geplaatst.
def makeMap(goal,waterTactic,corner=True):
    while True:
        # Setup
        numberOfMaisons = int(0.15*goal)
        numberOfBungalows = int(0.25*goal)
        numberOfSingles = int(0.6*goal)
        if waterTactic == 1:
            houseList = placeWater1()
        elif waterTactic == 2:
            houseList = placeWater2()
        if corner:
            numberOfMaisons = cornerMaisons(numberOfMaisons, houseList)
        # Plaatsing huizen:
        while numberOfMaisons != 0:
            maison = placeMaison(houseList)
            if isMapInvalid(houseList) == True:
                houseList.remove(maison)
                continue
            numberOfMaisons -= 1
        while numberOfBungalows != 0:
            bungalow = placeBungalow(houseList)
            if isMapInvalid(houseList) == True:
                houseList.remove(bungalow)
                continue
            numberOfBungalows -= 1
        while numberOfSingles != 0:
            single = placeSingle(houseList)
            if isMapInvalid(houseList) == True:
                houseList.remove(single)
                continue
            numberOfSingles -= 1
        return houseList


def placeMaisonConstraint1(houseList, numberOfMaisons):
    houseList.append(Maison(6, 6))
    houseList.append(Maison(143, 163.5))
    houseList.append(Maison(143, 6))
    if numberOfMaisons == 3:
        return 0
    houseList.append(Maison(6, 163.5))
    houseList.append(Maison(6, (180/2)))
    houseList.append(Maison(143, (180/2)))
    if numberOfMaisons == 6:
        return 2
    if numberOfMaisons == 9:
        houseList.append(Maison(74.5, 6))
        houseList.append(Maison((160/2) - (11/2), (180 / 2)))
        houseList.append(Maison(74.5, 163.5))
    else:
        return 5

def placeMaisonConstraint2(houseList, numberOfMaisons):
    houseList.append(Maison(6, 6))
    houseList.append(Maison(143, 163.5))
    houseList.append(Maison(143, 6))
    if numberOfMaisons == 3:
        return 0
    houseList.append(Maison(6, 163.5))
    houseList.append(Maison(6, (180/2)))
    houseList.append(Maison(143, (180/2)))
    if numberOfMaisons == 6:
        return 2
    if numberOfMaisons == 9:
        houseList.append(Maison(74.5, 6))
        houseList.append(Maison((160/2) - (11/2), (180 / 2)))
        houseList.append(Maison(74.5, 163.5))
    else:
        return 5


def makeMapConstraint(goal, waterTactic):

    while True:
        # Setup
        numberOfMaisons = int(0.15*goal)
        numberOfBungalows = int(0.25*goal)
        numberOfSingles = int(0.6*goal)
        if waterTactic == 1:
            houseList = placeWater1()
        elif waterTactic == 2:
            houseList = placeWater2()
        placeMaisonConstraint1(houseList, numberOfMaisons)
        """"
        while numberOfMaisons != 0:
            maison = placeMaisonConstraint(houseList)
            if checkOverlap(houseList) == True:
                houseList.remove(maison)
                continue
            numberOfMaisons -= 1
        while numberOfBungalows != 0:
            bungalow = placeBungalow(houseList)
            if checkOverlap(houseList) == True:
                houseList.remove(bungalow)
                continuex
            numberOfBungalows -= 1
        