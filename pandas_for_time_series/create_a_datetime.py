#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:52:45 2024

Pandas DateTime

@author: ondul
"""
#generating sample datasets to work with
import pandas as pd

date1 = pd.date_range('jan 01 2024', periods=12, freq='ME')

#quartely

date2 = pd.date_range('jan 01 2024', periods=4, freq='3ME')

#hourly

date3 = pd.date_range('jan 01 2024', periods=8760, freq='h')

