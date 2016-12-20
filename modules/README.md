# Modules Overview
This folder divides the project into different modules, each of which has its own responsibility. We are undergoing some changes currently, so some of these folders will go away (more information below).

### Description and Status
If a module is labeled as DEPRECATED, do not add anymore code to that folder. It is undergoing replacement.
- DMZ: Under active developerment
  - This module is for shared functionality, such at utility classes and machine learning models.
- MLTA: Under active development
  - This module is responsible for logging and analyzing data about trained models and their results.
- hub: Under active development
  - This module focuses on deploying workers that can train and test models. Eventually it will deploy workers to other servers on a network.
- reducers: DEPRECATED
- toolbox: DEPRECATED
- worker: Under active development
  - A worker requests tickets and satisfies the requirements of each ticket (or reports a failure). As part of a ticket they will be told what data to target, along with the model to use.

This documentation is ongoing and we will be adding more information as needed.
