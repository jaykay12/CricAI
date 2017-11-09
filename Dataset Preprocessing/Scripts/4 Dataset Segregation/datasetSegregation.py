#This Script segregates the dataset columns into Target Column & Feature Columns

import pandas as pd

df = pd.read_csv('dataset.csv')
df.set_index('Scorecard',inplace=True)
newDF = df[['Team 1','Team 2','Margin','Ground','Match Date','Winner']]
newDF.to_csv('dataset_new.csv')
print("Dataset Segregated!")

match_data = pd.read_csv('dataset_new.csv')
feature_cols = list(match_data.columns[:-1])
target_col = match_data.columns[-1]

print("Feature columns:\n{}".format(feature_cols))
print("Target column:\n{}".format(target_col))
