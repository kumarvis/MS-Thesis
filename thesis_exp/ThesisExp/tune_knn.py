import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data_gen_svm.csv', header=None)

X = dataset.iloc[:, 1:31].values
y = dataset.iloc[:, 0].values

rows = X.shape[0]

#y = y.reshape(rows, 1)

#lbls_arr = lbls_arr.reshape((len(lbls), 1))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.neighbors import KNeighborsClassifier
error = []
for i in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))

plt.figure(figsize=(12, 6))
plt.plot(range(1, 10), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

print('dfd')