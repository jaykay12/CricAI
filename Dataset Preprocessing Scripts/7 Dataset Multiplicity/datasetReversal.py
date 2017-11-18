#This script Reverses the dataset, currently Team 1 & Team 2 are reorganised in same match as Team 2 & Team 1 respectively.

import pandas as pd

originalDF = pd.read_csv('dataset.csv')

reverseDF = pd.DataFrame(columns = ['Scorecard','Team 1','Team 2','Margin','Ground','Match Date','Winner'])

itr = 0
for i,row in originalDF.iterrows():
	reverseDF.loc[itr] = [row['Scorecard'],row['Team 2'],row['Team 1'],row['Margin'],row['Ground'],row['Match Date'],row['Winner']]
	itr+=1

reverseDF.to_csv('dataset_reverse.csv')

print "Saved to File!"