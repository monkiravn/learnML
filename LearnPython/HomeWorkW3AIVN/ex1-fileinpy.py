import os
import numpy as np
from statisticsbasic import *
filepath = '/home/asus/learning/learnML/LearnPython/HomeWorkW3AIVN/data/Iris.csv'
file = open(filepath,'r')
if not (os.path.exists(filepath)):
    print('File not found!')
data = file.readlines()

dataNew = []
def IrisSpecies(Species):
    result = 0
    if (Species == 'Iris-versicolor'):
        result = 1
    elif (Species == 'Iris-virginica'):
        result = 2
    return result
for i in range(1,len(data)):
    string = data[i].split(',')
    SepalLengthCm = float(string[1].strip())
    SepalWidthCm = float(string[2].strip())
    PetalLengthCm = float(string[3].strip())
    PetalWidthCm = float(string[4].strip())
    Species = IrisSpecies(string[5].strip())
    dataNew.append([SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species])

dataNp = np.array(dataNew)
print('SepalLengthCm Min:',min(dataNp[:,0]))
print('SepalWidthCm Min:',min(dataNp[:,1]))
print('PetalLengthCm Min:',min(dataNp[:,2]))
print('PetalWidthCm Min:',min(dataNp[:,3]))
print('')
print('SepalLengthCm Max:',max(dataNp[:,0]))
print('SepalWidthCm Max:',max(dataNp[:,1]))
print('PetalLengthCm Max:',max(dataNp[:,2]))
print('PetalWidthCm Max:',max(dataNp[:,3]))
print('')
print('SepalLengthCm standard deviation:',variance(dataNp[:,0])**0.5)
print('SepalWidthCm standard deviation:',variance(dataNp[:,1])**0.5)
print('PetalLengthCm standard deviation:',variance(dataNp[:,2])**0.5)
print('PetalWidthCm standard deviation:',variance(dataNp[:,3])**0.5)
print('')
irisSpecies = counter(dataNp[:,4])
print('Iris Species:')
for count in irisSpecies:
    if (count[0] == 0):
        print('\tIris-setosa:',count[1])
    elif (count[0] == 1):
        print('\tIris-versicolor:',count[1])
    else:
        print('\tIris-virginica:',count[1])
file.close()





