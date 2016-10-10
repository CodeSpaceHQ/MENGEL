<a href="https://codeclimate.com/github/ASAAR/SE2-KaggleComp"><img src="https://codeclimate.com/github/ASAAR/SE2-KaggleComp/badges/gpa.svg" /></a> <a href="https://codeclimate.com/github/ASAAR/SE2-KaggleComp"><img src="https://codeclimate.com/github/ASAAR/SE2-KaggleComp/badges/issue_count.svg" /></a>

# SE2-KaggleComp
Software Engineering 2 class kaggle competition repo. We'll also be building a bit of a framework to help make doing these easier in the future.

## Setup Instructions
**You must be using a unix system for this software to work!**

###### Setting up Ubuntu Bash for Windows
[Use this tutorial](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)

###### Setting up machine learning libraries for Python
1. [Install the latest Python 2.7](https://www.python.org/downloads/release/python-2712/)
2. Go into your unix system and install [SciPy](https://www.scipy.org/install.html)
  1. Note that installation might be different for different systems
  2. For Ubuntu, try:
  
      ```shell
      sudo apt-get install python-numpy python-scipy python-pandas python-sympy python-nose
      ```
3. Install [SciKit-Learn](http://scikit-learn.org/stable/install.html) using pip

###### Miscellaneous
- We are using [ZenHub](https://www.zenhub.com/) for project management.
- We are using [AzureMLStudio](https://studio.azureml.net/) for initial data analysis and some machine learning.
- Our [Google Drive](https://drive.google.com/drive/folders/0B_C34Fpc9Zf_TDlRUDhlZ0c3WVE?usp=sharing) with our other documents can be viewed here: 

###### Coding Standards (Please Call Us On It)
- [Python](https://google.github.io/styleguide/pyguide.html)

###### Running The Framework
We will be streamlining this over future iterations, but currently it works like this. The framework is also not fully featured and only a few algorithms are fully supported currently.
- run "python launcher.py"
- provide answers to the following questions,
  - train or test: train means that you just want to see what kinds of results you might get, test means it will both train the model and run it against test data. Test is not fully supported yet.
  - training file name: In either case, this is necessary. Please include the file ending (i.e. .csv).
  - separator: This designates the type of separator used in the csv file, we will be modifying the way this works in the future to account for other file types.
  - target column: Provide the *name* of the column that you want to target, the framework will find and isolate that column before training a model.

We will be adding ways to see results, such as logger reports.
