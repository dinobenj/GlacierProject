#https://blog.sellorm.com/2021/04/25/shiny-app-in-docker/
FROM rocker/shiny:4.2.3

WORKDIR /home/shinyusr

#RUN install2.r rsconnect leaflet shiny shinydashboard RColorBrewer jsonlite rgdal \
#     ggplot2 raster elevatr rgeos leaflet rgl bmp httr countrycode sqldf arrow progress
RUN install2.r remotes
COPY DESCRIPTION .
RUN Rscript -e "remotes::install_deps()"

COPY Deployment .
CMD Rscript deploy.R