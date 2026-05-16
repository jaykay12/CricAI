#This Script Segregates the Win Margings into Winner1Inning & Winner2Inning using keywords like runs & wickets respectively.

import pandas as pd
import re

df = pd.read_csv('dataset.csv')
regInning2 = r'(.*?)(?:wickets|wicket)'
regInning1 = r'(.*?)(?:runs|run)'

df['Margin'].replace(to_replace=[regInning1,regInning2],value=['Winner1stInning','Winner2ndInning'],regex=True,inplace=True)

df.to_csv('dataset_new.csv',index=False)