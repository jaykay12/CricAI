import pandas as pd

df = pd.read_csv('Records1971.csv')
for var in range(1972,2018):
	newVar = str(var)
	dfCurrent = pd.read_csv('Records'+newVar+'.csv')
	df = df.append(dfCurrent,ignore_index=True)
	print("Merging Records of:"+newVar)

df.set_index('Scorecard',inplace=True)
df.to_csv('Dataset.csv')