from modules.toolbox import framework_tools as ft
from sklearn import svm
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
def run_random_forest(data, target_col):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, target_col)

    # Selecting the model
    model = RandomForestClassifier(n_estimators=100) # Default estimators is 10

    # Training the model
    model.fit(x_train, y_train)

    # Score the model
    return model.score(x_test, y_test)


# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
def run_knn(data, target_col):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, target_col)

    # Selecting the model
    model = neighbors.KNeighborsClassifier() # default is 5 neighbors

    # Training the model.
    model.fit(x_train,y_train)

    # Score the model
    return model.score(x_test, y_test)


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn-svm-svc
def run_svc(data, target_col):
    x_train, x_test, y_train, y_test = ft.get_train_test(data, target_col)

    # Selecting the model
    model = svm.SVC(decision_function_shape='ovo')

    # Training the model
    model.fit(x_train, y_train)

    # Score the model
    return model.score(x_test, y_test)
