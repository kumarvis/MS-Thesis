import numpy as np
import matplotlib.pyplot as plt

hidden_layers_unit = [6,8,10,12,14,16,18,20,22,24,26,28]
N = len(hidden_layers_unit)
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 9,
        }
plt.text(4, 100, r'learning rate =0.1', fontdict=font)

hidden_layers_unit = [6,       8,       10,    12,     14,     16,      18,   20,   22,      24,     26,   28]
yvals              = [47.4375, 52.8125, 58.75, 65.125, 70.625, 75.4375, 81.0, 82.5, 86.8125, 85.125, 91.5, 90.875]
zvals              = [45.0,    49.5,    55.1,  63.2,   68.9,   70.1,    69.2, 70.3, 68.9,    71.0,  70.3,  69.9]
rects1 = ax.bar(ind, yvals, width, color='r')
#zvals = [37.0,38.5,40.0,37.5,40.0,43.75,42.75,46.5,44.25,36.25,41.5,40.5]
rects2 = ax.bar(ind+width, zvals, width, color='g')

ax.set_ylabel('Accuracy')
ax.set_xlabel('Number of Hidden Units')
ax.set_xticks(ind+width)
ax.set_xticklabels(tuple(hidden_layers_unit) )
ax.legend((rects1[0], rects2[0]), ('Train', 'Validation'))

# def autolabel(rects):
#     for rect in rects:
#         h = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
#                 ha='center', va='bottom')
#
# autolabel(rects1)
# autolabel(rects2)


plt.show()