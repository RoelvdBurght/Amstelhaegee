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

def shortestPointPair(h1, h2):
    l1 = [[h1.x, h1.y], [h1.x + h1.width, h1.y], [h1.x + h1.width, h1.y + h1.height], [h1.x, h1.y + h1.height]]
    l2 = [[h2.x + h2.width, h2.y + h2.height], [h2.x, h2.y + h2.height], [h2.x, h2.y], [h2.x + h2.width, h2.y]]
    min = dist(l1[0], l2[0])
    for i in range(1,4):
        if dist(l1[i], l2[i]) < min:
            min = dist(l1[i], l2[i])
    return min

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

def checkOverlap(list):
    for i in list[:-1]:
        h1 = list[-1]
        h2 = i
       #print(h1.distanceTo(h2), "distance TO")
        if h1.distanceTo(h2) < h1.freespace or h1.distanceTo(h2) < h2.freespace:
            return False
        return True

def placeMaison(list):
    x = random.randint(0, 149)
    y = random.randint(0, 149)
    list.append(Maison(x,y))

def placeBungalow(list):
    x = random.randint(0, 150)
    y = random.randint(0, 152)
    list.append(Bungalow(x,y))


def placeSingle(list):
    x = random.randint(0, 152)
    y = random.randint(0, 152)
    list.append(SingleHouse(x,y))

def makeMap(goal):
    while True:
        numberOfMaisons = int(0.15*goal)
        numberOfBungalows = int(0.25*goal)
        numberOfSingles = int(0.6*goal)
        houseList = []
        for i in range(numberOfMaisons):
            placeMaison(houseList)
            if checkOverlap(houseList) == False:
                continue
        for i in range(numberOfBungalows):
            placeBungalow(houseList)
            if checkOverlap(houseList) == False:
                continue
        for i in range(numberOfSingles):
            placeSingle(houseList)
            if checkOverlap(houseList) == False:
                continue
        return houseList
