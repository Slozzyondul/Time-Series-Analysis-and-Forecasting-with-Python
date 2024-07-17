#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:20:39 2024

@author: ondul
"""
import numpy as np

NormalD = np.random.standard_normal(4)

UniformD = np.random.uniform(1,12,(3,4))

#generate floats numbers
random_floats = np.random.rand(3,4)

#generate random integers
random_array = np.random.randint(1,50,(2,5))

Zero = np.zeros((3,4))
ones = np.ones((3,4))

filter_array = np.logical_and(random_array>30, random_array<40)

F_random_array = random_array[filter_array]