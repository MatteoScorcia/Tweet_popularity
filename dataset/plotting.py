from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('fivethirtyeight')

data = pd.read_csv('final_data.csv')

names = data.screen_name.unique()

df1 = data[data.screen_name == names[6]]

avg_retweets = df1.mean()[0]

plt.bar(df1.index, df1.retweet_count)
plt.axhline(avg_retweets, color='red', label='Mean', linewidth=2, linestyle='--')

plt.legend()
plt.title(f'Retweet Distribution: {names[6]}')
plt.xlabel('Tweet')
plt.ylabel('Number of Retweets')

plt.show()