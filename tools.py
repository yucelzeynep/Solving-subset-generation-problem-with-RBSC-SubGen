#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:21:58 2021

@author: zeynep
"""
import numpy as np
import random

from importlib import reload

import preferences
reload(preferences)
                 
def get_rbsc(score1, score2):
    """
    score1 is assumed to be the one with higher scores
    score2 is assumed to be the one with lower scores
    
    Also check below for y1 and y2
    """
    favor, unfavor = 0,0
    for d1 in score1:
        for d2 in score2:
            if (d1) > (d2):
                favor += 1
            else:
                unfavor += 1
            rbsc = (favor - unfavor) / (favor + unfavor)
    return rbsc


def init():
    """
    Initialize defaults for hyper-parameter and output arrays.
    """

    UNIVERSALSETSIZE_DEFAULT = int(np.median(preferences.UNIVERSALSETSIZE))
    SUBSETSIZE_DEFAULT = int(np.median(preferences.SUBSETSIZE))
    RHO_STAR_DEFAULT = np.median(preferences.RHO_STAR)
    EPS_DEFAULT = np.median(preferences.EPS)

    counters, rho_accuracy = {}, {}
    for l in preferences.UNIVERSALSETSIZE:
        counters[l], rho_accuracy[l] = {}, {}
        for s in preferences.SUBSETSIZE:
            counters[l][s], rho_accuracy[l][s] = {}, {}
            for rs in preferences.RHO_STAR:
                counters[l][s][rs], rho_accuracy[l][s][rs] = {}, {}
                for e in preferences.EPS:
                    counters[l][s][rs][e], rho_accuracy[l][s][rs][e] = [], []
    
    return \
        UNIVERSALSETSIZE_DEFAULT,\
        SUBSETSIZE_DEFAULT,\
        RHO_STAR_DEFAULT,\
        EPS_DEFAULT,\
        counters, \
        rho_accuracy
    

def my_snippet(l, s, rs, e):
    
    """
    Generate a universal with ranking relations associated.
    """
    if preferences.UNIVERSAL_DIST == "normal":
        x = np.random.normal(loc = 0, scale = 1, size = l)
    elif preferences.UNIVERSAL_DIST == "exponential":        
        x = np.random.exponential(scale = 1, size = l)
    elif preferences.UNIVERSAL_DIST == "uniform":        
        x = np.random.uniform(low = 1, high = 5, size = l)
    elif preferences.UNIVERSAL_DIST == "vonmises":        
        x = np.random.vonmises(mu = 0, kappa = np.pi/10, size = l)
    elif preferences.UNIVERSAL_DIST == "lognormal":        
        x = np.random.lognormal(mean = 0.0, sigma = 1.0, size = l)
    else:
        print('Unknown distribution for universal sel!')
        sys.exit(0)

    y = random.sample(list(x), s)
    y1 = y[:int(len(y)*0.5)] # y1 is assumed to be the one with higher scores                          
    y2 = y[int(len(y)*0.5):] # y2 is assumed to be the one with lower scores      
    rho = get_rbsc(y1, y2)

    counter = 0

    z = list(set(x) - set(y))
    
    while (not (rs - e <= rho and rho <= rs + e)) and (counter < preferences.MAXITER):
    
        """
        When rho is too small
        """
        if rho < rs - e:
            #--------------------------------------------------
            temp_counter1 = 0
            while temp_counter1 < preferences.MAXITER:
                temp_counter1 += 1
                w = np.random.choice(z,1)[0]
                if(np.mean(y1) < w):
                    y1.append(w)
                    z.remove(w)
                    break
            """
            If you cannot find anyting to add/remove to/from y1/y2,
                        the condition, pick up an element randomly 
            and go on.
            """
            if temp_counter1 == preferences.MAXITER:
                w = np.random.choice(z,1)[0]
                y1.append(w)
                z.remove(w)
            #--------------------------------------------------
                
            temp_counter2 = 0
            while temp_counter2 < preferences.MAXITER:
                temp_counter2 += 1
                w = np.random.choice(y1,1)[0]                                
                if(np.mean(y1) > w):
                    y1.remove(w)
                    z.append(w)
                    break
            """
            If cannot find anyting to add/remove to/from y1/y2,
                        the condition, pick up an element randomly 
            and go on.
            """
            if temp_counter2 == preferences.MAXITER:
                w = np.random.choice(y1,1)[0]             
                y1.remove(w)
                z.append(w)
            #--------------------------------------------------
            
            temp_counter3 = 0
            while temp_counter3 < preferences.MAXITER:
                temp_counter3 += 1 
                w = np.random.choice(z,1)[0]
                if(np.mean(y2) > w):
                    y2.append(w)
                    z.remove(w)
                    break
            """
            If cannot find anyting to add/remove to/from y1/y2
                        the condition, pick up an element randomly 
            and go on.
            """
            if temp_counter3 == preferences.MAXITER:
                w = np.random.choice(z,1)[0]     
                y2.append(w)
                z.remove(w)
            #--------------------------------------------------
                
            temp_counter4 = 0
            while temp_counter4 < preferences.MAXITER:
                temp_counter4 += 1
                w = np.random.choice(y2,1)[0]
                if(np.mean(y2) < w):
                    y2.remove(w)
                    z.append(w)
                    break
            """
            If cannot find anyting to add/remove to/from y1/y2,
                        the condition, pick up an element randomly 
            and go on.
            """
            if temp_counter4 == preferences.MAXITER:
                w = np.random.choice(y2,1)[0] 
                y2.remove(w)
                z.append(w)
            #--------------------------------------------------
        """
        When rho is too large
        """
        if rho > rs + e:
            temp_counter5 = 0
            while temp_counter5 < preferences.MAXITER:
                temp_counter5 += 1
                w = np.random.choice(z,1)[0]
                if(np.mean(y2) < w):
                    y2.append(w)
                    z.remove(w)
                    break
            """
            If cannot find anyting to add/remove to/from y1/y2,
                        the condition, pick up an element randomly
            and go on.
            """
            if temp_counter5 == preferences.MAXITER:
                w = np.random.choice(z,1)[0]
                y2.append(w)
                z.remove(w)
            #--------------------------------------------------
            
            temp_counter6 = 0
            while temp_counter6 < preferences.MAXITER:
                temp_counter6 += 1
                w = np.random.choice(y2,1)[0]
                if(np.mean(y2) > w):
                    y2.remove(w)
                    z.append(w)
                    break
            """
            If cannot find anyting to add/remove to/from y1/y2,
            the condition, pick up an element randomly and go on.
            """
            if temp_counter6 == preferences.MAXITER:
                w = np.random.choice(y2,1)[0]
                y2.remove(w)
                z.append(w)
            #--------------------------------------------------
                
            temp_counter7 = 0                                
            while temp_counter7 < preferences.MAXITER:
                temp_counter7 += 1
                w = np.random.choice(z,1)[0]
                if(np.mean(y1) > w):
                    y1.append(w)
                    z.remove(w)
                    break
            """
            If cannot find anyting to add/remove to/from y1/y2,
            the condition, pick up an element randomly and go on.
            """
            if temp_counter7 == preferences.MAXITER:
                w = np.random.choice(z,1)[0]
                y1.append(w)
                z.remove(w)
            #--------------------------------------------------
                
            temp_counter8 = 0
            while temp_counter8 < preferences.MAXITER:
                temp_counter8 += 1
                w = np.random.choice(y1,1)[0]
                if(np.mean(y1) < w):
                    y1.remove(w)
                    z.append(w)
                    break
            """
            If cannot find anyting to add/remove to/from y1/y2,
            the condition, pick up an element randomly and go on.
            """
            if temp_counter8 == preferences.MAXITER:
                w = np.random.choice(y1,1)[0]
                y1.remove(w)
                z.append(w)
             
            #--------------------------------------------------



        if len(y1) != int(0.5*s):
            print("len(y1) = {}. It should be {}".format(len(y1),int(0.5*s) ))
            sys.exit(0)
            
        if len(y2) != int(0.5*s):
            print("len(y2) = {}. It should be {}".format(len(y2),int(0.5*s) ))
            sys.exit(0)
        
        rho = get_rbsc(y1, y2)
        counter += 1
                            
    return counter, np.abs(rho - rs)

