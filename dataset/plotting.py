import pandas as pd

data = pd.read_csv('../dataset/mse.csv')

TP_mse = data.iloc[0][0]

RF_mses = data.iloc[1:11]

RF_list_temp = RF_mses.values.tolist()
RF_list = []

for element in  RF_list_temp:
    RF_list.append(element[0])
len(RF_list)

SVR_mses = data.iloc[11:21]

SVR_list_temp = SVR_mses.values.tolist()
SVR_list = []

for element in  SVR_list_temp:
    SVR_list.append(element[0])
len(SVR_list)

from matplotlib import pyplot as plt

x_axis = list(range(1, 11))

plt.plot(x_axis, RF_list, c = 'blue', alpha = 0.5, marker = '.', label = 'RF')
plt.plot(x_axis, SVR_list, c = 'red', alpha = 0.5, marker = '.', label = 'SVM')

plt.axhline(TP_mse, color='green', label='Trivial Predictor', linewidth=2, linestyle='--')
plt.axhline(sum(RF_list) / len(RF_list), color='blue', label='RF MEAN', linewidth=2, linestyle='--')
plt.axhline(sum(SVR_list) / len(SVR_list), color='red', label='SVM MEAN', linewidth=2, linestyle='--')

plt.grid(color = '#D3D3D3', linestyle = 'solid')
plt.legend(loc = 'upper left')
plt.title('MSE through iterations', color='black')
plt.xlabel('Iteration', color='black')
plt.ylabel('MSE', color='black')

plt.show()