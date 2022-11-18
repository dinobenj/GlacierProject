import requests
import urllib3
import urllib
import pandas as pd
import numpy as np
# import elevation

import geopandas as gpd
import rasterio


GLACIER_DATA = pd.read_csv("test.csv", usecols=["NAME", "LATITUDE", "LONGITUDE"], encoding="latin1")

# GLACIER_DATA = GLACIER_DATA[["NAME", "LATITUDE", "LONGITUDE"]]
# print(GLACIER_DATA)

def get_lat_long(name: str) -> tuple:
    # gd = GLACIER_DATA.query(f"NAME == {name}")
    gd = GLACIER_DATA.loc[GLACIER_DATA["NAME"] == name]
    return gd.iloc[0]["LATITUDE"], gd.iloc[0]["LONGITUDE"]

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
    return response.text
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.freemaptools.com/ajax/elevation-service.php?v=4&lat=-64.00000&lng=-65.00000', headers=headers)


if __name__ == "__main__":
    # print(GLACIER_DATA)
    thunder = get_lat_long("THUNDER")
    print(thunder)

    print(make_elevation_request(thunder[0], thunder[1]))
    # for col in GLACIER_DATA.columns:
    #     print(len(col))
    # elevation.clip(bounds=(thunder[0] - 0.1, thunder[1] - 0.1, thunder[0] + 0.1, thunder[1] + 0.1), output='test.tif')

    # elevation.clean()
    # elevation_function(get_lat_long("THUNDER"))
    # print(get_lat_long("NO 4"))


    # print(df)