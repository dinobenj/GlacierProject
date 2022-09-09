print("deez")
p_id <- dd$NAME
output_csv <- subset(data, data$NAME == input$Input_Glacier_Name)
print(output_csv)
base <- 'https://portal.opentopography.org/API/globaldem?demtype=AW3D30'
api_key <- '25747927abfb0a12754cbd91f7430743'
#raw <- httr::GET("https://portal.opentopography.org/API/globaldem?demtype=AW3D30&south=60.15333&north=60.17333&west=-149.2541&east=-149.2341&API_Key=25747927abfb0a12754cbd91f7430743")
tmp_south <- p$lat - 0.1
tmp_north <- p$lat + 0.1
tmp_west <- p$lng - 0.1
tmp_east <- p$lng + 0.1
tmp_str <- paste0(base, '&south=', tmp_south, '&north=', tmp_north, '&west=', tmp_west, '&east=', tmp_east, '&API_Key=',api_key)
print(tmp_str)
raw <- httr::GET(tmp_str)
destfile <- "C:\\Users\\Benjamin#2\\Box Sync\\Documents\\Glacier\\Glacier_Project\\test_csv.csv"
download.file(tmp_str, destfile)