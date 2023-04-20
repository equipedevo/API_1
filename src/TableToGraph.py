import matplotlib.pyplot as plt
import pandas as pd

def TableToGraph(csvDir, title, bars, lineRange, xLabel, yLabel, figDir):
    dataFrame = pd.read_csv(csvDir)

    left = range(1, bars+1)

    height = []
    labels = []

    j = 0
    for i in lineRange:
        j += 1
        if j > bars:
            break
        labels.append(dataFrame.values[i][0])
        height.append(dataFrame.values[i][-1])

    colors = [
        '#fa0606',
        '#f8047e',
        '#fe05ff',
        '#870bf1',
        '#0003fe',
        '#0884f9',
        '#02faf9',
        '#03ff83',
        '#06fb04',
        '#7dff05',
        '#fcfb09',
        '#f98203']
    plt.bar(left, height, tick_label = labels, width = 0.75, color = colors)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    plt.title(title)

    plt.gcf().set_size_inches(10, 5)
    plt.tight_layout()
    plt.savefig(figDir)
