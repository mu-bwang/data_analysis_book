#!/usr/bin/env python
# coding: utf-8

# # Rating curve for stream discharge and hydrographs
# 
# 
# 
# ## Introduction
# 
# Hydrographs of a river or a stream is important hydrological information that describe the time series of discharge at a specific location. However, it is challenging to obtain field measurements of stream discharges over time. To obtain indirect measurements, USGS monitors the stream stages which can be used to calculate discharges through a rating curve method that is developed for that specific stream. In this lab module, we will examine the field data at a stream to develop the rating curve.
# 
# 
# ## Hinkson Creek at Columbia, MO  
# Here is the USGS site that publish water data: https://waterdata.usgs.gov/nwis/rt. Let's click the map and select Hinkson Creek close to the University of Missouri campus. Here is the website for the Hinkson Creek site: https://waterdata.usgs.gov/nwis/uv?06910230. You can navigate to 'Summary of all available data for this site' and then 'Field measurements' to access all field collected data at this site.
# 
# Let's download the data. Click 'Reselect output format' in the output format table and specify the data period and other formating parameters. Here is the direct link: https://waterdata.usgs.gov/nwis/measurements?site_no=06910230&agency_cd=USGS&format=brief_list
# 
# ```{admonition} In-class exercise
# Let's select the data from 2000-01-01 until now and choose 'save to file'. Please perform some data cleaning and keep two columns: stage (ft) and discharge (cfs).
# ```
# 
# 
# ```{admonition} In-class exercise
# Please download the data, and plot the relationship between stream stage and discharge using scatter plot.
# ```
# 
# A general relationship between discharge and stage can be described by a power-law equation:
# 
# ```{math}
# :label: rating1
# Q = a D^b
# ```
# where $Q$ is discharge, $D$ is stage, $a$ and $b$ are coefficients that can be obtained from curve fitting.
# 
# ```{admonition} In-class exercise
# Please fit the rating curve equation (Eq.{eq}`rating1`) and determine coefficients $a$ and $b$. Plot the fitted curve on top of the data in the same figure.
# ```
