#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)

# Load glacier data
glacier_data <- read.csv("./WGMS-FoG-2021-05-D-CHANGE.parquet")

# Define UI
ui <- fluidPage(
  titlePanel("Glacier Dashboard"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("glacier_select", "Select Glacier:", choices = unique(glacier_data$glacier)),
      sliderInput("years_select", "Select Years:", min = min(glacier_data$year), max = max(glacier_data$year), value = c(2000, 2020))
    ),
    
    mainPanel(
      plotOutput("glacier_plot"),
      dataTableOutput("glacier_table")
    )
  )
)

# Define server
server <- function(input, output) {
  
  # Subset data based on user input
  selected_data <- reactive({
    glacier_data %>%
      filter(glacier == input$glacier_select) %>%
      filter(year >= input$years_select[1] & year <= input$years_select[2])
  })
  
  # Generate plot
  output$glacier_plot <- renderPlot({
    ggplot(selected_data(), aes(x = year, y = area)) +
      geom_line() +
      labs(title = paste0("Glacier Area for ", input$glacier_select), x = "Year", y = "Area (sq km)")
  })
  
  # Generate table
  output$glacier_table <- renderDataTable({
    selected_data() %>%
      select(year, area) %>%
      arrange(year)
  })
}

# Run app
shinyApp(ui = ui, server = server)
