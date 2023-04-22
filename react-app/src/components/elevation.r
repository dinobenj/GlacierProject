# Load required libraries
library(raster)

# Set working directory
setwd("C:/Users/William Lin/Desktop/GlacierProject/react-app/src/components")

# Load elevation data
elevation_data <- raster("elevation/file.tif")

# Load glacier data from CSV file
glacier_data <- read.csv("glacier.csv")

# Extract elevation values for glacier locations
glacier_elevation <- extract(elevation_data, as.matrix(glacier_data[, c("longitude", "latitude")]), method="bilinear")

# Create a color palette
colors <- colorRampPalette(c("white", "blue"))

# Plot the elevation map with glacier locations
plot(elevation_data, col=colors(100), main="Elevation Map for Glaciers")
points(glacier_data$longitude, glacier_data$latitude, pch=20, col="red", cex=0.7)
