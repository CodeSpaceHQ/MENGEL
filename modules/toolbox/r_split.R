
#######   Splitter.py  ########

#  Splitter is a fucntion that takes is called from python (splitter.py)
#  The Data is read in, all the columns that are categorical are converted to factors
#  The Data is then split into training and testing data and exported to .csv in the folder
#  That RealSplit.py is called from.

setwd("datasets") ### need to set dynamically

library(dplyr)

Args <- commandArgs(trailingOnly =  T)

### reads in to csv and makes all String variables Factors #####

dataset <- read.csv(as.character(Args), sep = ';', stringsAsFactors = T)

### Randomly samples 80% of the dataset for training purposes
train.data <- data.frame(dplyr::sample_frac(dataset, .8, replace = F))

### gets the the rows from the original dataset that were not taken for the training set for testing purposes.
test.data <- setdiff(dataset, train.data)


### Will write to the folder calling from ####
write.csv(test.data, "testing.data.csv")
write.csv(train.data, "training.data.csv")

##### Save as RDS ####

saveRDS(test.data, "testing.data.rds")
saveRDS(train.data, "training.data.rds")