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

url <- get_geotiff(29.5160, 103.3347)

if (file.exists("precip_data.tif")) {
  unlink("precip_data.tif")
  print("File is deleted..")
}

curl_download(url, destfile = "precip_data.tif")

#download.file(get_geotiff(25.2975, 91.5826), destfile = "precip_data.tif")
#download.file(url, paste0('n0r_', sub(".*\\b(\\d+).*", "\\1", url), '.tif'), method = 'curl')


precip_data  <- raster("precip_data.tif")


# plot raster data
par(mar = c(1, 1, 1, 1))
plot(precip_data,
     main = "Percipitation Visualization 1 (DSM)",
     xlim=c(0, 100), ylim=c(0, 100))

