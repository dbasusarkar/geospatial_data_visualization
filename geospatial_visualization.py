import pandas as pd
import geopandas as gpd
import geoplot as gplt
import folium
import shapely
import contextily as ctx
from contextily import Place
import xyzservices.providers as xyz
import mapclassify as mc
import matplotlib.pyplot as plt
import numpy as np
import math

world_map = gpd.read_file(gplt.datasets.get_path('world'))

world_map.boundary.plot(edgecolor = 'black')
plt.ylabel("Longitude in degrees (" + u"\u00B0" + ")")
plt.xlabel("Latitude in degrees (" + u"\u00B0" + ")")
plt.savefig('world_map.boundary.pdf')
plt.savefig('world_map.boundary.jpg')

world_map.plot(cmap = 'viridis', figsize = (16, 10))
plt.ylabel("Longitude in degrees (" + u"\u00B0" + ")")
plt.xlabel("Latitude in degrees (" + u"\u00B0" + ")")
plt.savefig('world_map.plot.pdf')
plt.savefig('world_map.plot.jpg')

ax = world_map.plot(cmap='viridis', figsize=(16, 10))
world_map.boundary.plot(ax=ax, edgecolor='black')
plt.ylabel("Longitude in degrees (" + u"\u00B0" + ")")
plt.xlabel("Latitude in degrees (" + u"\u00B0" + ")")
plt.savefig('./world_map.boundary.plot.pdf')
plt.savefig('./world_map.boundary.plot.jpg')



