from tkinter import *
import tkinter
import Class
import Canvas
import Hillclimber
import Graphs

p = Class.makeMap(40, 1, True)
dist_list = Class.initDistList(p)



new_dist_list = Class.update_dist_list(p, dist_list, 1)

freespace = Class.freespaceFromDistList(dist_list)
new_freespace = Class.freespaceFromDistList(new_dist_list)

print(Class.valueOfMapFast(p, freespace))
print(Class.valueOfMapFast(p, new_freespace))
print(freespace == new_freespace)
print(dist_list == new_dist_list)

houseList = Class.makeMap(20, 1)
distList = Class.initDistList(houseList)
freespacelist = Class.freespaceFromDistList(distList)
print(Class.valueOfMapFast(houseList, freespacelist))
distList2 = Class.update_dist_list(houseList, distList, 1)
freespacelist2 = Class.freespaceFromDistList(distList2)
print(Class.valueOfMapFast(houseList, freespacelist2))
print(distList == distList2)

print(freespacelist == freespacelist2)
print(freespacelist)
print(freespacelist2)
