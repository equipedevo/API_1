import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrame = pd.read_csv("./São José dos Campos.csv")

labels = []
for l in range(0, len(dataFrame.values), 13):
    labels.append(dataFrame.values[l][0])
print(labels)

heights = {}
for i in range(1, 4):
    values = []
    for j in range(0, len(dataFrame.values), 13):
        values.append(dataFrame.values[j][i] / 1000)
    heights.update({
        dataFrame.columns[i]:
        np.array(values)
    })
print(heights)

fig, ax = plt.subplots()
bottom = np.zeros(len(labels))

for name, height in heights.items():
    p = ax.bar(labels, height, 0.5, label=name, bottom=bottom)
    bottom += height

    ax.bar_label(p, label_type="center")

ax.set_title("Quantidade de Procedimentos em SJC de 2019 a 2022")
ax.legend(loc="upper right")

plt.show()
