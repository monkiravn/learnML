import pandas as pd
import numpy as np 
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

#Load data
dataframe = pd.read_csv('/home/asus/learnML/Project/Linear Regressison/data/Advertising.csv')
radio_X = dataframe.values[:, 2]
sales_y = dataframe.values[:, 4]

#split data to training set and test set
np.random.seed(7)
radio_train,radio_test,sales_train,sales_test = train_test_split(radio_X,sales_y)

X = radio_train.reshape(150,1)
y = sales_train

regr = linear_model.LinearRegression()
regr.fit(X, y) # in scikit-learn, each sample is one row
# Compare two results
print("scikit-learn’s solution : weight = ", regr.coef_[0], "bias = ", regr.intercept_)
y_pred = regr.predict(radio_test.reshape(50,1))
print('Accuracy of model: %.2f %%' %(100*r2_score(sales_test,y_pred)))





