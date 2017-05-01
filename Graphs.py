import matplotlib.pyplot as plt
import Class
import Canvas

numbOfMaps = 20
x = list(range(numbOfMaps))

mapValues = Canvas.mapStats(numbOfMaps)[0]

data_to_plot = mapValues


plt.boxplot(data_to_plot)
plt.title("Boxplot of %i random sampled maps"%(numbOfMaps))

plt.ylabel("Value of Map")
plt.show()