import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data_gen_svm.csv', header=None)

X = dataset.iloc[:, 1:31].values
y = dataset.iloc[:, 0].values

rows = X.shape[0]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
