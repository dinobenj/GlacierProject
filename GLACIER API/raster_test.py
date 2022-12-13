# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

image = Image.open(r"elevation.png").convert("RGB")
edges = image.filter(ImageFilter.FIND_EDGES)
edges.save(r"raster_test_out.png")
