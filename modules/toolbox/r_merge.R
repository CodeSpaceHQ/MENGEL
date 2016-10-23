#######   merge.py  ########

#  merge is an r-script that is is called from python (merge.py)
#
#  The first input from the arguments should be what the datasets are joined on,
#  The next unspecefied number of arguments from Args will be the filepath of the datasets (in .csv form)
#  r_merge assumes that every file that is piped in has a column with the name of argument 1.
#
##

#### DOCUMENTATION #####
#
#  this rscript requries the dplyr package in order to run
#  to install type install.packages("dplyr") in to R console (see README.md)
#
##

library(dplyr)

path = getwd()
path = ifelse(length(grep("tests", path)) == 1, paste0(getwd(), "/../datasets"), paste0(getwd(), "/../../datasets"))

setwd(path) ### sets the path dynamically per machine, assuming this filestructure.

Args <- commandArgs(trailingOnly =  T)

### the variable to merge the datasets by #####
merge.var <- Args[1]

###t this will be the dataset that everything is joined to ###
dataset <- read.csv((Args[2]))

#### writing for loops in R makes me sad, may look into re-writng this with an apply function #####

for (filepath in 3:length(Args)){
    dataset = dplyr::full_join(dataset, read.csv(as.character(Args[filepath])), by = merge.var)
}

### Save as .csv ####
write.csv(dataset, "full.dataset.csv")

##### Save as RDS (rdata file) ####
saveRDS(dataset, "full.dataset.rds")
