from sklearn import svm
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier
import setup
from modules.toolbox import framework_tools as ft


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
def train_random_forest(validation_pack, data_pack):
    # Selecting the model
    model = RandomForestClassifier(n_estimators=100) # Default estimators is 10

    # Training the model
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "random_forest")


# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
def train_knn(validation_pack, data_pack):
    # Selecting the model
    model = neighbors.KNeighborsClassifier() # default is 5 neighbors

    # Training the model.
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "svc")


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn-svm-svc
def train_svc(validation_pack, data_pack):
    # Selecting the model
    model = svm.SVC(decision_function_shape='ovo')

    # Training the model
    model = model.fit(validation_pack.x_train, validation_pack.y_train)

    if data_pack.output_style == "train":
        return model.score(validation_pack.x_test, validation_pack.y_test)
    elif data_pack.output_style == "test":
        predictions = model.predict(model, data_pack)
        ft.save_predictions(setup.get_datasets_path(), predictions, "svc")
