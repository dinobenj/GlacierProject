#library(elevatr)
library(rgdal)
library(ggplot2)
library(httr)

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

test <- GET("http://localhost:3000/documents/WGMS-FoG-2021-05-A-GLACIER")

data <- read.json(GET("http://localhost:3000/documents/WGMS-FoG-2021-05-A-GLACIER"))
lon_lat_data <- read.json(GET("http://localhost:3000/documents/WGMS-FoG-2021-05-D-CHANGE"))

only_location <- lon_lat_data[, c(1,3, 2,5, 6, 7)]
only_location_sub <- subset(only_location, LATITUDE != "NA" & LONGITUDE != "NA")
only_location_sub[!duplicated(only_location_sub[c(5)]), ]

data[!duplicated(data[c(5)]), ]
change_data <- data[, c(2, 4, 1, 5, 9, 11)]
sub_data <- subset(change_data, AREA_CHANGE != "NA")

sub_data[, 'LATITUDE'] <- 0
sub_data[, 'LONGITUDE'] <- 0

for(x in sub_data$WGMS_ID){
  tmp <- which(only_location_sub$WGMS_ID == x)
  tmp_index <- which(sub_data$WGMS_ID == x)
  tmp_sub <- only_location_sub[tmp, ]
  sub_data[tmp_index,]$LATITUDE = tmp_sub$LATITUDE
  sub_data[tmp_index,]$LONGITUDE = tmp_sub$LONGITUDE
}

user_input <- "DIBBLE" #readline(prompt = "Enter the Glacier Name you would like to see a graph for: ")
plot_data <- sub_data[, c(1,4,5)]
plot_data <- subset(plot_data, NAME == user_input)
write.csv(plot_data, "test_with.csv")

gmap_data <- sub_data[, c(1, 7, 8, 3)]

gmap_data <- unique(gmap_data)


#-------------------------------
#Elevation Data
US_data <- subset(gmap_data, gmap_data$POLITICAL_UNIT == "US")


write.csv(US_data, "test_with.csv")
