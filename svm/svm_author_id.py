#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

classifier = SVC(kernel='rbf', C=10000.0)

t0 = time()
classifier.fit(features_train, labels_train)
print "Training time: %s s" % round(time()-t0, 3)

t0 = time()
predictions = classifier.predict(features_test)
print "Prediction time: %s s" % round(time()-t0, 3)

accuracy = accuracy_score(predictions, labels_test)

print "Predicitions: %s" % predictions
print "Accuracy: %s" % accuracy

unique, counts = np.unique(predictions, return_counts=True)

print "Emails from Sara: %s" % counts[0]
print "Emails from Chris: %s" % counts[1]
#########################################################


