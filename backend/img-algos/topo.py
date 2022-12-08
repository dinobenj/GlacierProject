import requests
import urllib3
import urllib
import pandas as pd
import numpy as np
import geopandas as gpd
import rasterio


GLACIER_DATA = pd.read_csv("test.csv", usecols=["NAME", "LATITUDE", "LONGITUDE"], encoding="latin1")

def get_lat_long(name: str) -> tuple:
    # gd = GLACIER_DATA.query(f"NAME == {name}")
    gd = GLACIER_DATA.loc[GLACIER_DATA["NAME"] == name]
    return float(gd.iloc[0]["LATITUDE"]), float(gd.iloc[0]["LONGITUDE"])

def make_elevation_request(lat, long):
    

    headers = {
        'referer': 'https://www.freemaptools.com/elevation-finder.htm',
    }

    params = (
        ('v', '4'),
        ('lat', str(lat)),
        ('lng', str(long)),
    )

    response = requests.get('https://www.freemaptools.com/ajax/elevation-service.php', headers=headers, params=params)
    result = response.text.split(",")
    return float(result[2].split(":")[1][:-2]) #1009,293,21

def get_elevation_from_region(lat, long):
    lis = []
    lat_range = np.arange(lat - 0.1, lat + 0.1, 0.03)
    long_range = np.arange(long - 0.1, long + 0.1, 0.03)
    for i in lat_range:
        for j in long_range:
            lis.append(make_elevation_request(i, j))
    return lis
    
if __name__ == "__main__":
    # print(GLACIER_DATA)
    thunder = get_lat_long("THUNDER")
    print(thunder)

    print(make_elevation_request(thunder[0], thunder[1]))
    print(get_elevation_from_region(thunder[0], thunder[1]))