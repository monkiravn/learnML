import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

data = pd.read_csv('/home/asus/learnML/Project/MissingData/data/data.csv', header=None)
print(data)
dataNp = data.values

#imp = Imputer(missing_values = np.nan , strategy = 'mean') #fit missing data by mean value
imp = Imputer(missing_values = np.nan , strategy = 'most_frequent') #fit missing data by most frequent value
imp.fit(dataNp)
dataFull = imp.transform(dataNp)
print(dataFull)
