import matplotlib.pyplot as plt
import Class
import Canvas
import Hillclimber

#plt.xlim(1, len(x))

def boxPlot(runs):
    mapValues = Canvas.mapStats(runs)[0]
    #x = list(range(runs))
    plt.title("Boxplot of %i random sampled maps" % (runs))
    plt.ylabel("Value of Map")
    #plt.yscale("log")
    plt.boxplot(mapValues)
    plt.show()



def lineGraph(mapValues):
  #  numOfIter = ...

    plt.title("Graph of %i iterations with hillclimber" % (len(mapValues)))
    plt.ylabel("Value of Map")
    plt.xlabel("Number of Iterations")
    plt.xlim(0, len(mapValues))
    plt.plot(range(len(mapValues)), mapValues)
    plt.show()




