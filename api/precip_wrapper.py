from datetime import date
from datetime import timedelta
from enum import Enum
from typing import Union
import urllib3
import json

''' 
This is a wrapper for the NASA Global Precipitation Measurement, which can be
found here https://gpm.nasa.gov/data/directory. The documentation for the
source api can be found here https://pmmpublisher.pps.eosdis.nasa.gov/docs. The
wrapper is used in glacier_api.py to serve plots.
'''

Accum = {
            "30min": "precip_30mn",
            "3hr": "precip_3hr",
            "1d_3hr": "precip_3hr_1d",
            "3d": "precip_3d",
            "7d": "precip_7d"
            }

FileType = Enum('File', ['PNG', 'TIFF', 'GZIP'])

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
                 limit: int,
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

        # urllib manager
        self._http = urllib3.PoolManager()
        
    def get_data_url(self) -> str:
        """
        This function is responsible for getting the download link
        corresponding to the file type class attribute.

        Returns
        -------
        str
            URL to download from.
        """

        try:
            response = self._send_request()
        except Exception as err:
            print(f"Error trying to get url:\n {err}")
            return None

        json_data = json.loads(response.data.decode("utf-8"))["items"]
        url = None

        if len(json_data) == 0:
            return None
        json_data = json_data[0]

        if self.file_type is FileType.PNG:
            url = json_data["image"][0]["url"]
        elif self.file_type is FileType.TIFF:
            url = json_data["action"][1]["using"][1]["url"]
        elif self.file_type is FileType.GZIP:
            url = json_data["action"][1]["using"][0]["url"]

        return url

    def _send_request(self) -> urllib3.response.HTTPResponse:
        """
        This function is responsible for building the url and sending a request
        to the site.

        Returns
        -------
        HTTPResponse
            The function returns an http response from the site. 
        """

        base = "https://pmmpublisher.pps.eosdis.nasa.gov/opensearch"
        fields = {"q": self.q,
                  "lat": self.lat,
                  "lon": self.lon,
                  "limit": self.limit,
                  "startTime": self.start_time,
                  "endTime": self.end_time}
        response = self._http.request("GET", base, fields=fields)

        if (response.status != 200):
            raise Exception(f"Error with http get request (status {response.status}):\n" + str(response.data))

        return response


def precip_test():
    test1 = Precip(Accum["30min"],  30,     -100,      1, date.today(), date.today(), FileType.PNG)
    test2 = Precip(Accum["3hr"],   -29.3432,  33.5,    1, date.today(), date.today(), FileType.TIFF)
    test3 = Precip(Accum["1d_3hr"], 38.2098, -3.309,   2, date.today(), date.today(), FileType.GZIP)
    test4 = Precip(Accum["3d"],     83.399,  -150.093, 5, date.today(), date.today(), FileType.PNG)
    test5 = Precip(Accum["30min"],  0,        0,       1, date.today(), date.today(), FileType.TIFF)
    test6 = Precip(Accum["30min"], -90,      -180,     1, date.today(), date.today(), FileType.TIFF)
    print(test1.get_data_url())
    print(test2.get_data_url())
    print(test3.get_data_url())
    print(test4.get_data_url())
    print(test5.get_data_url())
    print(test6.get_data_url())


if __name__ == "__main__":
    precip_test()







