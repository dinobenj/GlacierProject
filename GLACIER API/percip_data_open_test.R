library(raster)
library(Rtools)
library(rgdal)

# open raster data
lidar_dsm <- raster(x = "gpm_7d.20230131(2).tif")
# plot raster data
plot(lidar_dsm,
     main = "Lidar Digital Elevation Model (DEM)")