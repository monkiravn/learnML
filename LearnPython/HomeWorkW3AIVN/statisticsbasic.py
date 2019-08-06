from collections import Counter
data = ([7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10])
def mean(data):
    sumData = sum(data)
    N = len(data)
    return sumData / N

def variance(data):
    temp = []
    meanData = mean(data)
    for d in data:
        temp.append((d - meanData)**2)
    var = mean(temp)
    return var
def min(data):
    temp = data[0]
    for d in data:
        if (d < temp):
            temp = d
    return temp
def max(data):
    temp = data[0]
    for d in data:
        if (d > temp):
            temp = d
    return temp

def counter(data):
    c = Counter(data) #counter in data
    data_fren = c.most_common() #convert to list
    data_fren.sort() #sort list
    return data_fren


