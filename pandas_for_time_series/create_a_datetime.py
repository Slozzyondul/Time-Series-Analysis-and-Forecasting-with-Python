#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:52:45 2024

Pandas DateTime

@author: ondul
"""
#generating sample datasets to work with
import pandas as pd
import numpy as np

date1 = pd.date_range('jan 01 2024', periods=12, freq='ME')
#quartely
date2 = pd.date_range('jan 01 2024', periods=4, freq='3ME')
#hourly
date3 = pd.date_range('jan 01 2024', periods=8760, freq='h')


#set date as index
data_set = np.random.randint(1,1000, (8760,2))

dataframe_data_set = pd.DataFrame(data_set)

dataframe_data_set.set_index(date3, inplace=True)

df = pd.read_csv('/home/ondul/Desktop/time_series_python/Time-Series-Analysis-and-Forecasting-with-Python/Data-Set.csv')

df1 = pd.read_csv('/home/ondul/Desktop/time_series_python/Time-Series-Analysis-and-Forecasting-with-Python/Data-Set.csv', index_col='DATE', parse_dates=True)

df1.info()