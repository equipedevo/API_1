import matplotlib.pyplot as plt
import pandas as pd

import io

class Table :
    def __init__(self,
        title,
        xLabel, yLabel,
        tableDir,
        columns,
        lineStep,
        width,
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
        ):
        dataFrame = pd.read_csv(tableDir)

        height = []
        labels = []

        j = 0
        for i in range(0, len(dataFrame.values), lineStep):
            if j > columns:
                break
            j += 1

            labels.append(dataFrame.values[i][0])
            height.append(dataFrame.values[i][-1])
        
        plt.bar(range(1, columns+1), height, tick_label = labels, width = width, color = colors)

        plt.xlabel(xLabel)
        plt.ylabel(yLabel)

        plt.title(title)
    
    def SaveFig(self, path, name):
        plt.savefig(path+name) #'./static/img/graficoTeste.svg')