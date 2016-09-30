import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
from modules.ml_models import scikit_classification_learners
import setup
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA

#http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
def PCA_reducer():
    data = ft.get_data(setup.get_datasets_path(), "titanic_train.csv", ',')
    print(data.head())
    pca = PCA(n_components=5) #if components is not specified, all components are kept.
    data_2d = pca.fit_transform(data) #This both fits pca and transforms in 1 command
    print(data_2d)
    return pd.DataFrame(data_2d)

x = PCA_reducer()

# def train_knn(data):
#     x_train, x_test, y_train, y_test = ft.get_train_test(data, "Survived")
#
#     # Selecting the model
#     model = KNeighborsClassifier(n_neighbors=5)
#     model.fit(x_train, y_train)
#     # Training the model.
#     return model.score(x_test, y_test)
#
# x = PCA_reducer()
