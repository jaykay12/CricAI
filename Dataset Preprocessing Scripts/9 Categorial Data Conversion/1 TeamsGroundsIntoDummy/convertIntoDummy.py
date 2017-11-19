#This script segregates the categorial data of teams A, team B & Grounds into dummy variables

import pandas as pd

match_data = pd.read_csv('dataset.csv')
new_data = match_data[['Team 1','Team 2','Ground']].copy()
feature_cols = list(new_data.columns[0:3])

print("Feature columns:\n{}".format(feature_cols))

X_all = match_data[feature_cols]

def convert_intoDummyTeams(X):
	output = pd.DataFrame(index = X.index)

	for col,col_data in X.iteritems():
		if col_data.dtype == object:
			col_data = pd.get_dummies(col_data,prefix = col)
		output = output.join(col_data)
	return output

X_all = convert_intoDummyTeams(X_all)

print("Processed Feature columns:\n{}".format(list(X_all.columns)))

NewDF = pd.DataFrame(index = match_data.index)
NewDF = NewDF.join(X_all)

print(NewDF.head())

oldDF = match_data[['Margin','Venue','Winner']]

NewDF = NewDF.join(oldDF)

print(NewDF.head())

NewDF.to_csv('dataset_TeamsGrounds_IntoDummies.csv',index=False)
