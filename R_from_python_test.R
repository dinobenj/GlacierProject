library(raster)
#library(Rtools)
library(rgdal)
library(httr)
library(rjson)
library(jsonlite)
library(reticulate)

py_install('requests')

source_python('API_call_import.py')

precip_data <- get_geotiff(59.58985, -138.6278)

# open raster data
lidar_dsm <- raster(x = 'precip_geotiff.tif')
# plot raster data
plot(lidar_dsm,
     main = "Percipitation Visualization 1 (DSM)")