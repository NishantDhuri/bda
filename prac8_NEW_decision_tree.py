import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv('diabetes (1).csv',header=None, names=col_names)
pima.head()
 
# Split dataset into features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols]
Y = pima.label
# Split dataset into training set and testing set
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=1)
# 70% training 30% testing
# Create Decision Tree Classifier Object
clf = DecisionTreeClassifier()
# Train Decision Tree Classifier
clf = clf.fit(X_train,Y_train)
#Predict the response for test dataset
Y_pred = clf.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print('Accuracy:- ',metrics.accuracy_score(Y_test,Y_pred))
 
# Visualizing Decision Tree
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10, 8))
plot_tree(clf, feature_names=feature_cols, class_names=['0', '1'], filled=True)
plt.show()
