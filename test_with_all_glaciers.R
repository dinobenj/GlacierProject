#library(elevatr)
library(rgdal)
library(ggplot2)
library(httr)
library(jsonlite)
library(countrycode)
library(sqldf)
library(arrow)

# Set working directory
##############################################
##############################################
# To set working directory, you can either do:
# 1) setwd("<your_directory_here>")
# 2) 
#  a) right click on file in RStudio Window
#  b) select "set as working directory"
##############################################
##############################################

# Pull data from API
data <- read_parquet("WGMS-FoG-2021-05-D-CHANGE.parquet")
lon_lat_data <- read_parquet("WGMS-FoG-2021-05-A-GLACIER.parquet")
only_location <- lon_lat_data[, c("POLITICAL_UNIT", "WGMS_ID", "NAME", "SPEC_LOCATION", "LATITUDE", "LONGITUDE")]

only_location$LATITUDE <- type.convert(only_location$LATITUDE, as.is = T)
only_location$LONGITUDE <- type.convert(only_location$LONGITUDE, as.is = T)
only_location$WGMS_ID <- type.convert(only_location$WGMS_ID, as.is = T)

only_location_sub <- subset(only_location, LATITUDE != "NA" & LONGITUDE != "NA")

#change_data <- data[, c("NAME", "WGMS_ID", "POLITICAL_UNIT", "YEAR", "AREA_CHANGE", "THICKNESS_CHG")]
change_data <- sqldf("
      SELECT 
      NAME, WGMS_ID, POLITICAL_UNIT, YEAR, AREA_CHANGE, THICKNESS_CHG 
      FROM data 
      WHERE AREA_CHANGE != 'NA'
      ")
sub_data <- subset(change_data)
sub_data$YEAR <- type.convert(sub_data$YEAR, as.is = T)
sub_data$AREA_CHANGE <- type.convert(sub_data$AREA_CHANGE, as.is = T)
sub_data$WGMS_ID <- type.convert(sub_data$WGMS_ID, as.is = T)
only_location$LATITUDE <- type.convert(only_location$LATITUDE, as.is = T)
only_location$LONGITUDE <- type.convert(only_location$LONGITUDE, as.is = T)
only_location$WGMS_ID <- type.convert(only_location$WGMS_ID, as.is = T)
only_location_sub$POLITICAL_UNIT <- countrycode(only_location_sub$POLITICAL_UNIT, "iso2c", "country.name")	
sub_data$POLITICAL_UNIT <- countrycode(sub_data$POLITICAL_UNIT, "iso2c", "country.name")
only_lon_lat <- only_location_sub[, c(3, 5, 6)]
sub_data <- merge(sub_data, only_lon_lat, by = c("NAME"))

gmap_data <- sub_data[, c(1, 7, 8, 3)]

gmap_data <- unique(gmap_data)


#-------------------------------
#Elevation Data
# US_data <- subset(gmap_data, gmap_data$POLITICAL_UNIT == "US")


# write.csv(US_data, "test_with.csv")

