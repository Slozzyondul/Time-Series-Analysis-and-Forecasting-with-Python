#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:10:24 2024

ARIMA

@author: ondul
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('Temp-Data.csv', index_col = 'DATE', parse_dates=True)

df.index.freq = 'D'
df.dropna(inplace=True)

#filtering out uneeded columns 
df = pd.DataFrame(df["Temp"])

df.plot()

#training set

train = df.iloc[:510,0]
test = df.iloc[510:,0]


decomp_result = seasonal_decompose(df)
decomp_result.plot()

decomp_result.seasonal.plot()