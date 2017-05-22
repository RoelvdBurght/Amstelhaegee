# berekent de afstand tussen alle huizen en stopt deze in een lijst
# en returned een lijst met freespace
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

# calculates value of map with houselist
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

def initDistList2(houseList):
    length = len(houseList)-4
    distList = [[0 for x in range(length)] for y in range(length)]
    for i in range(length):
        for j in range(length):
            #isWater = False
            #if houseList[i].freespace == 0:
                #isWater = True
                #distList[i][j] = "w"
            #if houseList[j].freespace == 0:
            #    isWater = True
            sameHouse = False
            if i == j:
                sameHouse = True
                distList[i][j] = 0
            if not isWater and not sameHouse:
                if distanceBetween(houseList[i],houseList[j]) == 0.5:
                    print(distanceBetween(houseList[i],houseList[j]))
                    print(houseList[i])
                    print(houseList[j])
                distList[i][j] = distanceBetween(houseList[i],houseList[j])
    test = []
    for list in distList[4:]:
        test.append(min(x for x in list if x > 0))
    print(test)
    return distList