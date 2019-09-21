#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:32:53 2019

@author: wumeiqi
"""

import pandas as pd
data0 = pd.read_csv('stormdata_2013.csv')
#%%
data1 = pd.read_csv('StormEvents_details-ftp_v1.0_d2019_c20190817.csv')
#%%
data = data1.loc[:, ['BEGIN_YEARMONTH', 'BEGIN_DAY','STATE','BEGIN_LAT',
                     'BEGIN_LON', 'EVENT_TYPE']]
data['BEGIN_YEARMONTHDAY']=