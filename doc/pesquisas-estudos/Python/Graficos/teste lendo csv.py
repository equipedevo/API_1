import matplotlib.pyplot as plt
import pandas as pd

dataFrame = pd.read_csv("./São José dos Campos.csv")
print(dataFrame.columns)
print(len(dataFrame.index))

left = range(1, 5)

height = []

labels = []

for i in range(0, len(dataFrame.values), 13):
    labels.append(dataFrame.values[i][0])
    height.append(dataFrame.values[i][-1])

print(len(left))
print(len(height))
print(len(labels))

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
plt.bar(left, height, tick_label = labels, width = 0.8, color = colors)

plt.xlabel('ano')
plt.ylabel('quantidade')

plt.title('teste lendo csv')

plt.show()
