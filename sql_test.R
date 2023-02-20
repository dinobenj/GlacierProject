library(sqldf)
data <- read_parquet("WGMS-FoG-2021-05-D-CHANGE.parquet")
lon_lat_data <- read_parquet("WGMS-FoG-2021-05-A-GLACIER.parquet")
#"NAME", "WGMS_ID", "POLITICAL_UNIT", "YEAR", "AREA_CHANGE", "THICKNESS_CHG"
sqldf("
      SELECT 
      NAME, WGMS_ID, POLITICAL_UNIT, YEAR, AREA_CHANGE, THICKNESS_CHG 
      FROM data 
      WHERE AREA_CHANGE != 'NA'
      ")