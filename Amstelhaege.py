from tkinter import *
import tkinter
import Class
import Canvas
import Hillclimber
import SA
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import math
import xlwt
import copy


def codeHouseList(houseList):
    codedHouselist = []
    for object in houseList:
        codedHouselist.append((object.x, object.y, object.width, object.height, object.freespace))
    return codedHouselist

def decodeHouseList(codedHouseList):
    houseList = []
    for tuple in codedHouseList:
        if tuple[4] == 0:
            houseList.append(Class.Water(tuple[0], tuple[1], tuple[2], tuple[3], 1))
        elif tuple[4] == 2:
            houseList.append(Class.SingleHouse(tuple[0], tuple[1]))
        elif tuple[4] == 3:
            houseList.append(Class.Bungalow(tuple[0], tuple[1]))
        elif tuple[4] == 6:
            houseList.append(Class.Maison(tuple[0], tuple[1]))
    return houseList

def decoder(houseList):
    decodedList = []
    for house in houseList:
        tempList = []
        tempList.extend((house.x, house.y, house.freespace, house.width, house.height))
        decodedList.append(tempList)
    return str(decodedList)

def encoder(decodedList):
    houseList = []
    for list in decodedList:
        if list[2] == 2:
            single = Class.SingleHouse(list[0],list[1])
            houseList.append(single)
        elif list[2] == 3:
            bunga = Class.Bungalow(list[0],list[1])
            houseList.append(bunga)
        elif list[2] == 6:
            maison = Class.Maison(list[0],list[1])
            houseList.append(maison)
        elif list[2] == 0:
            water = Class.Water(list[0], list[1], list[3], list[4], 0)
            houseList.append(water)
    return houseList

p = encoder([[17, 17, 0, 38, 38], [105, 17, 0, 38, 38], [17, 125, 0, 38, 38], [105, 125, 0, 38, 38], [6, 6, 6, 11, 10.5], [143, 163.5, 6, 11, 10.5], [143, 6, 6, 11, 10.5], [123, 100, 3, 10, 7.5], [20, 87, 3, 10, 7.5], [78, 163, 3, 10, 7.5], [90, 108, 3, 10, 7.5], [50, 105, 3, 10, 7.5], [76, 3, 2, 8, 8], [74, 38, 2, 8, 8], [46, 72, 2, 8, 8], [28, 106, 2, 8, 8], [76, 130, 2, 8, 8], [117, 76, 2, 8, 8], [77, 105, 2, 8, 8], [54, 83, 2, 8, 8], [91, 120, 2, 8, 8], [74, 72, 2, 8, 8], [6, 117, 2, 8, 8], [36, 166, 2, 8, 8]])
values, climbed = SA.SA(SA.exponentialCooling, 50000, 1000, p, 20, 10000, 20, True, True)
