#This Script constructs a new feature Venue as (Home,Away,Neutral) on the basis of Grounds Info

import pandas as pd

venueDF = pd.DataFrame(columns = ['Scorecard','Team 1','Team 2','Venue_Team1','Venue_Team2'])

ourDF = pd.read_csv('Dataset_addedHostCountry.csv')

print "CSVs Loaded"

itr = 0

for i,row in ourDF.iterrows():
	if row['Host_Country']==row['Team 1']:
		venueDF.loc[itr] = [row['Scorecard'],row['Team 1'],row['Team 2'],"Home","Away"]
	elif row['Host_Country']==row['Team 2']:
		venueDF.loc[itr] = [row['Scorecard'],row['Team 1'],row['Team 2'],"Away","Home"]
	else:
		venueDF.loc[itr] = [row['Scorecard'],row['Team 1'],row['Team 2'],"Neutral","Neutral"]

	itr+=1

ourDF = pd.merge(ourDF,venueDF,how='inner',left_on=['Scorecard','Team 1','Team 2'],right_on=['Scorecard','Team 1','Team 2'])
print "Merging Done!"

ourDF.to_csv('dataset_final.csv',index=False)

'''
finalDF = pd.DataFrame(columns=['Scorecard','Team 1','Team 2','Margin','Ground','Match Date','Winner','Host_Country','Venue_Team1','Venue_Team2'])

itr = 0
toAdd = True
counter = 0
firstTime = True
for i,row in ourDF.iterrows():
	if toAdd==True:
		finalDF.loc[itr] = [row['Scorecard'],row['Team 2'],row['Team 1'],row['Margin'],row['Ground'],row['Match Date'],row['Winner'],row['Host_Country'],row['Venue_Team1'],row['Venue_Team2']]
		if firstTime==True:
			toAdd = False
			firstTime = False
		elif counter==1:
			toAdd = False
			counter = 0
		else:
			counter+=1
		itr+=1
	else:
		if counter==1:
			toAdd = True
			counter = 0
		else:
			counter+=1


finalDF.to_csv('dataset_final.csv',index=False)
print "Dataset Saved to File!"
'''