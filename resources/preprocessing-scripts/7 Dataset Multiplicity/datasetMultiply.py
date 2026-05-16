#This script combines both the Straight dataset as well as Reverse Dataset to form a single 2x time dataset.

import pandas as pd

straightDF = pd.read_csv('dataset.csv')
reverseDF = pd.read_csv('dataset_reverse.csv')

frames = [straightDF,reverseDF]
combinedDF = pd.concat(frames)

print "Done Merging!"

combinedDF.to_csv('dataset_temp.csv',index=False)

print "Saved to file in some OUT OF ORDER!"


#finalDF = pd.DataFrame(columns = ['MIndex','Scorecard','Team 1','Team 2','Margin','Ground','Match Date','Winner'])

#itr = 0
#firstTime = True
#for i,(index,row) in enumerate(combinedDF.iterrows()):
#	finalDF.loc[itr] = [row['MIndex'],row['Scorecard'],row['Team 1'],row['Team 2'],row['Margin'],row['Ground'],row['Match Date'],row['Winner']]
#	itr+=2
#	if firstTime==True and i == 3752:
#		itr = 1
#	elif firstTime==False and i == 7504:
#		break
#	else:
#		continue
		
#finalDF.sort_values('MIndex')
#finalDF.to_csv('dataset_final.csv')
#
#print "Final Work Done!"