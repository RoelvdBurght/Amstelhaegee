import math
import random

class House:
    def distanceTo(self, other):
        return distanceBetween(self, other)

class SingleHouse(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.value = 285000
        self.freespace = 2

class Bungalow(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 7.5
        self.value = 399000
        self.freespace = 3

class Maison(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 11
        self.height = 10.5
        self.value = 610000
        self.freespace = 6

# Shape 1 is a square, shape 2 is a circle
class Water:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

# Berekend de afstand tussen twee punten. De input zijn twee lijsten met beiden twee ints.
def dist(point1, point2):
    height = point1[0] - point2[0]
    width = point1[1] - point2[1]
    return math.sqrt(math.pow(abs(height), 2) + math.pow(abs(width), 2))

# Neemt de vier relevante hoekpunten van twee vierkanten en kijkt welk paar het dichts bij elkaar ligt
def shortestPointPair(h1, h2):
    l1 = [[h1.x, h1.y], [h1.x + h1.width, h1.y], [h1.x + h1.width, h1.y + h1.height], [h1.x, h1.y + h1.height]]
    l2 = [[h2.x + h2.width, h2.y + h2.height], [h2.x, h2.y + h2.height], [h2.x, h2.y], [h2.x + h2.width, h2.y]]
    min = dist(l1[0], l2[0])
    for i in range(1,4):
        if dist(l1[i], l2[i]) < min:
            min = dist(l1[i], l2[i])
    return min

# Rekent de kortste afstand uit tussen twee huizen
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

# Controleert of een kaart tot nu toe geldig is
def isMapValid(houseList):
def closestTo(houseList):
    closestHouses = []
    for j in range(len(houseList)):
        h1 = houseList[j]
        closest = h1.distanceTo(houseList[j])
        for i in range(len(houseList) - 1):
            x = h1.distanceTo(houseList[i])
            if x < closest:
                closest = x
                print(closest)
    return closest

def checkOverlap(houseList):
    h1 = houseList[-1]
    for i in range(len(houseList) - 1):
        h2 = houseList[i]
        if h1.distanceTo(h2) < h1.freespace or h1.distanceTo(h2) < h2.freespace:
            return False
        if overlap(h1, h2) or overlap(h2, h1):
            return False
    return True

def overlap(h1, h2):
    if h2.x + h2.width <= h1.x or h2.y + h2.height <= h1.y or h2.x >= h1.x + h1.width or h2.y >= h1.y + h1.height:
        return False
    return True

# Plaatst een maison in de lijst met alle huizen
def placeMaison(list):
    x = random.randint(0, 149)
    y = random.randint(0, 169)
    maison = Maison(x,y)
    list.append(maison)
    return maison

def placeBungalow(list):
    x = random.randint(0, 150)
    y = random.randint(0, 172)
    bungalow = Bungalow(x,y)
    list.append(bungalow)
    return bungalow


def placeSingle(list):
    x = random.randint(0, 152)
    y = random.randint(0, 172)
    singleHouse = SingleHouse(x,y)
    list.append(singleHouse)
    return singleHouse

def makeMap(goal):
    while True:
        numberOfMaisons = int(0.15*goal)
        numberOfBungalows = int(0.25*goal)
        numberOfSingles = int(0.6*goal)
        houseList = []
        while numberOfMaisons != 0:
            maison = placeMaison(houseList)
            if isMapValid(houseList) == False:
                houseList.remove(maison)
                continue
            numberOfMaisons -= 1
        while numberOfBungalows != 0:
            bungalow = placeBungalow(houseList)
            if isMapValid(houseList) == False:
                houseList.remove(bungalow)
                continue
            numberOfBungalows -= 1
        while numberOfSingles != 0:
            single = placeSingle(houseList)
            if isMapValid(houseList) == False:
                houseList.remove(single)
                continue
            numberOfSingles -= 1
        return houseList
