#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:13:55 2018

@author: gravwaves
"""


# Import
#import GW_Template
import GW_CCSNeFromCatalog


# Choose a template
TemplateName      = 'And1'                        # ('And1','Dim1','Ott1','Yak1')

# Read and plot raw template
t,hp,hx,h = GW_CCSNeFromCatalog.Read(TemplateName,1)


# Define a sampling frequency
fs                = 4096                          # Sampling frequency

# Resampling template and convert oy PyCBC time series
# template          = GW_Template.Read(TemplateName,fs,1)


