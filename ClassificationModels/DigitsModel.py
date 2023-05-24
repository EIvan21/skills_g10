import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
import pickle

digits = load_digits()
X, y = digits.data, digits.target
clf = RandomForestClassifier()
clf.fit(X, y)

pickle.dump(clf, open("ClfModel.pkl","wb"))