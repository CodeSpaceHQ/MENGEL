from sklearn import svm
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier
import setup
from modules.toolbox import framework_tools as ft


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
def train_random_forest():
    # Selecting the model
    return RandomForestClassifier(n_estimators=100) # Default estimators is 10


# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
def train_knn():
    # Selecting the model
    return neighbors.KNeighborsClassifier() # default is 5 neighbors


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn-svm-svc
def train_svc():
    # Selecting the model
    return svm.SVC(decision_function_shape='ovo')
