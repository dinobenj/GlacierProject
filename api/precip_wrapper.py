import requests
from datetime import date
from datetime import timedelta
from enum import Enum
from typing import Union

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

FileType = Enum('File', ['PNG', 'TIFF', 'JSON'])

class Precip:
    '''
    This class is the wrapper for the api. The constructor takes in args used
    for the api. Accumulation type and location data are required parameters,
    the rest are optional and have default initializations. 
    '''
    def __init__(self, 
                 q: str,
                 lat: float,
                 lon: float,
                 limit: Union[int, None],
                 start_time: Union[date, None],
                 end_time: Union[date, None],
                 file_type: FileType):
        
        # The type of accumulation query
        self.q  = q

        # Location data
        self.lat = lat
        self.lon = lon
        
        # Query count limit for api.
        self.limit = limit
        
        # The start time must be at most 60 days from the current day.
        if start_time is None or start_time <= (date.today() - timedelta(days=60)):
            self.start_time = date.today()
        else:
            self.start_time = start_time
        
        # If the end time is at or before the start time, set the end time to be a day after.
        if end_time is None or end_time <= self.start_time:
            self.end_time = self.start_time + timedelta(days=1)
        else:
            self.end_time = end_time
        
        # File type to save
        self.file_type = file_type
        
    def send_request(self):
        pass

def precip_test():
    test1 = Precip(accum["30min"], -100,     -100,     None, date.today(), date.today(), FileType.PNG)
    test2 = Precip(accum["3hr"],   -129.3432, 33.5,    None, date.today(), date.today(), FileType.TIFF)
    test3 = Precip(accum["1d_3hr"], 38.2098, -3.309,   2,    date.today(), date.today(), FileType.JSON)
    test4 = Precip(accum["3d"],     103.399, -150.093, 5,    date.today(), date.today(), FileType.PNG)
    test5 = Precip(accum["30min"],  0,        0,       1,    date.today(), date.today(), FileType.TIFF)
    test6 = Precip(accum["30min"],  180,     -180,     None, date.today(), date.today(), FileType.TIFF)
    print(test1.start_time, test1.end_time)

if __name__ == "__main__":
    precip_test()







