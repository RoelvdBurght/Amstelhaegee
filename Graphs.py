import matplotlib.pyplot as plt
import Class
import Canvas

numbOfMaps = 40
x = list(range(numbOfMaps))

mapValues = Canvas.mapStats(numbOfMaps)[0]
#plt.plot(range, mapValues)
plt.xlabel("Number of Maps")
plt.ylabel("Value of Map")

#plt.show()
