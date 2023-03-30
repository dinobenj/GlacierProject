#https://blog.sellorm.com/2021/04/25/shiny-app-in-docker/
FROM rocker/shiny:4.2.3
#RUN R -e 'install.packages(c(\
#          "rsconnect", "leaflet", "shiny", "shinydashboard", "RColorBrewer", \
#          "jsonlite", "rgdal", "ggplot2", "raster", "elevatr", "rgeos", \
#          "leaflet", "rgl", "bmp", "httr", "countrycode", "sqldf", "arrow", \
#          "progress")) 
RUN install2.r rsconnect leaflet shiny shinydashboard RColorBrewer jsonlite rgdal \
     ggplot2 raster elevatr rgeos leaflet rgl bmp httr countrycode sqldf arrow progress
WORKDIR /home/shinyusr
COPY Deployment .

#app.R \
#     ui.R \
#     test_with_all_glaciers.R \
#     deploy.R \
#     ./

CMD Rscript deploy.R