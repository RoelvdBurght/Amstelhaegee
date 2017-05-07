import matplotlib.pyplot as plt
import Class
import Canvas




#plt.xlim(1, len(x))


def boxPlot(runs):
    mapValues = Canvas.mapStats(runs)[0]
    #x = list(range(runs))
    plt.title("Boxplot of %i random sampled maps" % (runs))
    plt.ylabel("Value of Map")
    #plt.yscale("log")
    plt.boxplot(mapValues)
    plt.show()

def lineGraph():
  #  numOfIter = ...
    mapValues = hillclimber.getListWithValus(x)
    plt.title("Graph of n iterations with Hilclimber")
    plt.ylabel("Value of Map")
    plt.xlabel("Number of Iterations")
    plt.xlim(1, len(x))
    plt.plot(list(x), mapValues)