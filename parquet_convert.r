library(arrow)
library(parquetize)

#===========================================================================
#This file is used to convert csv data file to parquet for faster processing
#===========================================================================
csv_to_parquet("data/WGMS-FoG-2021-05-D-CHANGE.csv", path_to_parquet = "./")
csv_to_parquet("data/WGMS-FoG-2021-05-A-GLACIER.csv", path_to_parquet = "./")