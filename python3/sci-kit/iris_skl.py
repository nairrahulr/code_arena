import numpy as np
import warnings

from sklearn import datasets
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB


warnings.filterwarnings("ignore")

iris = datasets.load_iris()

x,y = iris.data[:,1:3], iris.target

clf1 = LogisticRegression(random_state = 1)
clf2 = RandomForestClassifier(random_state = 1)
clf3 = GaussianNB()

print('5-fold Cross Validation \n')

labels = ['Logistic Regression', 'Random Forest', 'Naive Bayes']

#for clf, label in zip([clf1, clf2, clf3], labels):
#    scores = model_selection.cross_val_score(clf, x, y, cv=5, scoring='accuracy')
#    print("Accuracy : %0.2f (+/- %0.2f) [%s]" %(scores.mean(), scores.std(), label))
	
voting_clf_hard = VotingClassifier(estimators=[(labels[0],clf1), (labels[1],clf2), (labels[2],clf3)], voting = 'hard')
voting_clf_soft = VotingClassifier(estimators=[(labels[0],clf1), (labels[1],clf2), (labels[2],clf3)], voting = 'soft')

labels_new = ['Logistic Regression', 'Random Forest', 'Naive Bayes', 'Voting_Classifier_Hard', 'Voting_Classifier_Soft']

for clf, label in zip([clf1, clf2, clf3, voting_clf_hard, voting_clf_soft], labels_new):
    scores = model_selection.cross_val_score(clf, x, y, cv=5, scoring='accuracy')
    print("Accuracy : %0.2f (+/- %0.2f) [%s]" %(scores.mean(), scores.std(), label))
	