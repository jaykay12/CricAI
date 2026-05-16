import pandas as pd

for var in range(1971,2018):
	newVar = str(var)
	df = pd.read_csv('Records'+newVar+'.csv')
	df.set_index('Scorecard',inplace=True)
	newDF = df[['Team 1','Team 2','Winner','Margin','Ground','Match Date']]
	newDF.to_csv('Records'+newVar+'.csv')
	print("Done: Furnishing Records of "+newVar)