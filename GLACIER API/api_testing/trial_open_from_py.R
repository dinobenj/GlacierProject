# This file calls the python get_geotiff function that I wrote in 
# the API_call_import.py file
# It converts the geotiff into a raster file, downloads the file,
# and plots the precipitation data

library(raster)
#library(Rtools)
library(rgdal)
library(httr)
library(rjson)
library(jsonlite)
library(reticulate)
library(curl)

# library for python API Calls
py_install('requests')

# telling R where the python function is
source_python('API_call_import.py')

# getting the download URL for the geotiff
url <- get_geotiff(25.2975, 91.5826)

# deleting the old file, if any
if (file.exists("precip_data.tif")) {
  unlink("precip_data.tif")
}

# downloading the new geotiff file from the python function call
curl_download(url, destfile = "precip_data.tif")

# reset precipitation data 
precip_data <- NULL
# create new raster file from geotiff
precip_data <- raster("precip_data.tif")

# plot raster data
par(mar = c(1, 1, 1, 1))
plot(precip_data,
     main = "Percipitation Visualization 1 (DSM)")

