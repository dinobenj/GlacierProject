library(raster)
#library(Rtools)
library(rgdal)
library(httr)
library(rjson)
library(jsonlite)
library(reticulate)
library(curl)

py_install('requests')

source_python('API_call_import.py')

#url <- get_geotiff(3.4653, 62.2159)

url <- get_geotiff(25.2975, 91.5826)

if (file.exists("precip_data.tif")) {
  unlink("precip_data.tif")
}

curl_download(url, destfile = "precip_data.tif")

#download.file(get_geotiff(25.2975, 91.5826), destfile = "precip_data.tif")
#download.file(url, paste0('n0r_', sub(".*\\b(\\d+).*", "\\1", url), '.tif'), method = 'curl')

precip_data <- NULL
precip_data <- raster("precip_data.tif")


# plot raster data
par(mar = c(1, 1, 1, 1))
plot(precip_data,
     main = "Percipitation Visualization 1 (DSM)")

