# This file calls the python get_geotiff function that I wrote in 
# the API_call_import.py file
# It takes the geotiff, converts it to a raster and plots 
# the precipitation data 

library(raster)
#library(Rtools)
library(rgdal)
library(httr)
library(rjson)
library(jsonlite)
library(reticulate)

# install the requests library from python
py_install('requests')

# find the python source file
source_python('API_call_import.py')

# create a raster data from the return value from 
# the python function get_geotiff(lat, long)
precip_data  <- raster(x = get_geotiff(25.2975, 91.5826))

# plot raster data
par(mar = c(1, 1, 1, 1))
plot(precip_data,
     main = "Percipitation Visualization 1 (DSM)",
     xlim=c(0, 100), ylim=c(0, 100))

