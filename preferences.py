#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:21:32 2021

@author: zeynep
"""
import numpy as np

# Domain for hyper-parameters values
UNIVERSALSETSIZE = np.arange(100, 901, 50)
SUBSETSIZE = np.arange(100, 501, 20)
RHO_STAR = np.arange(0.3, 0.71, 0.04)
EPS = np.arange(0.05, 0.16, 0.01)

# Threshold of number of iterations to decide saturation
MAXITER = 50
# Repeat subset generation with same set of hyper-parameters MAX_EXPERIMENTS times 
MAX_EXPERIMENTS = 30

# Choose the distribution of the universal set
# Use one of the below
# normal, exponential, uniform, vonmises, lognormal  
UNIVERSAL_DIST = "normal"
