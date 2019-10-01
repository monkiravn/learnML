import matplotlib.pyplot as plt 
from keras.models import load_model
import numpy as np
from keras.datasets import cifar10
from keras.utils import np_utils

model = load_model('cw1_wresnet.h5')

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
Y_test = np_utils.to_categorical(y_test, 10)
#scores = model.evaluate(X_test, Y_test, verbose=1)
#print('Test loss:', scores[0])
#print('Test accuracy:', scores[1])

imgtest = 5
plt.imshow(X_test[imgtest])
plt.axis('off')

y_predict = model.predict(X_test[imgtest].reshape(1,32,32,3))
print('Giá trị dự đoán: ', np.argmax(y_predict))
print('Giá trị nhãn: ', np.argmax(Y_test[imgtest]))