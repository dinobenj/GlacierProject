import requests
import urllib3
import urllib
import pandas as pd
import numpy as np
import elevation

GLACIER_DATA = pd.read_csv("test.csv", usecols=["NAME", "LATITUDE", "LONGITUDE"], encoding="latin1")

# GLACIER_DATA = GLACIER_DATA[["NAME", "LATITUDE", "LONGITUDE"]]
# print(GLACIER_DATA)

def get_lat_long(name: str) -> tuple:
    # gd = GLACIER_DATA.query(f"NAME == {name}")
    gd = GLACIER_DATA.loc[GLACIER_DATA["NAME"] == name]
    return gd.iloc[0]["LATITUDE"], gd.iloc[0]["LONGITUDE"]

if __name__ == "__main__":
    # print(GLACIER_DATA)
    thunder = get_lat_long("THUNDER")
    print(thunder)

    # for col in GLACIER_DATA.columns:
    #     print(len(col))
    elevation.clip(bounds=(thunder[0] - 0.1, thunder[1] - 0.1, thunder[0] + 0.1, thunder[1] + 0.1), output='test.tif')

    elevation.clean()
    # elevation_function(get_lat_long("THUNDER"))
    # print(get_lat_long("NO 4"))


    # print(df)