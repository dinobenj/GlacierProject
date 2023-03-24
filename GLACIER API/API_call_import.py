# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:07:34 2023

@author: klinga

This file contains the get_geotiff function 
which handles the precipitation data API request
"""

# module for API requesting
import requests

# parameters: latitude and longitude values
# returns a link to download a geotiff file
def get_geotiff(lat, long):

    # queries are the parameters we are asking the API fore
    query = {'q': 'precip_30mn', 'lat': lat, 'lon': long, 'startTime': '2023-03-14', 'endTime': '2023-03-16'}
    
    # storing the API reponse as a JSON file
    response = requests.get('https://pmmpublisher.pps.eosdis.nasa.gov/opensearch', params=query)
    data = response.json()

    # PARSING 

    # information part of the API call
    api_info = data['items']

    # data retrieval part of information
    data_retrieve = api_info[0]['action'][1]

    # information on different file formats
    file_info = data_retrieve['using']

    # geotiff file retrieval
    geotiff_info = file_info[1]

    # geotiff file 
    file = geotiff_info['url']
        
    return file
  
   