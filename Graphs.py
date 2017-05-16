import matplotlib.pyplot as plt
import Canvas
import Hillclimber
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import numpy as np

def boxPlot(data):
    #x = list(range(runs))
    plt.title("Boxplot of 100 random sampled maps")
    plt.ylabel("Value of Map")
    #plt.yscale("log")
    mpl_fig = plt.figure()
    ax = mpl_fig.add_subplot(111)

    ax.boxplot(data)

    plotly_fig = tls.mpl_to_plotly(mpl_fig)
    plot_url = py.plot(plotly_fig, 'mpl-multiple-boxplot')



def lineGraph(mapValues):
    trace = go.Scatter(
        x=list(range((len(mapValues)))),
        y=mapValues,
        mode='lines',
        name='lines'
    )
    data = [trace]

    py.plot(data, filename='basic-line')

    '''
    plt.xlim(0, len(mapValues))
    plt.plot(range(len(mapValues)), mapValues)
    plt.show()
    '''