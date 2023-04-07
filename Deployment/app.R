#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#
library(leaflet)
library(shiny)
library(shinydashboard)
library(RColorBrewer)
library(jsonlite)
library(rgdal)
library(ggplot2)
library(raster)
library(elevatr)
library(rgeos)
library(leaflet)
library(RColorBrewer)
library(rgl)
library(bmp)
library(progress)


source("./test_with_all_glaciers.R")#only run for first startup to load data


#returns the map data for the given country
get_country_map_data <- function(political_unit) {
  country_map_data <- subset(map_data, POLITICAL_UNIT == political_unit)
  return(country_map_data)
}

round_dataframe <- function(x, digits) {
  # round all numeric variables
  # x: data frame 
  # digits: number of digits to round
  for (i in 1:ncol(x)) {
    if (class(x[, i]) == "numeric") {
      x[i] <- round(x[i], digits)
    }
  }
  return(x)
}

get_area_chart <- function(glacier_name) {
  plot_data <- area_data
  plot_data <- subset(plot_data, NAME == glacier_name)
  b <- plot(plot_data$YEAR,
            plot_data$AREA,
            type = "o",
            main = glacier_name,
            xlab = "Years",
            ylab = "AREA (1000m^2)",
            col = "blue")
  
  get_mass_chart <- funciton(glacier_name){
    plot_data <- mass_data
  }
  
  text(plot_data$YEAR, plot_data$AREA, labels=plot_data$YEAR, font=2)
  #print(plot_data)
  return(plot_data)
}


display_raster <- function(glacier) {
  #Take the glacier's position and create a box to
  #put the elevation data into
  southPoint <- glacier$lng - 0.1
  northPoint <- glacier$lng + 0.1
  westPoint <- glacier$lat - 0.1
  eastPoint <- glacier$lat + 0.1
  southwestBound <- data.frame(x = westPoint, y = southPoint)
  northeastBound <- data.frame(x = eastPoint, y = northPoint)
  boundingBox <- rbind(southwestBound, northeastBound)
  elevation_data <- get_elev_raster(location = boundingBox, prj = "EPSG:4326", z = 9)
  elevation_plot <- plot(elevation_data, main = glacier$id, xlab = "Latitude", ylab = "Longitude")
  return(elevation_plot)
}

ui <- dashboardPage(
  dashboardHeader(title = "The Glacier Project"),
  dashboardSidebar(
    menuItem(selectInput(inputId = "Input_Country_Code", label = "Select 2 Letter Country Code", selected = TRUE, multiple = FALSE, choices = sort(map_data$POLITICAL_UNIT))),
    selectInput(inputId = "Input_Glacier_Name", label = "Select Glacier:", multiple = FALSE, choices = sort(map_data$NAME)),
    selectInput(inputId = "data_select", label = "Select Graph Data", multiple = FALSE, choices = list("Area Change", "Mass Balance", "Precipitation")),
    div(style = "display:inline-block; float:center", actionButton("downloadData", "Click to dowload CSV")),
    div(style = "display:inline-block; float:center", actionButton("plot_sat","Display raster of selected Glacier"))
  ),
  dashboardBody(
    fluidRow(
      box(leafletOutput("mymap"), width = 14)
    ),
    fluidRow(
      box(plotOutput("plotxy", click = "plot_click")),
      box(plotOutput("ip"))
    )
    
  )
)


map_data$INFO <- paste0(
  map_data$NAME,
  ", ",
  map_data$POLITICAL_UNIT
)


server <- function(input, output, session) {
  data <- reactive({
    map_data
  })
  
  observeEvent(input$Input_Country_Code, {
    map_data <- get_country_map_data(input$Input_Country_Code)
  })
  
  output$mymap = renderUI({
    leafletOutput('mymap', width = "20%", height = "20%")
  })
  
  ice <- makeAwesomeIcon(
    icon = "snowflake",
    iconColor = "black",
    markerColor = "blue",
    library = "fa"
  )
  
  output$mymap <- renderLeaflet({
    leaflet() %>%
      addProviderTiles(providers$Esri.NatGeoWorldMap,
                       options = providerTileOptions(noWrap = TRUE)
      ) %>%
      setView(0, 0, 2) %>%
      
      addAwesomeMarkers(data = country_map_data <- subset(map_data, POLITICAL_UNIT == input$Input_Country_Code),
                 icon = ice,
                 label = ~NAME,
                 layerId = ~NAME
      )
  })
  dwnld_data <- NULL
  output$plotxy <- renderPlot({
    plot_data <- subset(area_data, NAME == input$Input_Glacier_Name)
    if(nrow(plot_data) == 0){
      print("This data frame is empty")
    }
    else{
      area <- get_area_chart(input$Input_Glacier_Name)
      dwnld_data = area
      write.csv(dwnld_data, "tmp.csv")
      read.csv("tmp.csv")
    }
  })
  
  # observeEvent(input$data_select, {
  #   display_type <- input$data_select
  #   if(display_type == "Mass Balance"){
  #     mass_balance <- get_mass_chart(input$Input_Glacier_Name)
  #     output$plotxy <- render
  #   }
  # })
  
  
  
  observeEvent(input$mymap_marker_click, {
    p <- input$mymap_marker_click
    print(p)
    updateSelectInput(session,
                      "Input_Glacier_Name",
                      label = paste("Select Glacier:"),
                      choices = p$id,
                      selected = p$id)
    
  })
  p1 <- eventReactive(input$plot_sat, {
        a <- display_raster(input$mymap_marker_click)
  })
  
  output$ip <- renderPlot({
    req(input$mymap_marker_click) #checks req of var to run display raster
    display_raster(input$mymap_marker_click)
  })
  output$downloadData <- downloadHandler(
    filename = function() {
      paste("data-", Sys.Date(), ".csv", sep = "")
    },
    content = function(file) {
      dwnld_data <- read.csv("tmp.csv")
      write.csv(dwnld_data, file)
    }
  )
  
  
  
}

shinyApp(ui = ui, server = server)
