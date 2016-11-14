# Overview
This sub-module of DMZ controls models and model selection.

## Sub-module
- model_filter.py: Controls the selection of the appropriate model based on the configuration of the project.
- model_properties.py: Allows each model to have specific properties which will help us with advanced selection
later on.
- classification: This folder contains all python files that allow access to classification models.
- regression: This folder contains all python files that allow access to regression models.

None of these except model_filter should be called directly. It will then return functions that
retrieve the model and the model parameters in the form (params, model).
