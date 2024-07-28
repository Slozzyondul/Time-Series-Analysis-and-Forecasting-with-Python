#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:59:52 2024

@author: ondul
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]

customer2 = [14,16,11,7,6,6,7,6,5,8,9,12]

#generating a scatter graph
plt.scatter(month,customer1,color = 'red', label='customer1')
plt.scatter(month,customer2,color = 'yellow', label='customer2')
plt.xlabel('month')
plt.ylabel('consumption')
plt.title('scatter plot sample graph')
plt.grid()
plt.legend(loc = 'best')
plt.show()