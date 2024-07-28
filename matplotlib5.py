#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:17:02 2024

@author: ondul
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]

customer2 = [14,16,11,7,6,6,7,6,5,8,9,12]

#boxplot
plt.boxplot(customer1, notch=False, vert=True)
#vert false = horizontal axis
#notch false = normal squrebox

plt.boxplot([customer1,customer2], patch_artist=True,
            boxprops=dict(facecolor='red', color='green'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='yellow'),
            medianprops=dict(color='orange'),
            )
plt.show()