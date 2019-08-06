import numpy as np 
import random
from collections import Counter


data = [1,2,3,4,5,6,7,8,9]
sum = np.sum(data)
#Xac suat xuat hien cac chu so
new_data = [1/sum , 2 /sum,3/sum,4/sum,5/sum,6/sum,7/sum,8/sum,9/sum]
#chia thanh cac moc mien gia tri
new_data[-1] = 1 - new_data[-1]
for i in range(len(new_data) - 1):
    new_data[-i-2] = new_data[-i-1] - new_data[-i-2]
#ham xac dinh so dua vao mien gia tri
def point(number):
#    if ( number > 0 and number < 1/sum):
#        return 0
    if ( number >= new_data[0] and number < new_data[1]):
        return 1
    elif ( number >= new_data[1] and number < new_data[2]):
        return 2
    elif ( number >= new_data[2] and number < new_data[3]):
        return 3
    elif ( number >= new_data[3] and number < new_data[4]):
        return 4
    elif ( number >= new_data[4] and number < new_data[5]):
        return 5
    elif ( number >= new_data[5] and number < new_data[6]):
        return 6
    elif ( number >= new_data[6] and number < new_data[7]):
        return 7
    elif ( number >= new_data[7] and number < new_data[8]):
        return 8
    else: 
        return 9
#Ham lap 
def rand(iters):
    result = []
    temp = 0
    for i in range(iters):
        number = random.random()
        temp = point(number)
        result.append(temp)
    return result

pointP = rand(1000)
#Dem tan suat xuat hien
point_C = Counter(pointP) 
point_fren = point_C.most_common()
point_fren.sort()
fren = 0
for p in point_fren:
    fren += p[1]
    print('{0}\t{1}'.format(p[0],p[1]))
print(fren)


