#This Script constructs a new feature Venue as (Home,Away,Neutral) on the basis of Grounds Info

import pandas as pd

venueDF = pd.DataFrame(columns = ['Scorecard','Venue'])

ourDF = pd.read_csv('Dataset_addedHostCountry.csv')

print "CSVs Loaded"

itr = 0

for i,row in ourDF.iterrows():
	if row['Host_Country']==row['Winner']:
		venueDF.loc[itr] = [row['Scorecard'],"Winner_Home"]
	elif row['Host_Country']==row['Team 2'] or row['Host_Country']==row['Team 1']:
		venueDF.loc[itr] = [row['Scorecard'],"Winner_Away"]
	else:
		venueDF.loc[itr] = [row['Scorecard'],"Winner_Neutral"]

	itr+=1

ourDF = pd.merge(ourDF,venueDF,on='Scorecard',how='inner')
print "Merging Done!"

finalDF = pd.DataFrame(columns=['Scorecard','Team 1','Team 2','Margin','Ground','Match Date','Winner','Host_Country','Venue'])

itr = 0
toAdd = True
for i,row in ourDF.iterrows():
	if toAdd==True:
		finalDF.loc[itr] = [row['Scorecard'],row['Team 2'],row['Team 1'],row['Margin'],row['Ground'],row['Match Date'],row['Winner'],row['Host_Country'],row['Venue']]
		toAdd = False
		itr+=1
	else:
		toAdd = True
		continue

finalDF.to_csv('dataset_final.csv',index=False)
print "Dataset Saved to File!"