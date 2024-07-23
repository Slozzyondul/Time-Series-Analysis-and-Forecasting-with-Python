#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:17:51 2024

@author: ondul
"""

import pandas as pd
import numpy as np

Age = pd.Series([10,20,30,40],index=['age1','age2', 'age3', 'age4'])

#selecting specific age
Age.age2

#filtering

filtered_age = Age[Age>=20]

#calling values of the series
Age.values

#calling indies of the series
Age.index

#changing indexing´ format
Age.index = ['a1', 'a2', 'a3', 'a4']


"""
Dataframe

"""
DF = np.array([[20,10,8],[25,8,10],[27,5,3],[30,9,7]])

data_set = pd.DataFrame(DF)

data_set1 = pd.DataFrame(DF, index= ['std1','std2','std3','std4'])

data_set2 = pd.DataFrame(DF, index= ['std1','std2','std3','std4'], columns= ['age', 'grade1', 'grade2'])

data_set2['grade3'] = [9,6,7,10]



