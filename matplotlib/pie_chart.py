from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [120, 80]
labels = ['Sixty', 'Forty']

colors = ['blue', 'yellow']

plt.pie(slices, labels=labels, colors=colors,
        wedgeprops={'edgecolor': 'black'})

plt.title("My Pie Chart")
plt.tight_layout()
plt.show()
