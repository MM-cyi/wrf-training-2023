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
filename = 'wrfout_d03_2022-05-06_01:00:00'



## Read in the file
ncfile = Dataset(os.path.join(myPath, filename))


varname = 'p'

# 
data = getvar(ncfile, varname, timeidx=ALL_TIMES)



## Print basic info
print('User requested "{}"'.format(varname))
print(data.dims, data.coords)




nr_variables = len(ncfile.variables)
first_N_variables = 30

print("Filename {} contains {} variables.\n-->At the moment, the user exported only variable {}".format(filename, nr_variables, varname) )


ds = xr.open_dataset(os.path.join(myPath, filename))
c = 1
print('\nExtracting first {} variable names...'.format(first_N_variables))
for item in list(ds.variables)[0:first_N_variables]:
    print("{:2d}) {}".format(c, item))
    _temp = getvar(ncfile, varname, timeidx=ALL_TIMES)
    print(_temp.coords)   
    print("{} in {}".format(_temp.description,_temp.units ))
        
    print("")
    c=c+1
    
    
    
has_vert = []
for item in ds:
    if 'bottom_top' in ds[item].dims: 
        has_vert.append(item)
print("{} variables out of {} have a vertical dimension (counting only unstaggered)".format(len(has_vert), len(ds)))            



# WRF-python is built on xarray and, thus, accepts same syntax and commands: 
# Lets try slicing the data:

# Does the data have vertical dimension?? Let us code something that is flexible enough to understand it, and act accordingly

if "bottom_top" in data.dims:
    sliced = data.isel(Time=0, west_east = 20, south_north=25, bottom_top=1)
    print('Exctrating indices!')
    print('\tTime:0')
    print('\tx:20')
    print('\ty:25')
    print('\tz:1')
else:
    sliced = data.isel(Time=0, west_east = 20, south_north=25)
    print('Exctrating indices!')
    print('\tTime:0')
    print('\tx:20')
    print('\ty:25')
    print('\tVariable {} has NO vertical cooridnate'.format(varname))
print('**AFTER** the slicing, the dimensional rank was reduced and the original time-varying datacube is now... a point\nIf we print its description we have:\n')
print(sliced)

