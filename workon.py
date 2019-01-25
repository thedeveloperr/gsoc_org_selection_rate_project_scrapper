import json
import pandas as pd
import matplotlib.pyplot as plt
with open("data.json") as datafile:
    data = json.load(datafile)
dataframe = pd.DataFrame(data)
dataframe['total'] = dataframe.sum(1)
dataframe.to_csv('dataframe.csv', encoding='utf-8')
