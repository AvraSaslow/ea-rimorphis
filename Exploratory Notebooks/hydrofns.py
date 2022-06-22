#!/usr/bin/env python
# coding: utf-8

# Import libraries
import hydrofunctions as hf

# function that finds stream gage data for any given site and time frame
def create_stream_gage_df(site, start, end):
    """Imports data to dataframe, adds geolocation and stream gage site name

    Parameters
    ----------
    site : string
        Site number as specified by USGS

    start : string
        Desired start date for data

    end : string
        Desired end date for data 

    Returns
    -------
    response_df : dataframe
        Dataframe created from downloaded csv    """

    if start > end:
        print("Start date must be prior to end date.")
        
    else:
        try:
            # Generate dataframe from NWIS for gage discharge data at specified sites
            response = hf.NWIS(site, 'dv', start, end, parameterCd='00060')
            response_df = response.df()
        except ValueError:
            print("This site number does not exist. Please use a valid NWIS site number.")

        # Rename columns for discharge and flags
        response_df.columns = ('discharge', 'qualifiers')

        # Add column for site name
        response_df["sitename"] = hf.get_nwis_property(
            response.json, key='siteName')[0]

        # Add columns for gage location latitude and longitude
        geolocation = hf.get_nwis_property(response.json, key='geoLocation')[0]
        response_df["latitude"] = geolocation["geogLocation"]["latitude"]
        response_df["longitude"] = geolocation["geogLocation"]["longitude"]

        return response_df

# function that finds stream gage height data for any given site and time frame


def create_df_gageht(site, start, end):
    """Imports data to dataframe, adds geolocation and stream gage height site name

    Parameters
    ----------
    site : string
        Site number as specified by USGS

    start : string
        Desired start date for data

    end : string
        Desired end date for data 

    Returns
    -------
    response_df : dataframe
        Dataframe created from downloaded csv    """
    if start > end:
        print("Start date must be prior to end date.")
        
    else:
        try:
            # Generate dataframe from NWIS for gage discharge data at specified sites
            response = hf.NWIS(site, 'dv', start, end, parameterCd='00065')
            response_df = response.df()
        except ValueError:
            print("This site number does not exist. Please use a valid NWIS site number.")

        # Rename columns for discharge and flags
        response_df.columns = ('gage ht', 'qualifiers')

        # Add column for site name
        response_df["sitename"] = hf.get_nwis_property(
            response.json, key='siteName')[0]

        # Add columns for gage location latitude and longitude
        geolocation = hf.get_nwis_property(response.json, key='geoLocation')[0]
        response_df["latitude"] = geolocation["geogLocation"]["latitude"]
        response_df["longitude"] = geolocation["geogLocation"]["longitude"]

        return response_df

