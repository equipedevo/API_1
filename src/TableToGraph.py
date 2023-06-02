import matplotlib.pyplot as pyplot
import numpy
import pandas
import os

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

def BarGraphFromDB(select, title, xLabel, yLabel, figDir):
    dataFrame = pandas.DataFrame(select)

    lines = []
    bars = []
    for val in dataFrame.values:
        lines.append(val[0])
        bars.append(val[1])

    fig = pyplot.figure(figsize = (10, 5))
    
    pyplot.bar(lines, bars, 0.75, 0.0)

    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.title(title)

    MakeFolder()

    pyplot.gcf().set_size_inches(10, 5)
    pyplot.tight_layout()
    pyplot.savefig(figDir)

def GroupedBarGraph(csvDir, title, barRange, lineRange, xLabel, yLabel, figDir, autoDivide = False, divisor = 1):
    dataFrame = ReadCSV(csvDir)

    lines = []
    for i in lineRange:
        lines.append(dataFrame.values[i][0][:3])

    largestValue = 0

    bars = {}
    for i in barRange:
        values = []
        for j in lineRange:
            value = 0
            try:
                value = float(dataFrame.values[j][int(i)+1])
            except:
                value = 0
            
            if value > largestValue:
                largestValue = value

            values.append(value)
        bars.update({ dataFrame.columns[int(i)+1]: numpy.array(values) })

    autoDivideValue = 10 ** (len(str(int(largestValue))) - 3)
    if(autoDivideValue <= 100):
        autoDivideValue = 1

    x = numpy.arange(len(lines))
    width = 1 / (len(bars) + 1)
    multiplier = 0

    fig, axes = pyplot.subplots()

    for names, values in bars.items():
        offset = width * multiplier
        rects = axes.bar(x + offset, values / (autoDivideValue if autoDivide else divisor), width, label=names)
        axes.bar_label(rects)
        multiplier += 1

    axes.set_xlabel(xLabel)

    if autoDivide and autoDivideValue > 1:
        axes.set_ylabel(f"{yLabel} / {autoDivideValue}")
    elif divisor > 1:
        axes.set_ylabel(f"{yLabel} / {divisor}")
    else:
        axes.set_ylabel(yLabel)

    axes.set_title(title)
    axes.set_xticks(x if len(lines) == 1 else x + (width * (len(bars) - 1) / 2), lines)
    axes.legend(loc="upper right")
    axes.set_ymargin(0.2)

    MakeFolder()

    pyplot.gcf().set_size_inches(10, 5)
    pyplot.tight_layout()
    pyplot.savefig(figDir)

def PercentageLineGraph(csvDir, title, barRange, lineRange, xLabel, yLabel, figDir):
    dataFrame = ReadCSV(csvDir)

    lines = []
    for i in lineRange:
        lines.append(dataFrame.values[i][0][:3])

    total = []
    bars = {}
    for i in barRange:
        values = []
        total.append(float(dataFrame.values[lineRange[0]-1][int(i)+1]))
        for j in lineRange:
            value = 0
            try:
                value = float(dataFrame.values[j][int(i)+1])
            except:
                value = 0
            values.append(value)
        bars.update({ dataFrame.columns[int(i)+1]: numpy.array(values) })

    x = numpy.arange(len(lines))
    width = 1 / (len(bars) + 1)
    multiplier = 0

    fig, axes = pyplot.subplots()

    totalTick = 0
    for names, values in bars.items():
        width * multiplier
        axes.plot([float((x / total[totalTick]) * 100) for x in values], label=names)
        multiplier += 1
        totalTick += 1

    axes.set_xlabel(xLabel)
    axes.set_ylabel(yLabel)
    axes.set_title(title)
    axes.set_xticks(x, lines)
    axes.legend(loc='upper left')
    axes.set_ymargin(0.2)
    # axes.set_ylim(0, 120)

    MakeFolder()

    pyplot.gcf().set_size_inches(10, 5)
    pyplot.tight_layout()
    pyplot.savefig(figDir)

def ReadCSV(csvDir):
    try:
        return pandas.read_csv(csvDir, encoding="utf-8")
    except:
        raise Exception(f"Falha ao ler tabela: {csvDir}")

def MakeFolder():
    if not os.path.isdir("./static/graficos/"):
        os.makedirs("./static/graficos/")
