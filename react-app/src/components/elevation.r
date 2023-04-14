# Load required libraries
library(raster)

# Set working directory
setwd("path/to/working/directory")

# Load elevation data
elevation_data <- raster("path/to/elevation/file.tif")

# Load glacier data
glacier_data <- shapefile("path/to/glacier/shapefile.shp")

# Extract elevation values for glacier locations
glacier_elevation <- extract(elevation_data, glacier_data)

# Create a color palette
colors <- colorRampPalette(c("white", "blue"))

# Plot the elevation map with glacier locations
plot(elevation_data, col=colors(100), main="Elevation Map for Glaciers")
plot(glacier_data, add=TRUE, pch=20, col="red")
