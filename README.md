# Earth Lab + RIMORPHIS
Authors: Avra Saslow & Kristen Tortorelli

  > This repository is for a research project for improving flood detection with a focus on comparing stream gage discharge data against satellite imagery in order to determine at which point we can detect overbank flooding. We're working in conjunction with the NSF funded project RIMORPHIS to ultimately assist in modeling streamflow and overbank flooding across the US.

This workflow utilizes both Google Earth Engine (GEE) and the National Water Information System (NWIS).

## Table of Contents
* [Development Environment](https://github.com/earthlab-education/final-project-group-blog-post-rimorphis#development-environment)
* [Workflow](https://github.com/earthlab-education/final-project-group-blog-post-rimorphis#workflow)
* [Notebooks](https://github.com/earthlab-education/final-project-group-blog-post-rimorphis#notebooks)
* [References](https://github.com/earthlab-education/final-project-group-blog-post-rimorphis#references)
* [Contact](https://github.com/earthlab-education/final-project-group-blog-post-rimorphis#project-contacts)

## Data Sources
### NWIS Data

The National Water Information System (NWIS) provides access to water-related data at over 1.5 million sites in the United States, and therefore can provide stream gage discharge data and gage height data. This project's notebooks use the hydrofunctions library from USGS to extract stream discharge and gage height data for all sites.

* [Stream discharge and gage height data for the Vicksburg, Mississippi gage site](https://waterdata.usgs.gov/nwis/inventory/?site_no=07289000&agency_cd=USGS)
* [Gage height data for Pine Bluff, Arkansas gage site](https://waterdata.usgs.gov/usa/nwis/uv?site_no=07263650)


### Sentinel-2 data

Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission which supports the monitoring of vegetation, soil and water cover. Sentinel-2 data over both gage sites can be downloaded from the https://earthexplorer.usgs.gov/ site. This project's notebooks use Google Earth Engine to download Sentinel-2 images for all sites over a number of date ranges.

## Development Environment
The notebooks were developed using Python 3.9.5 on a Mac system. The workflow utilizes packages from Google Earth Engine, Hydrofunctions, Folium, Geemap, and Matplotlib. The workbook was developed using the earth-analytics-python environment.

Installation instructions for the earth analytics python environment can be found [here.](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/)

## Workflow

![workflow diagram](Assets/workflow.png)


## Notebooks
Additional "explorations" notebooks have been included showing more of the process completed to finalize the workflow.

* Hydrofunctions workflow: Hydrofunctions Exploratory Notebook.ipynb
* Google Earth Engine workflow: Google Earth Engine Exploratory Notebook.ipynb
* Time series automation workflow: Automation Workflow.ipynb

## References

## Project Contacts

[@Avra Saslow](mailto:avra.saslow@colorado.edu)<br>
[@Kristen Tortorelli](mailto:kristen.tortorelli@colorado.edu)<br>
[@Elsa Culler](mailto:elsa.culler@colorado.edu )<br>