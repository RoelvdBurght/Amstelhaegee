import math
import random

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

"""
# deze doet de magic uit eindelijk, wel nog alleen voor 20 huizen
# haalt voor ieder huis de de korste afstand naar een volgend huis uit list
def closestTo(distList, houseList):
    length = len(houseList)
    for j in range(length):
        x = distList[:length - 1]
        minimum = min(x)
        freespace.append(minimum)
        print("vrijstand house", j, "=", minimum)
        del x[:(length -1)]
        del distList[:(length - 1)]
    print(freespace)
    return freespace
"""
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

def placeWater1():
    list = []
    list.append(Water(11, 11, 38, 38, 1))
    list.append(Water(111, 11, 38, 38, 1))
    list.append(Water(11, 131, 38, 38, 1))
    list.append(Water(111, 131, 38, 38, 1))
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

def cornerMaisons(numberOfMaisons, houseList):
    houseList.append(Maison(0, 0))
    houseList.append(Maison(149, 169.5))
    houseList.append(Maison(149, 0))
    if numberOfMaisons == 3:
        return 0
    houseList.append(Maison(0, 169.5))
    if numberOfMaisons == 6:
        return 2
    else:
        return 5

def makeMapRandomOrder(goal, waterTactic):

# Eerste argument is het aantal te plaatsen huizen
# Tweede argument is de plaatsing van het water. Mogelijkheden zijn 1 of 2.
# Derde (optionele) argument bepaald of de maisons zoveel mogelijk in de hoek worden geplaatst.
def makeMap(goal,waterTactic,corner=True, random=False):
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



        while numberOfMaisons != 0:
            maison = placeMaison(houseList)
            if checkOverlap(houseList) == True:
                houseList.remove(maison)
                continue
            numberOfMaisons -= 1
        while numberOfBungalows != 0:
            bungalow = placeBungalow(houseList)
            if checkOverlap(houseList) == True:
                houseList.remove(bungalow)
                continue
            numberOfBungalows -= 1
        while numberOfSingles != 0:
            single = placeSingle(houseList)
            if checkOverlap(houseList) == True:
                houseList.remove(single)
                continue
            numberOfSingles -= 1
        return houseList