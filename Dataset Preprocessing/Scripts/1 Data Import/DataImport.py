#Script for Importing data from Stats.cricinfo website

import pandas as pd

for var in range(2000,2018):
	newVar = str(var)
	DF = pd.read_html('http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id='+newVar+';type=year')
	newDF = pd.DataFrame(DF[0])
	newDF.to_csv('Records'+newVar+'.csv')
	print('Done for Year:'+newVar)