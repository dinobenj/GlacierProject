import requests
from datetime import date
from datetime import timedelta

''' 
This is a wrapper for the NASA Global Precipitation Measurement, which can be
found here https://gpm.nasa.gov/data/directory. The documentation for the
source api can be found here https://pmmpublisher.pps.eosdis.nasa.gov/docs. The
wrapper is used in glacier_api.py to serve plots.
'''
accum = {
            "30min": "precip_30mn",
            "3hr": "precip_3hr",
            "1d_3hr": "precip_3hr_1d",
            "3d": "precip_3d",
            "7d": "precip_7d"
            }

class Precip:
    def __init__(self):

        self.q = None
        self.lat = None
        self.lon = None 
        self.limit = None 
        self.start_time = date.today()
        self.end_time = date.today() + timedelta(days=5)


a = Precip()
print(a.start_time, a.end_time)

