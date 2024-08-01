#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:16:09 2024

finding the value of p, d and q

@author: ondul
"""
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd

df = pd.read_csv('Temp-Data.csv', index_col = 'DATE', parse_dates=True)

train = df.iloc[:510,0]
test = df.iloc[510:,0]

#going 40 steps beackward
plot_acf(train, lags=40)
plot_pacf(train, lags=40)