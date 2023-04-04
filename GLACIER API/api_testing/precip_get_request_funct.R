# This file contains a function that makes the API request in R
# and then plots the resulting geotiff

library(raster)
#library(Rtools)
library(rgdal)
library(httr)
library(rjson)
library(jsonlite)


print_precip_graph <- function(input_lat, input_long){
  
  # get request for raster data from NASA PMM API
  dat <- GET("https://pmmpublisher.pps.eosdis.nasa.gov/opensearch", 
             query = list(q="precip_30mn", lat = input_lat, long = input_long))
  
  # abort if the API call is bad
  stop_for_status(dat)

  # open raster data
  lidar_dsm <- raster(dat)
  # plot raster data
  par(mar = c(1, 1, 1, 1))
  plot(lidar_dsm,
       main = "Lidar Digital Elevation Model (DSM)")
  
}

print_precip_graph(64.2008, 149.4937)
