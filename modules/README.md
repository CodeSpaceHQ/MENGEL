# Modules Overview
This folder divides the project into different modules, each of which has its own responsibility. We are undergoing some changes currently, so some of these folders will go away (more information below).

### Description and Status
If a module is labeled as DEPRECATED, do not add anymore code to that folder. It is undergoing replacement.
- MLTA: Under active development. This module is responsible for logging and analyzing data about trained models and their results.
- data_supplier: Under active development. This module will have a primary singleton that uses other classes to load, clean, modify, and provide data to machine learning algorithms.
- gym: Under active development. This module will train and validate machine learning models. This is also where results will be logged using MLTA.
- logger: DEPRECATED
- ml_models: DEPRECATED
- model_coach: Under active development. This module will select algorithms to use based on the configuration options provided for the given project. It will request data and pass the model and the data to the gym for training and validation.
- reducers: DEPRECATED
- supply_closet: Under active development. This module will contain helper classes and utilities for the project.
- toolbox: DEPRECATED

This documentation is ongoing and we will be adding more information as needed.
