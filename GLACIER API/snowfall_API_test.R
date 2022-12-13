

library(httr)
library(jsonlite)

check = GET("https://pmmpublisher.pps.eosdis.nasa.gov/opensearch", 
            query = list(q=precip_30mn,lat=1,lon=1,startTime=2022-10-30,endTime=2022-10-31))
data = fromJSON(rawToChar(check$content))
data$response

res = GET("https://api.open-notify.org/iss-pass.json",
          query = list(lat = 40.7, lon = -74))
data = fromJSON(rawToChar(res$content))
data$response