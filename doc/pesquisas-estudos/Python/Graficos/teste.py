import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5, 6, 7, 8]

# heights of bars
height = [67733089.88, 69018743.43, 80916419.53, 82128786.04, 67733089.88, 69018743.43, 80916419.53, 82128786.04]

# labels for bars
tick_label = ['2019', '2020', '2021', '2022', '2019', '2020', '2021', '2022']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red', 'green', 'yellow', 'purple'])

# naming the x-axis
plt.xlabel('ano')
# naming the y-axis
plt.ylabel('quantidade')
# plot title
plt.title('primeiro teste')

# function to show the plot
plt.show()
