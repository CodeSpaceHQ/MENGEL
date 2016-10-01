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
    print(data.head)
    data_df = pd.DataFrame(data)
    pca = PCA(n_components=5) #if components is not specified, all components are kept.
    pca.fit_transform(data_df) #This both fits pca and transforms in 1 command
    x = (pd.DataFrame(pca.components_, columns=data_df.columns, index=['PC-1', 'PC-2', 'PC-3', 'PC-4', 'PC-5']))
    return x

x = PCA_reducer()
print(x)
# def train_knn(data):
#     x_train, x_test, y_train, y_test = ft.get_train_test(data, "Survived")
#
#     # Selecting the model
#     model = KNeighborsClassifier(n_neighbors=5)
#     model.fit(x_train, y_train)
#     # Training the model.
#     return model.score(x_test, y_test)
