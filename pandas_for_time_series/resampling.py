#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:57:09 2024

resampling

@author: ondul
"""
import pandas as pd


df1 = pd.read_csv('/home/ondul/Desktop/time_series_python/Time-Series-Analysis-and-Forecasting-with-Python/Data-Set.csv', index_col='DATE', parse_dates=True)


"""
'D': Calendar day frequency
'W': Weekly frequency
'M': Month end frequency
'Q': Quarter end frequency
'A': Year end frequency
'H': Hourly frequency
'T' or 'min': Minute frequency
'S': Second frequency

"""
df1_resample = df1.resample(rule = 'D').mean()
