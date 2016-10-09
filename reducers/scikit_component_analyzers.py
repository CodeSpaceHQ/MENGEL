import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

def run_analyzer(analyzer, n, data):

    #Select the model to be run and input the number of components
    model = analyzer(n_components = n)

    #Fit and Transform the Data
    model.fit_transform(data)

    #Return the formatted data with the feature names back in place.
    model = (pd.DataFrame(model.components_, columns = data.columns))
    return model