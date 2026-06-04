import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

plt.style.use("fivethirtyeight")

df = pd.read_csv('data0.csv')

df.columns = ['ID', 'Languages']

ids = df['ID']
languages = df['Languages']

lang_counter = Counter()

for language in languages:
    lang_counter.update(language.split(';'))

lang_axis = []
popularity_axis = []

for item in lang_counter.most_common(15):
    lang_axis.append(item[0])
    popularity_axis.append(item[1])

lang_axis.reverse()
popularity_axis.reverse()

total = sum(popularity_axis)
percent = []

for item in popularity_axis:
    percent.append(('{}%'.format(item / total * 100)))


bars = plt.barh(lang_axis, popularity_axis)

plt.bar_label(bars, labels=percent, fontsize=8, weight='bold', zorder=3)

plt.title("Popularity of Languages")
plt.xlabel("Popularity")


plt.show()
