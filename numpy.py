#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:21:09 2024

@author: ondul
"""
import numpy as np
Nump_Array = np.array([[1,2,3],[4,5,6]])

NP1 = np.array([[1,3],[4,5]])

NP2 = np.array([[3,4],[5,7]])

MNP = NP1@NP2 

MNP3 = np.dot(NP1,NP2)

MNP2 = NP1*NP2

MNP4 = np.multiply(NP1,NP2)

