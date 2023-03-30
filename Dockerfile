#https://blog.sellorm.com/2021/04/25/shiny-app-in-docker/
FROM rocker/shiny:4.2.3
#RUN R -e 'install.packages(c(\
#          "rsconnect", "leaflet", "shiny", "shinydashboard", "RColorBrewer", \
#          "jsonlite", "rgdal", "ggplot2", "raster", "elevatr", "rgeos", \
#          "leaflet", "rgl", "bmp", "httr", "countrycode", "sqldf", "arrow", \
#          "progress")) 
RUN install2.r rsconnect leaflet shiny shinydashboard RColorBrewer jsonlite rgdal \
     ggplot2 raster elevatr rgeos leaflet rgl bmp httr countrycode sqldf arrow progress

RUN --mount=type=secret,id=SHINY_ACC_NAME \
     --mount=type=secret,id=SHINY_APP_TOKEN \
     --mount=type=secret,id=SHINY_APP_SECRET \
     --mout=type=secret,id=MASTER_NAME \
     export SHINY_ACC_NAME=$(cat /run/secrets/SHINY_ACC_NAME) && \
     export SHINY_APP_TOKEN=$(cat /run/secrets/SHINY_APP_TOKEN) && \
     export SHINY_APP_SECRET=$(cat /run/secret/SHINY_APP_SECRET) && \
     export MASTER_NAME=$(cat /run/secrets/MASTER_NAME) 
WORKDIR /home/shinyusr
COPY Deployment .

#app.R \
#     ui.R \
#     test_with_all_glaciers.R \
#     deploy.R \
#     ./

CMD Rscript deploy.R