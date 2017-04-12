import math
import random
#random.seed(1234)


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

def minDistanceBetween(h1,h2):
    return min(distanceBetween(h1,h2), distanceBetween(h2,h1))

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

def closestTo(houseList, houseNum):
    print (houseList[houseNum])
    houseToComp = houseList[houseNum]
    houseList.remove(houseList[houseNum])
    min = houseToComp.distanceTo(houseList[-1])
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

def checkOverlap(houseList):
    h1 = houseList[-1]
    for i in range(len(houseList) - 1):
        h2 = houseList[i]
        if h1.distanceTo(h2) < h1.freespace or h1.distanceTo(h2) < h2.freespace:
            return True
    return False

def placeMaison(list):
    x = random.randint(6, 149)
    y = random.randint(6, 169)
    maison = Maison(x,y)
    list.append(maison)
    return maison

def placeBungalow(list):
    x = random.randint(3, 150)
    y = random.randint(3, 172)
    bungalow = Bungalow(x,y)
    list.append(bungalow)
    return bungalow

def placeSingle(list):
    x = random.randint(2, 152)
    y = random.randint(2, 172)
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
