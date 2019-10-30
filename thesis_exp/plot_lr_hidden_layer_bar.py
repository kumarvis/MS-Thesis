import numpy as np
import matplotlib.pyplot as plt


hidden_layers_unit = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
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
plt.text(0.01, 9, r'learning rate =0.1', fontdict=font)

yvals = [6+1, 8+1, 10+1, 12+1, 14+1, 16+1, 18+1, 20+1, 22+1, 24+1, 26+1, 28+1]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [6-1, 8-1, 10-1, 12-1, 14-1, 16-1, 18-1, 20-1, 22-1, 24-1, 26-1, 28-1]
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