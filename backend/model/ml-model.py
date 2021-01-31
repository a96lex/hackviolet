import numpy as np

np.set_printoptions(threshold=np.inf)  # Showing all the array in Console
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# ------ Importing the DataSet

dataset = pd.read_csv("./voice.csv")
col = ["sp.ent", "meandom", "mindom", "maxdom", "dfrange", "modindx"]
dataset.drop(col, inplace=True, axis=1)

#####################################################
#                                                   #
#        Starting with Sets and Pre-Processing      #
#                                                   #
#####################################################

# ------ Separating the Independent and Dependent Variables
# Getting all Columns, except the last one with the genders
X = dataset.iloc[:, :-1].values
# Getting the last column
y = dataset.iloc[:, -1].values

# No Need of Taking Care of Missing Data :)

# ------ Encoding Categorical Data of the Dependent Variable
# male -> 1
# female -> 0
from sklearn.preprocessing import LabelEncoder

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# ------ Splitting the Dataset into the Training Set and Test Set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

# ------- Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#####################################################
#                                                   #
#                  Kernel SVM - RBF                 #
#                                                   #
#####################################################

# Fitting Kernel SVM to the Training set
from sklearn.svm import SVC

classifier = SVC(kernel="rbf", random_state=0)
classifier.fit(X, y)
import pickle

f = open("./model.pickle", "wb")
pickle.dump(classifier, f)
