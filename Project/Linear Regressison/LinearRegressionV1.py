import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score
from sklearn import linear_model
#Load data
dataframe = pd.read_csv('/home/asus/learning/learnML/Project/Linear Regressison/data/Advertising.csv')
radio_X = dataframe.values[:,2]
sales_y = dataframe.values[:,4]

np.random.seed(7)
radio_train , radio_test , sales_train, sales_test = train_test_split(radio_X,sales_y)


#plt.scatter(radio_train, sales_train,marker='o')
#plt.show()

#define predic function
def predic_sale(new_radio, weight, bias):
    return new_radio*weight + bias

#define lost function
def lost_func(radio_train, sales_train, weight, bias):
    lenght_X = len(radio_train)
    total_error = 0.0
    for i in range(lenght_X):
        total_error += (sales_train[i] - (weight*radio_train[i] + bias))**2
    return total_error / lenght_X

#update weight and bias with gradient descent lost function
def update_weight(radio_train, sales_train, weight, bias, learning_rate):
    weight_temp = 0.0
    bias_temp = 0.0
    lenght_X = len(radio_train)
    for i in range(lenght_X):
        # -2x(y - (mx + b))
        weight_temp += -2*radio_train[i]*(sales_train[i] - (weight*radio_train[i] + bias))
        # -2(y - (mx + b))  
        bias_temp += -2*(sales_train[i] - (weight*radio_train[i] + bias))
    weight -= (weight_temp / lenght_X)*learning_rate
    bias   -= (bias_temp / lenght_X)*learning_rate
    return weight, bias

#training
def train(radio_train, sales_train, weight, bias, learning_rate, iters):
    lost_his = []
    for i in range(iters):
        weight,bias = update_weight(radio_train, sales_train, weight, bias, learning_rate)
        lost = lost_func(radio_train, sales_train, weight, bias)
        lost_his.append(lost)
    return weight,bias, lost_his

weight, bias, lost = train(radio_train, sales_train, 0.03, 0.014, 0.001, 6000)

print(weight)
print(bias)
#print(lost)
iters = [i for i in range(6000)]

plt.plot(iters, lost)
plt.show()



plt.scatter(radio_train, sales_train,marker='o')
plt.plot(radio_train,radio_train*weight + bias)
plt.show()
#Accuracy of linear regreession using RMSE score

sales_pred = predic_sale(radio_test,weight,bias)

# sum of square of residuals
ssr = np.sum((sales_pred - sales_test)**2)

#  total sum of squares
sst = np.sum((sales_test - np.mean(sales_test))**2)

# R2 score
r2score = 1 - (ssr/sst)

print('Accuracy of model: %.2f %%' %(100*r2score))




