import sys
import pandas as pd
from sklearn.model_selection import train_test_split as tts

class Dataset:
	def ReadCategoricalDataSet(self):
		self.match_data = pd.read_csv('CategoricalDataset.csv')

		target_cols = self.match_data.columns[217:237]
		feature_cols = self.match_data.columns[0:217]

		target_set = self.match_data[target_cols]
		feature_set = self.match_data[feature_cols]

		X = feature_set
		Y = target_set
		self.X_train, self.X_test, self.Y_train, self.Y_test = tts(X, Y, test_size=0.3, random_state=100)
		
	def ReadLabelledDataSet(self):
		self.match_data = pd.read_csv('LabelledDataset.csv')

		target_cols = self.match_data.columns[217]
		feature_cols = self.match_data.columns[0:217]

		target_set = self.match_data[target_cols]
		feature_set = self.match_data[feature_cols]

		X = feature_set
		Y = target_set
		self.X_train, self.X_test, self.Y_train, self.Y_test = tts(X, Y, test_size=0.3, random_state=100)	
	