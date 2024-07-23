#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:17:51 2024

@author: ondul
"""

import pandas as pd

Age = pd.Series([10,20,30,40],index=['age1','age2', 'age3', 'age4'])

#selecting specific age
Age.age2

#filtering

filtered_age = Age[Age>=20]

#calling values of the series
Age.values

#calling indies of the series
Age.index

Age.index = ['a1', 'a2', 'a3', 'a4']