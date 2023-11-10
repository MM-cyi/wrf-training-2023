## Import packages

import os # something very general

import matplotlib.pyplot as plt     #for plotting
from matplotlib.cm import get_cmap

import cartopy.crs as crs    #for geography maps
from cartopy.feature import NaturalEarthFeature

from netCDF4 import Dataset   #netCDF4 library and wrf-python
from wrf import (getvar, ALL_TIMES)

import xarray as xr

## Define my own custom filepath, from where I should ingest wrf data
myPath   = r'/home/olddog/Documents/Python_Scipts/WRF_nesting_prediction_Web/dataTest'
filename = 'wrfout_d03_2022-05-07_01:00:00'
## Read in the file
ncfile = Dataset(os.path.join(myPath, filename))




varname = 'p'
# 
data = getvar(ncfile, varname, timeidx=ALL_TIMES)


### Start slicing data, using index selection
nz = 0
sliced = data.isel(bottom_top=nz, Time=10)



sliced.plot()
del sliced




sliced = data.isel(bottom_top=0, Time=10)
sliced = sliced/100                     # convert from Pa to hPa
sliced.attrs['units'] = 'hPa'          # update units
sliced.XLONG['name'] = 'longitude'


plt.figure(figsize=(7, 7))
ax = plt.axes(projection=crs.PlateCarree())

cbar_kwargs = {'orientation':'horizontal', 'shrink':0.9, 'aspect':50, 'pad':.1 , 'label':'Pressure in hPa'}
sliced.plot(x='XLONG', y='XLAT',ax=ax, robust=True, cmap = 'Oranges_r', cbar_kwargs=cbar_kwargs)

ax.coastlines(resolution='10m')
gl = ax.gridlines(draw_labels=True)
gl.top_labels = False
gl.right_labels = False


title_string = "Variable {}, at time {}\nVertical Level index: {}".format(sliced.name, str(sliced.Time.values).split(':')[0], nz)
ax.set_title(title_string)







