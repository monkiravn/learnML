import math
def derTanh(x):
    result = 4*(math.e**(-2*x))/(1 + math.e**(-2*x))
    return result
#Tinh dao ham cua f(x) = tanh(x) = 2/(1+e^-2x) - 1
#f'(x) = 4*(e^-2x)/(1+e^-2x)
print('Ket qua cua dao ham f(x) = tanh(x) tai x0 = 9 la:',derTanh(9))
def derELU(x, Anphal):
    if(x < 0 ):
        result = Anphal*(math.e**x)
    else:
        result = 1
    return result
#Tinh dao ham cua ham ELU(Exponential Linear Unit)
print('Ket qua dao ham cua ham ELU tai x = -9 va x = 2 la',derELU(-9,1),'  ', derELU(2,1))