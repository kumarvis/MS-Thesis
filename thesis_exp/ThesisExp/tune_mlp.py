import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

dataset = pd.read_csv('data_gen_svm.csv', header=None)

X = dataset.iloc[:, 1:31].values
y = dataset.iloc[:, 0].values

rows = X.shape[0]

#y = y.reshape(rows, 1)

#lbls_arr = lbls_arr.reshape((len(lbls), 1))


def calculate_accuracy(classifier, test_X, test_y, train_X, train_y):
    '''this func calculate and returns the train & training accuracy'''
    # for training
    prob_train = classifier.predict_proba(train_X)
    prob_train_max = prob_train.argmax(axis=1)
    ##success_vector_train = (train_y.values.argmax(axis=1) == prob_train_max)
    success_vector_train = (train_y == prob_train_max)
    success_int_vector_train = success_vector_train.astype(int)
    train_accuracy = (success_int_vector_train.sum() / success_int_vector_train.__len__()) * 100

    # for testing
    prob_test = classifier.predict_proba(test_X)
    prob_test_max = prob_test.argmax(axis=1)
    ##success_vector_test = (test_y.values.argmax(axis=1) == prob_test_max)
    success_vector_test = (test_y == prob_test_max)
    success_int_vector_test = success_vector_test.astype(int)
    test_accuracy = (success_int_vector_test.sum() / success_int_vector_test.__len__()) * 100
    print("Training set score: %f" % train_accuracy)
    print("Test set score: %f" % test_accuracy)
    return train_accuracy, test_accuracy

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


classifier = MLPClassifier(solver="adam", verbose=True, early_stopping=False, max_iter=2000)
llst_train_test_acc_hl1 = []

max_no_neuro = 30
for no_of_neurons in range(6, max_no_neuro, 2):
    print('No_Neaurons = ', no_of_neurons)
    classifier.hidden_layer_sizes = (no_of_neurons, )
    classifier.activation = "relu"
    lst_lr = [0.1, 0.01, 0.005, 0.001, .00001]
    for lr in lst_lr:
        classifier.learning_rate_init = lr

        # fit the model
        classifier.fit(X_train, y_train)

        # for calculating accuracy manually
        print('\n------------------------accuracies for ' + str(no_of_neurons) + ' neurons----------------------------\n')
        train_accuracy, test_accuracy = calculate_accuracy(classifier, X_test, y_test, X_train, y_train)
        llst_train_test_acc_hl1.append([no_of_neurons, lr, train_accuracy, test_accuracy])


import csv
f = open('train_test_accuracy_hl01.csv', 'w')
writer = csv.writer(f, delimiter=' ')
for list_train_test_acc in llst_train_test_acc_hl1:
    writer.writerow(list_train_test_acc)
f.close()


llst_train_test_acc_hl2 = []
for no_of_neurons_hl1 in range(6, max_no_neuro, 2):
    for no_of_neurons_hl2 in range(4, max_no_neuro, 2):
        print('No_Neaurons = ', no_of_neurons)
        classifier.hidden_layer_sizes = (no_of_neurons_hl1, no_of_neurons_hl2)
        classifier.activation = "relu"
        lst_lr = [0.1, 0.01, 0.005, 0.001, .00001]
        for lr in lst_lr:
            classifier.learning_rate_init = lr

            # fit the model
            classifier.fit(X_train, y_train)

            # for calculating accuracy manually
            print('\n------------------------accuracies for ' + str(no_of_neurons) + ' neurons----------------------------\n')
            train_accuracy, test_accuracy = calculate_accuracy(classifier, X_test, y_test, X_train, y_train)
            llst_train_test_acc_hl2.append([no_of_neurons_hl1, no_of_neurons_hl2, lr, train_accuracy, test_accuracy])


import csv
f = open('train_test_accuracy_hl02.csv', 'w')
writer = csv.writer(f, delimiter=' ')
for list_train_test_acc in llst_train_test_acc_hl2:
    writer.writerow(list_train_test_acc)
f.close()
