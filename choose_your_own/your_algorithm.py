#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

import numpy as np
from sklearn import ensemble
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from time import time

clf = ensemble.AdaBoostClassifier(n_estimators=20, learning_rate=2, random_state=1)  # acc = 0.936
clf = ensemble.RandomForestClassifier(n_estimators=20, min_samples_split=90, random_state=1) # acc = 0.936
clf = KNeighborsClassifier(n_neighbors=8) # acc = 0.944

print "Using '%s'" % clf.__class__.__name__

t0 = time()
clf.fit(features_train, labels_train)
print "Training time: %s s" % round(time()-t0, 3)

t0 = time()
predictions = clf.predict(features_test)
print "Prediction time: %s s" % round(time()-t0, 3)

accuracy = accuracy_score(predictions, labels_test)

print "Accuracy: %s" % accuracy

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
