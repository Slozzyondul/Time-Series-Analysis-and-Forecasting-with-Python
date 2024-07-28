#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:34:17 2024

@author: ondul
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]

customer2 = [14,16,11,7,6,6,7,6,5,8,9,12]

customer3 = np.random.rand(12)
customer4 = np.random.rand(12)

#generating a bar graph
plt.bar(month,customer1,color = 'red', label='customer1')
plt.bar(month,customer2,color = 'yellow', label='customer2')
plt.xlabel('month')
plt.ylabel('consumption') 
plt.title('bar plot sample graph')
plt.legend(loc = 'best')
plt.show()


######
bar_width = 0.4
#generating an array of random 11 numbers
month_values = np.arange(12)

plt.bar(month_values, customer1, bar_width, color='blue', label='customer1')

plt.bar(month_values+bar_width, customer2, bar_width, color='black', label='customer2')

plt.bar(month_values+bar_width+bar_width, customer3, bar_width, color='red', label='customer3')

plt.bar(month_values+bar_width+bar_width+bar_width, customer4, bar_width, color='green', label='customer4')

plt.xlabel('month')
plt.ylabel('consumption') 
plt.title('bar plot sample graph')
plt.xticks(month_values + (bar_width)/12, ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
plt.legend(loc = 'best')
plt.show()

