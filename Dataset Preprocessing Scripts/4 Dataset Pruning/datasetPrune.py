#This script removes all the match entries of second class teams & special 11 teams from the dataset

import pandas as pd

df = pd.read_csv('Dataset.csv')

print("File Opened")

teamsA = df['Team 1'] != ("Asia XI" or "Africa XI" or "ICC World XI")
teamsB = df['Team 2'] != ("Asia XI" or "Africa XI" or "ICC World XI")
WinnersTied = df['Winner'] != "tied"
WinnersNoResults = df['Winner'] != "no result"

print("Done Selecting")

newDF = df[teamsA & teamsB & WinnersTied & WinnersNoResults]
newDF.to_csv('FinalDataset.csv',index=False)