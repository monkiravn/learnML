import pandas as pd 
import matplotlib.pyplot as plt
#Load data
dataframe = pd.read_csv('/home/asus/learnML/Project/Linear Regressison/data/Advertising.csv')
radio_X = dataframe.values[:,2]
sales_y = dataframe.values[:,4]

#plt.scatter(radio_X, sales_y,marker='o')
#plt.show()

#define predic function
def predic_sale(new_radio, weight, bias):
    return new_radio*weight + bias

#define lost function
def lost_func(radio_X, sales_y, weight, bias):
    lenght_X = len(radio_X)
    total_error = 0.0
    for i in range(lenght_X):
        total_error += (sales_y[i] - (weight*radio_X[i] + bias))**2
    return total_error / lenght_X

#update weight and bias with gradient descent lost function
def update_weight(radio_X, sales_y, weight, bias, learning_rate):
    weight_temp = 0.0
    bias_temp = 0.0
    lenght_X = len(radio_X)
    for i in range(lenght_X):
        # -2x(y - (mx + b))
        weight_temp += -2*radio_X[i]*(sales_y[i] - (weight*radio_X[i] + bias))
        # -2(y - (mx + b))  
        bias_temp += -2*(sales_y[i] - (weight*radio_X[i] + bias))
    weight -= (weight_temp / lenght_X)*learning_rate
    bias   -= (bias_temp / lenght_X)*learning_rate
    return weight, bias

#training
def train(radio_X, sales_y, weight, bias, learning_rate, iters):
    lost_his = []
    for i in range(iters):
        weight,bias = update_weight(radio_X, sales_y, weight, bias, learning_rate)
        lost = lost_func(radio_X, sales_y, weight, bias)
        lost_his.append(lost)
    return weight,bias, lost_his

weight, bias, lost = train(radio_X, sales_y, 0.03, 0.014, 0.001, 60)

print(weight)
print(bias)
print(lost)
iters = [i for i in range(60)]

#plt.plot(iters, lost)
#plt.show()

plt.scatter(radio_X, sales_y,marker='o')
plt.plot(radio_X,radio_X*weight + bias)
plt.show()


