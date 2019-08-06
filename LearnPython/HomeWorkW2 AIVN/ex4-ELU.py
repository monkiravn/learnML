import numpy as np
import matplotlib.pyplot as plt

alpha = 0.1
#define function ELU y = alpha*(e^x - 1) if x < 0 else x >= 0 y = x
def ELU(data):
    result = []
    N = len(data)
    for i in range(N):
        if (data[i] < 0):
            temp = alpha*(np.exp(data[i]) - 1) 
            result.append(temp)
        else:
            temp = data[i]
            result.append(temp)
    return result

data = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
result = ELU(data)
plt.plot(data,result)
plt.xlabel('x values')
plt.ylabel('ELU values')
plt.title('ELU Function')
plt.show()