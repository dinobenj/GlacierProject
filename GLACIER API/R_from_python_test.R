library(raster)
#library(Rtools)
library(rgdal)
library(httr)
library(rjson)
library(jsonlite)
library(reticulate)

py_install('requests')

source_python('API_call_import.py')

#precip_data <- raster(x = get_geotiff(3.4653, 62.2159))

precip_data  <- raster(x = get_geotiff(25.2975, 91.5826))

#precip_data <- raster(x = get_geotiff(76.7000, 41.2000)) doens't work?

# plot raster data
par(mar = c(1, 1, 1, 1))
plot(precip_data,
     main = "Percipitation Visualization 1 (DSM)",
     xlim=c(0, 100), ylim=c(0, 100))

