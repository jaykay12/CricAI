#This script modifies our dataset by merging the 2 datasets: dataset.csv & venues.csv

import pandas as pd

ourDF = pd.read_csv('dataset.csv')
DF = pd.read_csv('Venues.csv')

print "Both CSVs Loaded!"
ourDF = pd.merge(ourDF,DF,on='Ground',how='left')

ourDF.to_csv('Dataset_addedHostCountry.csv',index=False)
print "Merged Successfully & Saved to File!"