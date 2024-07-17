#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:02:34 2024

@author: ondul
"""

import numpy as np

Data_n = np.array([1,3,4,5,7,9])

Mean = np.mean(Data_n)

Median = np.median(Data_n)

variance = np.var(Data_n)

standard_dev = np.std(Data_n)

Nump_array = np.array([[1,2,3],[4,5,7]])

var_Nump_array = np.var(Nump_array, axis=1)
var_Nump_array1 = np.var(Nump_array, axis=0)