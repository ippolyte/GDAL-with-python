#
# GDAL Tutorial 
# Created on November 27th 2019 (Thanksgiving)
# by Aggeliki Barberopoulou
# GDAL Getting Dataset Information
#
# This code can be executed from within the python console in qgis
# Later versions might also be provided for running this externally
# but this code has not been tested outside of qgis python console

# It is considered good Python form to only
# import what you actually use
import os
# From open street geospatial foundation libraries
# import gdal library
from osgeo import gdal


# Enter your tif image full path filename here
# No spaces between r and the path

path=r"Z:\Personal\abarberopoulou\project" # make sure to change this to where your files reside

# Change to the path of your files and python script
os.chdir(path)

filename="cropped.tif"

# open file for reading only
dataset = gdal.Open(filename, gdal.GA_ReadOnly)

# Check that the dataset was successfully opened
if not dataset:
    print("Unable to open ",filename," file")
    sys.exit(1)

# if the dataset does exist in our working directory
# provide its type of file

print("Driver: {}/{}".format(dataset.GetDriver().ShortName,
                             dataset.GetDriver().LongName))
                                                         

# Print size of raster
print("Size is {} x {} x {}".format(dataset.RasterXSize,
                                    dataset.RasterYSize,
                                    dataset.RasterCount))
                                    
# print projection information for this file
# printing on the screen is pretty long
print("Projection is {}".format(dataset.GetProjection()))

# use geotransform() to convert
# from map to pixel coordinates

# Here is what geotransform corresponds to
# geotransform[0] = top left x
# geotransform[1] = w-e pixel resolution
# geotransform[2] = 0
# geotransform[3] = top left y
# geotransform[4] = 0
# geotransform[5] = n-s pixel resolution (negative value)

geotransform = dataset.GetGeoTransform()
if geotransform:
    print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
    print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))

for bandno in range(1,7):
    print("Band={}".format(bandno))
    band = dataset.GetRasterBand(bandno)
    print("Band Type={}".format(gdal.GetDataTypeName(band.DataType)))

    min = band.GetMinimum()
    max = band.GetMaximum()
    if not min or not max:
        (min,max) = band.ComputeRasterMinMax(True)
    print("Min={:.3f}, Max={:.3f}".format(min,max))
      
    if band.GetOverviewCount() > 0:
        print("Band has {} overviews".format(band.GetOverviewCount()))
      
    if band.GetRasterColorTable():
        print("Band has a color table with {} entries".format(band.GetRasterColorTable().GetCount()))

# Display QGIS message
print(
"""
# Run inside QGIS at Plugins->Open python console >>> prompt
import os # make os functions avaliable here
os.chdir('C:\kokos') # change to working folder
execfile('gdal_tutorial.py') # run your code Python2 QGIS 2.x OR
exec(open('gdal_tutorial.py').read()) # run your code Python3 QGIS 3.x
"""
)
##
## Output :
##
## Driver: GTiff/GeoTIFF
## Size is 1600 x 1600 x 6
## Projection is PROJCS["WGS 84 / UTM zone 35N",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",27],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",500000],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Easting",EAST],AXIS["Northing",NORTH],AUTHORITY["EPSG","32635"]]
## Origin = (211665.0, 3950115.0)
## Pixel Size = (30.0, -30.0)
# # Band=1
# # Band Type=UInt16
# # Min=8046.000, Max=42948.000
# # Band=2
# # Band Type=UInt16
# # Min=6687.000, Max=44500.000
# # Band=3
# # Band Type=UInt16
# # Min=5848.000, Max=47107.000
# # Band=4
# # Band Type=UInt16
# # Min=5488.000, Max=41720.000
# # Band=5
# # Band Type=UInt16
# # Min=5107.000, Max=26690.000
# # Band=6
# # Band Type=UInt16
# # Min=5011.000, Max=23497.000
# # Band=7
## # Run inside QGIS at Plugins->Open python console >>> prompt
## import os # make os functions available here
## os.chdir('C:\kokos') # change to working folder
## execfile('gdal_tutorial.py') # run your code Python2 QGIS 2.x OR
## exec(open('gdal_tutorial.py').read()) # run your code Python3 QGIS 3.x
