import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from modules.toolbox import framework_tools as ft
from modules.toolbox import ml_runners as mr
import setup
from sklearn.random_projection import GaussianRandomProjection
from sklearn.decomposition import PCA
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import FastICA


# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
def principle_component_analyzer(data):
    pca = PCA(n_components=3)  # if components is not specified, all components are kept.
    pca.fit_transform(data)  # This both fits pca and transforms in 1 command
    pca = (pd.DataFrame(pca.components_, columns=data.columns))  # Retain feature labels
    return pca


# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA
def independent_component_analyzer(data):
    ica = FastICA(n_components=3)
    ica.fit_transform(data)
    ica = (pd.DataFrame(ica.components_, columns=data.columns))
    return ica


# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html
def factor_component_analyzer(data):
    far = FactorAnalysis(n_components = 3)
    far.fit_transform(data)
    far = (pd.DataFrame(far.components_, columns=data.columns))
    return far


# http://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection
def gaussian_random_projection(data):
    grp = GaussianRandomProjection(n_components=3)  # default is 'auto', but leads to interesting results
    grp.fit_transform(data)
    grp = (pd.DataFrame(grp.components_, columns=data.columns))
    return grp
