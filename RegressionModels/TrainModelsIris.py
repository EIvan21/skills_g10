from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle

# Instanciamos el dataset
iris = load_iris()

# Definimos las variables objetivo e independientes
X = iris.data
y = iris.target

# Separamos los datos de train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Instanciamos los modelos

lr = LinearRegression()
dtc = DecisionTreeClassifier()
svc = LinearSVC(multi_class='crammer_singer', max_iter=1000)

lr.fit(X_train,y_train)
dtc.fit(X_train,y_train)
svc.fit(X_train,y_train)

pickle.dump(lr, open("LinearModel.pkl","wb"))
pickle.dump(dtc, open("TreeModel.pkl","wb"))
pickle.dump(svc, open("SVCModel.pkl","wb"))