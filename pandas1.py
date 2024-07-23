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

#viewing data stored at a specific location
pos1 = data_set2.loc['std2']

#locating item using index 
pos2 = data_set2.iloc[1][3]

#choosing an entire column 
pos3 = data_set2.iloc[:,0]

#choosing several columns
pos4 = data_set2.iloc[:,1:3]

#deleting a column

data_set3 = data_set2.drop('grade1',axis=1)

#replacing values
data_set4 = data_set.replace(10,12)

#replaing values using dictionary
pos5 = data_set3.replace({12:10, 9:30})

#first 3 items
pos6 = data_set3.head(3)

#last 3
pos7 = data_set3.tail(3)

#sorting values
pos8 = data_set2.sort_values('grade1', ascending=False)

#sorting index
pos9 = data_set2.sort_index(axis=0, ascending=True)

#reading different file formats in pandas
data = pd.read_csv('Data-Set.csv')