# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:49:51 2023

@author: klinga

Original code in api_call_only_python.py

Creating a function to open and graph 
precipitation data from API 
"""

# module for making API data calls
import requests

# module for getting current date for API Call
from datetime import date
from datetime import timedelta

# module for creating datatset ranges
import numpy as np

# module for opening geotiff files
import rasterio

# module for converting geotiff data into data 
# that numpy and matplotlib can use
from affine import Affine

# module for graphing 
import matplotlib.pyplot as plt
import matplotlib.colors as colors


# this function handles the API data request
# parameters: latitude and longitude for the location
# we want precipitation data for
# returns a geotiff file 
def get_geotiff(lat, long):

    # getting today's and yesterday's date
    today = date.today()
    yesterday = today - timedelta(days=1)
    # queries are the parameters we are asking the API for
    query = {'q': 'precip_30mn', 'lat': lat, 'lon': long, 'startTime': yesterday, 'endTime': today}
    
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
  


def graph_precip(lat, long):
    
    # directory path and file name
    path = ''
    file_in = get_geotiff(lat, long)

    # read in file with geotiff precipitation data
    tiff_data = rasterio.open(path + file_in)

    # retrieve the affine transformation
    # so it can be printed by matplotlib
    if isinstance(tiff_data.transform, Affine):
         transform = tiff_data.transform
    else:
         transform = tiff_data.affine

    # find the limits of the dataplot 
    N = tiff_data.width
    M = tiff_data.height
    dx = transform.a
    dy = transform.e
    minx = transform.c
    maxy = transform.f

    # read the image data, flip upside down if necessary
    data_in = tiff_data.read(1)
    if dy < 0:
      dy = -dy
      data_in = np.flip(data_in, 0)

    # generate X and Y grid locations
    # for matplotlib printing
    xdata = minx + dx/2 + dx*np.arange(N)
    ydata = maxy - dy/2 - dy*np.arange(M-1,-1,-1)

    # scale the precipitation data for nicer visualization 
    d = np.log(np.clip(data_in, 1, 1000))
    data_scale = (255*(d - np.amin(d))/np.ptp(d)).astype(np.uint8)


    # construct an RGB table over a range of 1000
    # finding an array of evenly spaced numbers over an interval
    precip = np.exp(np.linspace(np.log(1), np.log(1000), num=256))
    # storing this evenly spaced array
    hue = np.arange(256)/255.0
    # making sure all values are "bucketed" into one of the intervals
    # in the evenly spaced array
    sat = np.clip(1./3 + precip/187.5, 0, 1)
    # creating an array of zeroes 
    value = np.zeros(256) + 0.75
    # combining the array of zeroes and the evenly spaced array
    hsv = np.stack((hue, sat, value), axis=1)
    # coloring the combined array based on "buckets"
    rgb = colors.hsv_to_rgb(hsv)
    # making the default color white 
    rgb[0,:] = 1
    # creates the plot of the combined array in color
    cmap = colors.ListedColormap(rgb, name='precipitation')


    # GRAPHING 

    # figure out the graph limits
    extent = [xdata[0], xdata[-1], ydata[0], ydata[-1]]
    # create the plot object 
    plt.figure(figsize=(8,8))
    # show the plot
    fig = plt.imshow(data_scale, extent=extent, origin='lower', cmap=cmap)
    # aesthetics 
    plt.title('Precipitation Map at Latitude ' + str(lat) + ' and Longitude ' + str(long))
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)

    # save graph
    plt.savefig("python_sample.png", dpi=300, bbox_inches='tight', pad_inches=0.5)
    # show graph 
    plt.show()


graph_precip(47.6062, 122.3321)