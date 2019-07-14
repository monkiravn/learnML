from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np
np.random.seed(7)
iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size= 130)
print(len(X_test))
model = DecisionTreeClassifier()
model.fit(X_train,y_train)
X_New = np.array([[6.4, 3.1, 5.0, 2.0]])
result = model.predict(X_New)
print(result)
print("Accuracy of model : %.2f %%" %(100*model.score(X_test, y_test)))
