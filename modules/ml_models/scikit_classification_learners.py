from modules.toolbox import framework_tools as ft
from sklearn import svm
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
def train_random_forest(x_train, y_train):
    # Selecting the model
    model = RandomForestClassifier(n_estimators=100) # Default estimators is 10

    # Training the model
    return model.fit(x_train, y_train)


# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
def train_knn(x_train, y_train):
    # Selecting the model
    model = neighbors.KNeighborsClassifier() # default is 5 neighbors

    # Training the model.
    return model.fit(x_train, y_train)


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn-svm-svc
def train_svc(x_train, y_train):
    # Selecting the model
    model = svm.SVC(decision_function_shape='ovo')

    # Training the model
    return model.fit(x_train, y_train)
