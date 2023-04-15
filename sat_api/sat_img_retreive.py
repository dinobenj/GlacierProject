# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:18:23 2023

@author: klinga

This code accesses the satellite images via API 
and saves them to this device 

Code adapted from NASA Gibs website
"""

# for requesting image from API
import urllib.request

# python library for accessing API data 
from owslib.wms import WebMapService

# image display library 
from IPython.display import Image, display

# module for getting current date for API Call
from datetime import date
from datetime import timedelta



def get_sat_img (lat, long):
    
    # connecting to the API
    wms = WebMapService('https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?', version='1.1.1')

    # figuring out the time parameter for the API request
    today = date.today()
    yesterday = today - timedelta(days=1)

    # make request for MODIS_Terra_CorrectedReflectance_TrueColor
    # meaning: satellite image of requested coordinates in real life color
    img = wms.getmap(layers=['MODIS_Terra_CorrectedReflectance_TrueColor'],  # layers
                 srs='epsg:4326',  # geopgraphical projection of the image
                 bbox=(long-2,lat-2,long+2,lat+2),  # latitude and longitude bounds (format: long min, lat max, long max, lat max)
                 size=(400, 400),  # image size
                 time=yesterday,  # time of data
                 format='image/png',  # image format
                 transparent=True)  # Nodata transparency

    # saving image as a PNG
    out = open('C:/Users/klinga/GlacierProject/MODIS_Terra_CorrectedReflectance_TrueColor.png', 'wb')
    out.write(img.read())
    out.close()

    # displaying the image 
    Image('C:/Users/klinga/GlacierProject/MODIS_Terra_CorrectedReflectance_TrueColor.png')

# format: lat, long
get_sat_img(-3.4653, 62.2159)
