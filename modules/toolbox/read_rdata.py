####### read_rdata.py #######
###  Created by Ryan Berg 10/9/2016
###  User Story: As a user I want to be able to read an rdata file and convert it to a pandas data frame
###
### This function assums that there is a .rds file saved, and the filepath to that file is input from the command line.
###


import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()
import sys

class reader:

    def Read_rds(filepath):
        """
        :input: filepath to .rds file
        :return: A pandas Dataframe
        """
        dataset = robjects.r['readRDS'](filepath)
        dataset = pandas2ri.ri2py(dataset)
        return dataset


    if __name__ == "__main__":
        filepath = sys.argv[1]
        dataset = Read_rds(filepath)
