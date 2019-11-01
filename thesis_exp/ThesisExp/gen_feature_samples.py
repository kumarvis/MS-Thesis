import pandas as pd
import random
random.seed( 30 )

data = pd.read_csv("features_lbl.csv")

# Preview the first 5 lines of the loaded data
data_preview = data.head()

#data_sort = data.sort_values(data_preview.columns[0])

lst_cols_remove = [str(i) for i in range(1, 60,2)]


# Delete multiple columns from the dataframe
data_refined = data.drop(lst_cols_remove, axis=1)

df_ext_lbl0 = df_lbl0 = data_refined.loc[data_refined['0'] == 0]

df_ext_lbl1 = df_lbl1 = data_refined.loc[data_refined['0'] == 1]

df_ext_lbl2 = df_lbl2 = data_refined.loc[data_refined['0'] == 2]

df_ext_lbl3 = df_lbl3 = data_refined.loc[data_refined['0'] == 3]



no_random_sample = 6
lbl1, lbl2, lbl3 = 212, 103, 157
no_spl1, no_spl2, no_spl3 = df_lbl1.shape[0], df_lbl2.shape[0], df_lbl3.shape[0]

##label1
for ii in range (lbl1 - no_spl1 + 1):
    rand_ll = [random.randint(0, no_spl1-1) for i in range(no_random_sample)]
    df_rand = df_lbl1.iloc[rand_ll]
    df_rand_mean = df_rand.mean(axis=0)

    df_ext_lbl1 = df_ext_lbl1.append(df_rand_mean, ignore_index=True)

print(df_ext_lbl1.shape)

##label2
for ii in range (lbl2 - no_spl2 + 1):
    rand_ll = [random.randint(0, no_spl2-1) for i in range(no_random_sample)]
    df_rand = df_lbl2.iloc[rand_ll]
    df_rand_mean = df_rand.mean(axis=0)

    df_ext_lbl2 = df_ext_lbl2.append(df_rand_mean, ignore_index=True)

print(df_ext_lbl2.shape)

#label3
for ii in range (lbl3 - no_spl3 + 1):
    rand_ll = [random.randint(0, no_spl3-1) for i in range(no_random_sample)]
    df_rand = df_lbl3.iloc[rand_ll]
    df_rand_mean = df_rand.mean(axis=0)
    df_ext_lbl3 = df_ext_lbl3.append(df_rand_mean, ignore_index=True)

print(df_ext_lbl3.shape)

df_ext_lbl0 = df_ext_lbl0.append(df_ext_lbl1, ignore_index=True)
df_ext_lbl0 = df_ext_lbl0.append(df_ext_lbl2, ignore_index=True)
df_ext_lbl0 = df_ext_lbl0.append(df_ext_lbl3, ignore_index=True)

df_final = df_ext_lbl0

lst_header_name = [str(i) for i in range(0, 31,1)]

df_final.columns = lst_header_name

df_normalize = df_final.copy()
for feature_name in df_normalize:
    if feature_name == '0':
        continue
    max_value = df_final[feature_name].max()
    min_value = df_final[feature_name].min()
    df_normalize[feature_name] = (df_final[feature_name] - min_value) / (max_value - min_value)

df_normalize.to_csv('features_normalized_final.csv', index=False)

print('exit')