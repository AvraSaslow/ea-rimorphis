# Earth Lab + RIMORPHIS: How Much Water Makes a Flood?

Authors: Avra Saslow & Kristen Tortorelli

  > This repository is for a research project that aims to improve flood detection with a focus on comparing stream gage discharge data against satellite imagery in order to determine at which point we can detect overbank flooding. We're working in conjunction with the NSF funded project [RIMORPHIS](https://rimorphis.org/) to ultimately assist in modeling streamflow and overbank flooding across the US.

This workflow utilizes both Google Earth Engine (GEE) and the National Water Information System (NWIS).

## Table of Contents
* [Project Purpose and Goals](https://github.com/AvraSaslow/ea-rimorphis#project-purpose-and-goals)
* [Repository Organization](https://github.com/AvraSaslow/ea-rimorphis#repository-organization)
* [Development Environment](https://github.com/AvraSaslow/ea-rimorphis#development-environment)
* [Workflow](https://github.com/AvraSaslow/ea-rimorphis#workflow)
* [Example Usage](https://github.com/AvraSaslow/ea-rimorphis#example-usage)
* [Data Sources](https://github.com/AvraSaslow/ea-rimorphis#data-sources)
* [Contact](https://github.com/AvraSaslow/ea-rimorphis#project-contacts)
* [Citation](https://github.com/AvraSaslow/ea-rimorphis#zenodo-citation)

## Project Purpose and Goals
The premise of this research project is to contextualize flooding with satellite data, rather than relying on stream gage data to indicate whether or not water levels are above a flood threshold. It's important to model overbank flooding because it's crucial to understand _where_ and _how_ exactly a landscape floods. The ability to monitor and predict the extent of flooding across a landscape is critical for managing phenomena such as agricultural irrigation and habitat conservation.

This cannot just be done with stream gage data; stream gage data only tells us when the water level or flow is above a certain threshold. Moreover, gauging stations generally fail to provide accurate flow observations during extreme events due to the distributed complex nature of flood processes.

Utilizing other data types, such as satellite imagery, can provide a better understanding of how rivers flood. It's important to see not only where on a floodplain the water travels to, but where that water carries sediment loads to as well. That's why our research is comprised of modelling where stream gage data (i.e., water volume) and satellite imagery (i.e., water area) converge, because it could give us a better understanding of _where_ water and and sediment go when water levels hit a flood level threshold.

This research sits under the umbrella of a larger research effort called the River Morphology Information System, or RIMORPHIS, which is a USF-funded, collaborative project. The goal of RIMORPHIS is to create a user-friendly information system that enables its community to observe and record important variables for modeling streamflow and sediment transport across the U.S.

Our piece of research fits into that mission because it evaluates if multiple methods of measurement create a stronger and more accurate model for overbank flooding, rather than relying on a single data point (such as precipitation, or stream gage data).

To narrow our scope of work, we decided to specifically study flood events at 1-3 locations that had both stream gage or stream height data and clear enough satellite images. For this stage in our study, we're simply looking to find if there is any correlation between stream gage/height data and the number of water pixels counted for the same time period in the study area.

## Repository Organization

This repository has a few organizational notebooks that comprise of the project. These include:

* Two folders for all presentations and intermediary reports
* An assets folder for all images related to the project
* A folder comprised of exploratory notebooks that were used to develop the analysis:
* Folder for the final blog that details the project:
  * Contains images within blog, final blog ipynb and html files, and python notebooks

Unless you want to replicate the project yourself or look through the intermediary steps, the only directory you'll need to navigate to is the [final blog](https://github.com/AvraSaslow/ea-rimorphis/tree/main/Final%20Blog). This has both the write-up explaining the project and the python notebooks for you to actually run through the code and workflow. 

## Development Environment
The notebooks were developed using Python 3.9.5 on a Mac system. The workflow utilizes Anaconda, and packages from Google Earth Engine, [Hydrofunctions](https://pypi.org/project/hydrofunctions/), [Folium](https://pypi.org/project/folium/), [Geemap](https://geemap.org/), and [Matplotlib](https://matplotlib.org/stable/users/installing/index.html). The workbook was developed using the earth-analytics-python environment.

Installation instructions for the earth analytics python environment can be found [here.](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/)


## Workflow

### How to Run Workflow
Simply follow the instructions to run the code for this project from source above:

* Ensure that the earth analytics python environment mentioned above is set up on your local machine. Use `conda activate <yourenvironmentname>` to activate the environment
* Clone this repository onto your local machine
* Run `jupyter notebook` within this repository's folder in terminal
* Wait for the Jupyter Notebook GUI to load - navigate to the ipynb files in the [Final Blog/Python Notebooks folder](https://github.com/AvraSaslow/ea-rimorphis/tree/main/Final%20Blog) of the repository 
    * rimorphis_mississippi_images_tortorelli_saslow.ipynb: This notebook generates true color, NDWI, and water maps for the Vicksburg Mississippi site
    * rimorphis_mississippi_pixel_count_vs_gage_plot_tortorelli_saslow.ipynb: This notebook uses hydrofunctions data and water pixel count functions to generate final pixel vs gage data plot for Vicksburg Mississippi site
    * rimorphis_pinebluff_images_tortorelli_saslow.ipynb: This notebook generates true color, NDWI, and water maps for the Pine Bluff Arkansas site
    * rimorphis_pinebluff_pixel_count_vs_gage_plot_tortorelli_saslow.ipynb: This notebook uses hydrofunctions data and water pixel count functions to generate final pixel vs gage data plot for Pine Bluff Arkansas site 
* Navigate to desired notebook listed above, and then navigate to the kernel in the menu, and run all code cells. It will pause when it gets to the Google Earth Engine code snippet. This will require you to provide credentials for Google Earth Engine and copy an authentication code into the notebook to continue running the notebook.
* Final Blog ipynb and html files have images embedded in markdown. Images contained within final blog files are in Final Blog folder. 

![workflow diagram](Assets/workflow.png)

## Example Usage
Since this project uses the GEE package to view and analyze Sentinel-2 data, and the hydrofunctions package to export and analyze stream gage data, there are no data download requirements to run this project's workflow. To run the images workflow (see 'rimorphis_mississippi_images_tortorelli_saslow.ipynb' under [Final Blog/Python Notebook](https://github.com/AvraSaslow/ea-rimorphis/tree/main/Final%20Blog), [select a river gage monitoring site](https://dashboard.waterdata.usgs.gov/app/nwd/?region=lower48&aoi=default) to analyze. Find geographical coordinates for a rectangle surrounding your desired study area, and insert coordinates into notebook. Navigate to the notebook's kernel and run all code cells. You may need to adjust wet and dry season start and end dates to reflect the area's actual seasons. 

Once you have generated desired images, you can also run the pixel count versus gage data notebook. Navigate to the 'rimorphis_mississippi_pixel_count_vs_gage_plot_tortorelli_saslow' file in the same folder, and insert river gage monitoring site number and coordinates. Run all code cells to generate plots. Depending on what measurements are available for your USGS gage site, you may need to adjust which hydrofunctions function is called (refer to 'hydrofns.py' file in main folder) to export stream gage data. Adjust date variables as desired to study different time periods. 

## Data Sources
### NWIS Data

The National Water Information System (NWIS) provides access to water-related data at over 1.5 million sites in the United States, and therefore can provide stream gage discharge data and gage height data. This project's notebooks use the hydrofunctions library from USGS to extract stream discharge and gage height data for all sites.

* [Stream discharge and gage height data for the Vicksburg, Mississippi gage site](https://waterdata.usgs.gov/nwis/inventory/?site_no=07289000&agency_cd=USGS)
* [Gage height data for Pine Bluff, Arkansas gage site](https://waterdata.usgs.gov/usa/nwis/uv?site_no=07263650)


### Sentinel-2 data

Sentinel-2 is a wide-swath, high-resolution, multi-spectral imaging mission which supports the monitoring of vegetation, soil and water cover. Sentinel-2 data over both gage sites can be downloaded from the https://earthexplorer.usgs.gov/ site. This project's notebooks use Google Earth Engine to download Sentinel-2 images for all sites over a number of date ranges.


## Project Contacts

[@Avra Saslow](mailto:avra.saslow@colorado.edu)<br>
[@Kristen Tortorelli](mailto:kristen.tortorelli@colorado.edu)<br>
[@Elsa Culler](mailto:elsa.culler@colorado.edu )<br>

## Zenodo Citation
[![DOI](https://zenodo.org/badge/495654495.svg)](https://zenodo.org/badge/latestdoi/495654495)
