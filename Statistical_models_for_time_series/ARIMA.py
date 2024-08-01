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

df = pd.read_csv('Temp-Data.csv', index_col = 'DATE', parse_dates=True)

df.index.freq = 'D'
df.dropna(inplace=True)