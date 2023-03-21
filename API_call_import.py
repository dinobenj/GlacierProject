# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:07:34 2023

@author: klinga
"""

import requests

def get_geotiff(lat, long):

    # current lat = 59.58985
    # current long = -138.6278
    
    # queries are the parameters we are asking the API fore
    query = {'q': 'precip_30mn', 'lat': lat, 'long': long, 'startTime': '2023-02-17', 'endTime': '2023-02-23'}
    
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
    
    # requesting file data
    geo = requests.get(file)
    
    # creating a file
    ret_file = open('precip_geotiff.tif').write(geo.content)
        
    return ret_file
