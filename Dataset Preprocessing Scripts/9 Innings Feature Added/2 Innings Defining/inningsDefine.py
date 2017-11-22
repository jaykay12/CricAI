#This Script defines the Innings of each team, Team 1 and Team 2 as FirstInnings or SecondInnings

import pandas as pd

inningsDF = pd.DataFrame(columns = ['Scorecard','Team 1','Team 2','Innings_Team1','Innings_Team2'])

ourDF = pd.read_csv('dataset.csv')

print "CSVs Loaded!"

itr = 0
for i,row in ourDF.iterrows():
	if row['Winner']==row['Team 1'] and row['Margin']=="Winner1stInning":
		inningsDF.loc[itr] = [row['Scorecard'],row['Team 1'],row['Team 2'],"First","Second"]
	elif row['Winner']==row['Team 1'] and row['Margin']=="Winner2ndInning":
		inningsDF.loc[itr] = [row['Scorecard'],row['Team 1'],row['Team 2'],"Second","First"]
	elif row['Winner']==row['Team 2'] and row['Margin']=="Winner1stInning":
		inningsDF.loc[itr] = [row['Scorecard'],row['Team 1'],row['Team 2'],"Second","First"]
	elif row['Winner']==row['Team 2'] and row['Margin']=="Winner2ndInning":
		inningsDF.loc[itr] = [row['Scorecard'],row['Team 1'],row['Team 2'],"First","Second"]
	itr+=1

ourDF = pd.merge(ourDF,inningsDF,how='inner',left_on=['Scorecard','Team 1','Team 2'],right_on=['Scorecard','Team 1','Team 2'])
print "Merging Done!"

ourDF.to_csv('dataset_final.csv',index=False)