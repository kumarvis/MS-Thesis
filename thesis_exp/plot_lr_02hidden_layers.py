import numpy as np
import matplotlib.pyplot as plt

def lr01_plot():
        hidden_layers_unit = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
        N = len(hidden_layers_unit)
        ind = np.arange(N)  # the x locations for the groups
        width = 0.27  # the width of the bars

        fig = plt.figure()
        ax = fig.add_subplot(111)

        font = {'family': 'serif',
                'color': 'darkred',
                'weight': 'normal',
                'size': 9,
                }
        #plt.text(4, 100, r'learning rate =0.1', fontdict=font)

        hidden_layers_unit = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
        yvals              = [73.8, 30.6, 72.3, 74.8, 71.5, 73.6, 72.3, 68.1, 66.8, 74.0, 71.2, 66.6, 29.1]
        zvals              = [45.0, 49.5, 55.1, 63.2, 68.9, 70.1, 69.2, 70.3, 68.9, 71.0, 70.3, 69.9]
        rects1 = ax.bar(ind, yvals, width, color='r')
        # zvals = [37.0,38.5,40.0,37.5,40.0,43.75,42.75,46.5,44.25,36.25,41.5,40.5]
        rects2 = ax.bar(ind + width, zvals, width, color='g')

        ax.set_ylabel('Accuracy')
        ax.set_xlabel('Number of Hidden Units')
        ax.set_xticks(ind + width)
        ax.set_xticklabels(tuple(hidden_layers_unit))
        ax.legend((rects1[0], rects2[0]), ('Train', 'Validation'))

        plt.show()

lr01_plot()