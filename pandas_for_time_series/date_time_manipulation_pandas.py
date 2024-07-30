#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:17:58 2024

creating date time column

@author: ondul
"""
import numpy as np
import pandas as pd


date1 = pd.date_range('jan 01 2024', periods=12, freq='ME')
#quartely
date2 = pd.date_range('jan 01 2024', periods=4, freq='3ME')
#hourly
date3 = pd.date_range('jan 01 2024', periods=8760, freq='h')


#generating  a random dataset of weights between 1 - 1000 for a list of 8760 rows with 2 columns

data1 = np.random.randint(1,1000,(8760, 2))

#convert to dataframe
df = pd.DataFrame(data1)

df.set_index(date3, inplace=True)
              
df1 = pd.read_csv('/home/ondul/Desktop/time_series_python/Time-Series-Analysis-and-Forecasting-with-Python/Data-Set.csv', index_col='DATE', parse_dates=True)
df1.info()