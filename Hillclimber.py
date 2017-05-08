import Class
import random

#krijgt een lijst binnen en swapt 2 huizen, houd geen rekening met overlap en dergelijke
def swapHouses(list1, goal):
    if goal == 20:
        a, b = 6, 23
    elif goal == 40:
        a, b = 7, 43
    elif goal == 60:
        a, b = 7, 63
    house1 = random.randint(a, b)
    house2 = random.randint(a, b)
    temph1x = list1[house1].x
    temph1y = list1[house1].y
    temph2x = list1[house2].x
    temph2y = list1[house2].y
    list1[house1].x = temph2x
    list1[house1].y = temph2y
    list1[house2].x = temph1x
    list1[house2].y = temph1y
    varList = [house1, temph1x, temph1y, house2, temph2x, temph2y]
    return(list1, varList)

#zet de huizen terug op hun oude plek als de swap niet voor verbetering zorgde
def swapHousesback(houseList, varList):
    house1 = varList[0]
    house2 = varList[3]
    houseList[house1].x = varList[1]
    houseList[house1].y = varList[2]
    houseList[house2].x = varList[4]
    houseList[house2].y = varList[5]
    return houseList

#Krijgt een lijst binnen en swapt duizend keer een huis, accepteert de verandering alleen als er prijstoename is
def houseSwapper(houseList, goal, itNR):
    counter = 0
    for i in range(itNR):
        oldValue = Class.valueOfMap(houseList)
        newList, varList = swapHouses(houseList, goal)
        newValue = Class.valueOfMap(newList)
        if (newValue > oldValue) and not Class.overlapFinalBoss(newList):
            counter += 1
            houseList = newList
        else:
            houseList = swapHousesback(houseList, varList)
    print(counter, "X geswapped")
    return houseList
## plaatst soms nog wat gedeeltelijk in het water en is niet compatible met waterstrat2



#Checkt of de coördinaten x en y voor een bepaald type huis buiten de kaart vallen
#Neemt als input een huis object en 2 nieuwe coördinaten
def checkHouseOutOfBounds(house, x, y):
    if (x - house.width) < 0 or (y - house.height) < 0 or (x + house.width) > 160 or (y + house.height) > 180:
        return True
    return False
"""
Neemt als input: houseList = de lijst met huizen
                 goal      = het aantal huizen op de kaart
                 itNR      = aantal keer dat er een poging tot verplaatsen gedaan wordt
                 changeNum = afwijking nieuwe coördinaten ten opzichte van oude

Deel 1 kiest een willekeurig huis uit de lijst om te verplaatsen,
afhankelijk van hoe groot de lijst is ivb hoekhuizen en water
Deel 2 kiest nieuwe X en Y coördinaten door changeNum af en op te tellen bij de huidige coördinaten
en binnen die range willekeurig iets te kiezen
Deel 3 evalueert of er winst wordt gemaakt met de verandering, het huis buiten de kaart valt of er overlap is
"""
def verplaatser(houseList, goal, itNR, changeNum):
    counter = 0
    winst = 0
    valueList = []
#--------------------1-------------------------#
    for i in range(itNR):
        oldValue = Class.valueOfMap(houseList)
        if goal == 20:
            house = random.randint(3, 20)
        elif goal == 40:
            house = random.randint(4, 40)
        elif goal == 60:
            house = random.randint(4, 60)
#--------------------2--------------------------#
        oldX = houseList[house].x
        oldY = houseList[house].y
        lowerX, higherX = (oldX - changeNum), (oldX + changeNum)
        lowerY, higherY = (oldY - changeNum), (oldY + changeNum)
        newX = random.randint(round(lowerX), round(higherX))
        newY = random.randint(round(lowerY), round(higherY))
#--------------------3--------------------------#
        if not checkHouseOutOfBounds(houseList[house], newX, newY):
            valueList.append(Class.valueOfMap(houseList))
            houseList[house].x = newX
            houseList[house].y = newY
            if Class.valueOfMap(houseList) > oldValue and not Class.overlapFinalBoss(houseList):
                winst += Class.valueOfMap(houseList) - oldValue
                counter += 1
            else:
                houseList[house].x = oldX
                houseList[house].y = oldY
    print("winst =", winst)
    print("NR verplaatsingen =", counter)
    return houseList, valueList