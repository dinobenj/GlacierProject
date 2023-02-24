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


#source("./test_with_all_glaciers.R")#only run for first startup to load data



get_country_data <- function(political_unit) {
  country_map_data <- subset(dd, POLITICAL_UNIT == political_unit)
  return(country_map_data)
}

return_graph_data <- function(data) {
  return(data)
}

dd <- gmap_data

round_df <- function(x, digits) {
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

area_chart <- function(glacier_name) {
  user_input <- glacier_name #readline(prompt = "Enter the Glacier Name you would like to see a graph for: ")
  plot_data <- sub_data[, c(1, 4, 5)]
  plot_data <- subset(plot_data, NAME == user_input)
  p <- plot(plot_data$YEAR, plot_data$AREA_CHANGE, main = "Deez Nut", xlab = "Year", ylab = "Area Change", xlim = c(1950, 2020), ylim = c(-10000, 10000))
  b <- barplot(plot_data$AREA_CHANGE, names.arg = plot_data$YEAR,
               main = user_input,
               xlab = "Years",
               ylab = "AREA CHANGE (1000m^2)",
               col = "blue")
  return(plot_data)
}

# download the satellite image to filepath
display_raster <- function(p) {
  tmp_south <- p$lat - 0.1
  tmp_north <- p$lat + 0.1
  tmp_west  <- p$lng - 0.1
  tmp_east  <- p$lng + 0.1
  tmp1 <- data.frame(x = tmp_west, y = tmp_south)
  tmp2 <- data.frame(x = tmp_east, y = tmp_north)
  tmp <- rbind(tmp1, tmp2)
  elevation <- get_elev_raster(location = tmp, prj = "EPSG:4326", z = 9)
  pl <- plot(elevation, main = p$id, xlab = "Longitude", ylab = "Latitude")
  return(pl)
}


#map %>%
#  add_markers(lat = "LATITUDE", lon = "LONGITUDE", mouse_over = "NAME")

ui <- dashboardPage(
  dashboardHeader(title = "The Glacier Project"),
  dashboardSidebar(
    menuItem(selectInput(inputId = "Input_Country_Code", label = "Select 2 Letter Country Code", selected = TRUE, multiple = FALSE, choices = sort(dd$POLITICAL_UNIT))),
    selectInput(inputId = "Input_Glacier_Name", label = "Select Glacier:", multiple = FALSE, choices = sort(dd$NAME)),
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
#   bootstrapPage(
#   titlePanel("The Glacier Project"),
#   tags$style(type = "text/css", "html, body {width:100%;height:100%}"),
#   leafletOutput("mymap", width = "100%", height = "100%"),
#   absolutePanel(top = 5, right = 5,
#                 selectInput(inputId = "Input_Country_Code", label = "Select 2 Letter Country Code", selected = TRUE, multiple = FALSE, choices = sort(dd$POLITICAL_UNIT)),
#                 selectInput(inputId = "Input_Glacier_Name", label = "Select Glacier:", multiple = FALSE, choices = sort(dd$NAME)),
#                 downloadButton("downloadData", "Click to dowload CSV"),
#                 plotOutput("plotxy", click = "plot_click"),
#                 actionButton("plot_sat", "Click to display raster of selected Glacier")
#   ) 
# )

dd$INFO <- paste0(
  dd$NAME,
  ", ",
  dd$POLITICAL_UNIT
)


server <- function(input, output, session) {
  data <- reactive({
    dd
  })
  
  observeEvent(input$Input_Country_Code, {
    dd <- get_country_data(input$Input_Country_Code)
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
      
      addAwesomeMarkers(data = country_map_data <- subset(dd, POLITICAL_UNIT == input$Input_Country_Code),
                 icon = ice,
                 label = ~NAME,
                 #popup = area_chart(input$Input_Glaccier_Name),
                 layerId = ~NAME
      )
  })
  dwnld_data <- NULL
  output$plotxy <- renderPlot({
    area <- area_chart(input$Input_Glacier_Name)
    dwnld_data = area
    write.csv(dwnld_data, "tmp.csv")
    read.csv("tmp.csv")
  })
  
  
  
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
