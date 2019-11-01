import pandas as pd
import random
random.seed(201)
import numpy as np

mu0, sigma0 = 0, 5 # 73
#mu0, sigma0 = 0, 50
mu1, sigma1 = 50, 0.5
mu2, sigma2 = 75, 0.5
mu3, sigma3 = 80, 0.5

no_samples_cls0, no_samples_cls1, no_samples_cls2, no_samples_cls3 = 200, 350, 280, 260

lbl_cls0 = [0] * no_samples_cls0
lbl_cls1 = [1] * no_samples_cls1
lbl_cls2 = [2] * no_samples_cls2
lbl_cls3 = [3] * no_samples_cls3

lbls = lbl_cls0 + lbl_cls1 + lbl_cls2 + lbl_cls3
lbls_arr = np.asarray(lbls)
lbls_arr = lbls_arr.reshape((len(lbls), 1))

samples_cls0 = np.random.normal(mu0, sigma0, (no_samples_cls0, 30))
samples_cls1 = np.random.normal(mu0, sigma0, (no_samples_cls1, 30))
samples_cls2 = np.random.normal(mu0, sigma0, (no_samples_cls2, 30))
samples_cls3 = np.random.normal(mu0, sigma0, (no_samples_cls3, 30))

norm_samples_cls0 = (samples_cls0 - samples_cls0.min(axis=0)) / (samples_cls0.max(axis=0) - samples_cls0.min(axis=0))
norm_samples_cls1 = (samples_cls1 - samples_cls1.min(axis=0)) / (samples_cls1.max(axis=0) - samples_cls1.min(axis=0))
norm_samples_cls2 = (samples_cls2 - samples_cls2.min(axis=0)) / (samples_cls2.max(axis=0) - samples_cls2.min(axis=0))
norm_samples_cls3 = (samples_cls3 - samples_cls3.min(axis=0)) / (samples_cls3.max(axis=0) - samples_cls3.min(axis=0))

norm_samples = np.concatenate((norm_samples_cls0, norm_samples_cls1, norm_samples_cls2, norm_samples_cls3), axis=0)
data = np.concatenate((lbls_arr, norm_samples), axis=1)

np.savetxt("data_gen.csv", data, delimiter=",")

print('exit')




