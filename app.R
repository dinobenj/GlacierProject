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
library(RColorBrewer)
library(jsonlite)
library(rgdal)
library(ggplot2)


get_country_data <- function(political_unit){
  country_map_data <- subset(dd, POLITICAL_UNIT == political_unit)
  return(country_map_data)
}

return_graph_data <- function(data){
  return(data)
}

dd <- gmap_data

round_df <- function(x, digits) {
  # round all numeric variables
  # x: data frame 
  # digits: number of digits to round
  for(i in 1:ncol(x)){       
    if(class(x[,i])=="numeric"){         
      x[i] <-  round(x[i], digits)
    }     
  }     
  return(x) 
}

area_chart <- function(glacier_name){
  user_input <- glacier_name #readline(prompt = "Enter the Glacier Name you would like to see a graph for: ")
  plot_data <- sub_data[, c(1,4,5)]
  plot_data <- subset(plot_data, NAME == user_input)
  p <- plot(plot_data$YEAR, plot_data$AREA_CHANGE, main = "Deez Nut", xlab = "Year", ylab = "Area Change", xlim = c(1950, 2020), ylim = c(-10000, 10000))
  b <- barplot(plot_data$AREA_CHANGE, names.arg = plot_data$YEAR,
               main = user_input,
               xlab = "Years",
               ylab = "AREA CHANGE (1000m^2)",
               col = "blue")
  return(plot_data)
}


#map %>%
#  add_markers(lat = "LATITUDE", lon = "LONGITUDE", mouse_over = "NAME")

ui <- bootstrapPage(
  titlePanel("The Glacier Project"),
  tags$style(type = "text/css", "html, body {width:100%;height:100%}"),
  leafletOutput("mymap", width = "100%", height = "100%"),
  absolutePanel(top = 10, right = 10,
                selectInput(inputId = "Input_Country_Code", label = "Select 2 Letter Country Code", selected = TRUE, multiple = FALSE, choices = sort(dd$POLITICAL_UNIT)),
                selectInput(inputId = "Input_Glacier_Name", label = "Select Glacier:", multiple = FALSE, choices = sort(dd$NAME)),
                downloadLink("downloadData", "Click to dowload CSV"),
                plotOutput("plotxy", click = "plot_click")
  )
)

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
  
  output$mymap=renderUI({
    leafletOutput('mymap', width = "20%", height = "20%")
  })
  
  output$mymap <- renderLeaflet({
    leaflet() %>%
      addProviderTiles(providers$Esri.NatGeoWorldMap,
                       options = providerTileOptions(noWrap = TRUE)
      ) %>%
      setView(0,0, 2) %>%
      
      addMarkers(data = country_map_data <- subset(dd, POLITICAL_UNIT == input$Input_Country_Code),
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
  
  observeEvent(input$mymap_marker_click , { 
    
    p <- input$mymap_marker_click 
    print(p)
    
    updateSelectInput(session, 
                      "Input_Glacier_Name",
                      label = paste("Select Glacier:"),
                      choices = p$id,
                      selected = p$id)
    #base <- 'https://portal.opentopography.org/API/globaldem?demtype=AW3D30'
    #api_key <- '25747927abfb0a12754cbd91f7430743'
    #raw <- httr::GET("https://portal.opentopography.org/API/globaldem?demtype=AW3D30&south=60.15333&north=60.17333&west=-149.2541&east=-149.2341&API_Key=25747927abfb0a12754cbd91f7430743")
    #tmp_south <- p$lat - 0.1
    #tmp_north <- p$lat + 0.1
    #tmp_west <- p$lng - 0.1
    #tmp_east <- p$lng + 0.1
    #tmp_str <- paste0(base, '&south=', tmp_south, '&north=', tmp_north, '&west=', tmp_west, '&east=', tmp_east, '&API_Key=',api_key)
    #print(tmp_str)
    #raw <- httr::GET(tmp_str)
    #destfile <- "C:\\Users\\Benjamin#2\\Box Sync\\Documents\\Glacier\\Glacier_Project\\test.TIF"
    #download.file(tmp_str, destfile)
    #tmp_str = ""
    #print(raw[["content"]])
  })

  output$downloadData <- downloadHandler(
    filename = function(){
      paste("data-", Sys.Date(), ".csv", sep = "")
    },
    content = function(file){
      dwnld_data <- read.csv("tmp.csv")
      write.csv(dwnld_data, file)
    }
  )
  
}

shinyApp(ui = ui, server = server)


