from sklearn.svm import SVR
from numpy import dot
import numpy as np
n_samples, n_features = 6, 3
np.random.seed(0)
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)
clf = SVR(C=1.0, epsilon=0.2,kernel='linear')
clf.fit(X, y)
a=clf.fit(X, y).predict(X)
b=clf.coef_

print b#Weights assigned to the features
print '------------------------------------------------'
print X
print '------------------------------------------------'
print a
print '------------------------------------------------'


