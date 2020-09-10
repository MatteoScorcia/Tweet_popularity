import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm

data = pd.read_csv('../dataset/dataset.csv')

plt1 = plt
plt1.style.use("seaborn")
plt.style.use("seaborn")

#Retweet distribution plot
freq = data['retweet_count'].value_counts()

y = freq.values.tolist()
x = freq.index.tolist()

plt1.xlabel('Numero di Retweet', color='black', size=15)
plt1.ylabel('Frequenza (Log)', color='black', size=15)
plt1.bar(x,y)
plt1.show()

set_color = cm.get_cmap('Set3', 11)

mean = data[['screen_name', 'retweet_count']].groupby(['screen_name']).mean().round(0).sort_values('retweet_count')
x = []
for element in mean.values:
    x.append(int(element))

ordered_names = mean.index.tolist()
print(ordered_names)
ordered_values = []

count = data['screen_name'].value_counts()
print(count)

for index in range(0, len(ordered_names)):
    for i, element in enumerate(count.index.tolist()):
        if ordered_names[index] == element:
            ordered_values.append(count.values[i])
            
fig, axes = plt.subplots(1, 2)
axes[0].set(ylabel='Numero di Retweet')
axes[0].set_xticklabels(ordered_names, rotation=65)
axes[0].bar(ordered_names, ordered_values, color=set_color.colors)
axes[1].set(ylabel='Media di Retweet')
axes[1].set_xticklabels(mean.index, rotation=65)
axes[1].bar(mean.index, height=x, color=set_color.colors)

plt.show()