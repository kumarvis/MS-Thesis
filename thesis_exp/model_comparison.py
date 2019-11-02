from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
money = [24.0, 72.3, 84.7]


# def millions(x, pos):
#     'The two args are the value and tick position'
#     return 'Per Accuracy %1.1f%' % (x)
#
#
# formatter = FuncFormatter(millions)

fig, ax = plt.subplots()
#
plt.bar(x, money)
plt.xticks(x, ('kNN', 'Neural Networks', 'SVM'))

ax.set_ylabel('Accuracy')
ax.set_xlabel('ML Algorithms')
ax.xaxis.label.set_color('green')
ax.yaxis.label.set_color('green')

plt.show()