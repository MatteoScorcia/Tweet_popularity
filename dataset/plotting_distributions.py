import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('../dataset/dataset.csv')


plt.style.use("seaborn")
plt.title('Publishing time distribution', color='black', size=15)
plt.xlabel('Tweet index', color='black', size=15)
plt.ylabel('Publishing time', color='black', size=15)
plt.scatter(data.index.tolist(), data['time'].tolist(), alpha=0.8, s=8)

for name in data.screen_name.unique():
    start = data[data.screen_name == name].index[0]
    plt.axvline(start, color='red', linewidth=2, linestyle='--')
    
start = data[data.screen_name == name].index[0]
plt.axvline(start, color='red', label='pages separator', linewidth=2, linestyle='--')
    
plt.legend(loc = 'best')
plt.show()


"""
plt.style.use("seaborn")
plt.title('Retweets distribution', color='black', size=15)
plt.xlabel('Tweet index', color='black', size=15)
plt.ylabel('Number of retweets', color='black', size=15)
plt.plot(data.index.tolist(), data['retweet_count'].tolist(), alpha=0.8)
plt.show()
"""