from sklearn import svm
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier
import xgboost
from modules.DMZ.models import model_properties as mp


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
def train_random_forest():
    # Selecting the model
    return mp.ModelProperties(), RandomForestClassifier(n_estimators=100) # Default estimators is 10


# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
def train_knn():
    # Selecting the model
    return mp.ModelProperties(), neighbors.KNeighborsClassifier() # default is 5 neighbors


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn-svm-svc
def train_svc():
    # Selecting the model
    return mp.ModelProperties(), svm.SVC(decision_function_shape='ovo')


def train_xgboost_classifier():
    return mp.ModelProperties(), xgboost.XGBClassifier()
