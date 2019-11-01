import random
import numpy as np
from sklearn.datasets import make_gaussian_quantiles# Construct dataset

random.seed(7)

X1, y1 = make_gaussian_quantiles(cov=1.,
                                 n_samples=2000, n_features=30,
                                 n_classes=4, random_state=1)

y1 = y1.reshape((len(y1), 1))
data = np.concatenate((y1, X1), axis=1)
np.savetxt("data_gen_svm.csv", data, delimiter=",")

print('dfd')