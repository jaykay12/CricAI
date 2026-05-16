#This Script normalizes the grounds data as Colombo(NBC) & Colombo(SBS) into Single venue like Colombo etc.

import pandas as pd
import re

df = pd.read_csv('dataset.csv')

ourRegex = r"(?P<Ground_id>[A-Za-z '.0-9]+(?<! ))+(.*)"
matched = r"\g<Ground_id>"

df['Ground'].replace(to_replace=ourRegex,value=matched,regex=True,inplace=True)

df.to_csv('dataset_final.csv')

