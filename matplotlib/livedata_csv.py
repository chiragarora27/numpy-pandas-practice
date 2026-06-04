# livedata in csv is changing through a python script which is run on console simultaneously


import pandas as pd
from matplotlib.animation import FuncAnimation
import random
import matplotlib.pyplot as plt


def animate(i):
    data = pd.read_csv('data.csv')

    x_value = data['x_value']
    total_1 = data['total_1']
    total_2 = data['total_2']

    plt.cla()

    plt.plot(x_value, total_1, label='Channel 1')
    plt.plot(x_value, total_2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, 1000)

plt.show()
