import requests
import urllib
import pandas as pd

GLACIER_DATA = pd.read_csv("../../DOI-WGMS-FoG-2021-05/WGMS-FoG-2021-05-A-GLACIER.csv", encoding="latin1")
# USGS Elevation Point Query Service
url = r'https://nationalmap.gov/epqs/pqs.php?'

# coordinates with known elevation 
lat = [48.633, 48.733, 45.1947, 45.1962]
lon = [-93.9667, -94.6167, -93.3257, -93.2755]

# create data frame
df = pd.DataFrame({
    'lat': lat,
    'lon': lon
})

def get_lat_long(name: str) -> tuple:
    gd = GLACIER_DATA[GLACIER_DATA["NAME"] == name]
    return gd["LATITUDE"], gd["LONGITUDE"]

def elevation_function(df, lat_column, lon_column):
    """Query service using lat, lon. add the elevation values as a new column."""
    elevations = []
    for lat, lon in zip(df[lat_column], df[lon_column]):

        # define rest query params
        params = {
            'output': 'json',
            'x': lon,
            'y': lat,
            'units': 'Meters'
        }

        # format query string and return query value
        result = requests.get((url + urllib.parse.urlencode(params)))
        elevations.append(result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation'])

    df['elev_meters'] = elevations

if __name__ == "__main__":

    #elevation_function(df, 'lat', 'lon')
    print(get_lat_long("NO 4"))


    # print(df)