# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:15:30 2023

@author: klinga

GlacierProject

In this file, I am figuring out how to import json files and manipulate
the data from json files.

Our API data is giving us a json file.
"""

import json

# opening and reading the json file
file = open("Testing w- JSON.postman_collection.json")

# API data imports to python as a dictionary
data_dict = json.load(file)

# let's see what data the json file is giving us
for dat in data_dict.keys():
    print(dat, data_dict[dat])
    
print(list(data_dict.keys()))

# we can see that the 'info' key has a dictionary for the value
# and that the key 'item' has a list of dictionaries as the value
# the 'item' key contains information on what we are importing
#   into Postman (what API we are requesting)




