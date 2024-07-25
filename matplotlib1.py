#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:02:00 2024

visualization using Matplotlib

@author: ondul
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

temp = [0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]

plt.plot(year,temp)
plt.xlabel("year")
plt.ylabel("temperature")
plt.title("sample for learning only", {'fontsize':12, 'horizontalalignment':'left'})
plt.show() #for rendering the graph