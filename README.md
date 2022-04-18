
# Earth Lab + RIMORPHIS

_Authors: Avra Saslow & Kristen Tortorelli_

This repository is for a research project for improving flood detection with a focus on comparing stream gage discharge data against satellite imagery in order to determine at which point we can detect overbank flooding. We're working in conjunction with the NSF funded project [RIMORPHIS](https://rimorphis.org/) to ultimately assist in modeling streamflow and overbank flooding across the US.

This workflow utilizes both Google Earth Engine (GEE) and the National Water Information System (NWIS)

## Input Data Required

### NWIS Data
Stream discharge and gage height data for the Vicksburg gage site on the Mississippi River can be downloaded as TSV files from the following site: 
(https://waterdata.usgs.gov/nwis/inventory/?site_no=07289000&agency_cd=USGS)

Gage height data for the Yankton SD gage site on the Missour River near the Gavins Pt Dam can be downloaded as TSV files from the following site: 
(https://nwis.waterdata.usgs.gov/nwis/inventory/?site_no=06467500&agency_cd=USGS)

This project's notebooks use the hydrofunctions library from USGS to extract stream discharge and gage height data for all sites. 

### Sentinel-2 data

Sentinel-2 data over the Vicksburg gage site and the Yankton SD gage site can be downloaded from the https://earthexplorer.usgs.gov/ site. 

This project's notebooks use Google Earth Engine to download Sentinel-2 images for all sites over a number of date ranges. 

## Development Environment
The notebooks were developed using Python 3.9.5 on a Mac system. The workflow utilizes packages from NumPy, EarthPy, Hydrofunctions, Folium, Geemap, and Matplotlib. The workbook was developed using the [earth-analytics-python environment](https://github.com/earthlab/earth-analytics-python-env).

Installation instructions for the earth analytics python environment can be found here: (https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/).

## Workflow 

1. Use hydrofunctions library to download stream gage data for each location, save to pd dataframe
2. Pick time series for that river location (1-2 years)

Stream gage analysis
3. Plot the time series of discharge (matplotlib), observe patterns, seasonality, progression of discharge/gage height, etc.
4. Select time period (6  months) around flood event and extract max discharge value for each month
5. Save max discharge values to new pd dataframe

Satellite analysis
6. Generate images for each site that match dates of high discharge values for each month of time period (6 months)
7. Filter/clean up images as required (remove clouds, etc...)
8. Classify water pixels for each image, generate water pixel counts 
9. Save water pixel count values to max discharge dataframe, append with date column

10. Plot max discharge values for each location on x-axis vs flooded extent (water pixel count) on y-axis using matplotlib


## Notebooks
Additional "explorations" notebooks have been included showing more of the process completed to finalize the workflow.

Combined workflow: RIMORPHIS workflow.ipynb

Hydrofunctions workflow: Hydrofunctions_discharge_KJT_04032022.ipynb

Google Earth Engine workflow: GEE_sentinel2_MSgage_KJT_04032022.ipynb


## References

