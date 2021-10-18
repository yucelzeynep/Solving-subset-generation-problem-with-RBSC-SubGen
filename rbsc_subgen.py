#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:43:56 2021

@author: zeynep
"""

import sys
import numpy as np
import random
import datetime
import pickle
import time
from importlib import reload

import tools as tools

import preferences
reload(preferences)
    
if __name__ == "__main__":
    
        start_time = time.time()

        UNIVERSALSETSIZE_DEFAULT,\
        SUBSETSIZE_DEFAULT,\
        RHO_STAR_DEFAULT,\
        EPS_DEFAULT,\
        counters, \
        rho_accuracy = \
        tools.init()
        
        """
        Defaults: LISTSIZE, SELECTLIST
        Non-defaults: RHO_STAR, EPS
        """

        for rs in preferences.RHO_STAR:
            for e in preferences.EPS:
            
                n_experiment = 0
                for n_experiment in range(preferences.MAX_EXPERIMENTS):

                    temp_counter, temp_rho_accuracy = tools.my_snippet(\
                                UNIVERSALSETSIZE_DEFAULT,\
                                SUBSETSIZE_DEFAULT,\
                                rs,\
                                e)

                        
                    counters[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e].append(temp_counter) 
                    rho_accuracy[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e].append(temp_rho_accuracy)
                        
                        
                if len(counters[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e]) != preferences.MAX_EXPERIMENTS:
                    print("Problem! len(counters[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e) is {}. It should be {}.".format(\
                        len(counters[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e]), preferences.MAX_EXPERIMENTS))
                    sys.exit(0)
                         
                print('-------------------------')    
                print('Defaults:\t listsize:{0:0.2f}\t selectlist: {1:0.2f}\t \t'.format(\
                      UNIVERSALSETSIZE_DEFAULT,SUBSETSIZE_DEFAULT,\
                      ))
    
     
                print('Non-defaults:\t RHO_STAR \t  EPS\t')
                print('Results:\t niter: {0:0.2f} pm {1:0.2f}\t  rho_accuracy: {2:0.2f} pm {3:0.2f}\t'.format(\
                np.mean(counters[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e]),\
                np.std(counters[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e]),\
                np.mean(rho_accuracy[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e]),\
                np.std(rho_accuracy[UNIVERSALSETSIZE_DEFAULT][SUBSETSIZE_DEFAULT][rs][e])))

        """
        Defaults: LISTSIZE, RHO_STAR
        Non-defaults: SELECTLIST, EPS
        """

        for s in SELECTLIST:
            if UNIVERSALSETSIZE_DEFAULT <= s:
                break
            for e in preferences.EPS:
           
                n_experiment = 0
                for n_experiment in range(preferences.MAX_EXPERIMENTS):

                    temp_counter, temp_rho_accuracy = tools.my_snippet(\
                                UNIVERSALSETSIZE_DEFAULT,\
                                s,\
                                RHO_STAR_DEFAULT,\
                                e)

                        
                    counters[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e].append(temp_counter) 
                    rho_accuracy[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e].append(temp_rho_accuracy)
                        
                if len(counters[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e]) != preferences.MAX_EXPERIMENTS:
                    print("Problem! len(counters[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e]) is {}. It should be {}.".format(\
                        len(counters[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e]), preferences.MAX_EXPERIMENTS))
                    sys.exit(0)
                        
                        
                print('-------------------------')    
                print('Defaults:\t listsize:{0:0.2f}\t rs: {1:0.2f}\t \t'.format(\
                      UNIVERSALSETSIZE_DEFAULT,RHO_STAR_DEFAULT,\
                      ))
    
     
                print('Non-defaults:\t SELECTLIST\t  EPS\t')
                print('Results:\t niter: {0:0.2f} pm {1:0.2f}\t  rho_accuracy: {2:0.2f} pm {3:0.2f}\t'.format(\
                np.mean(counters[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e]),\
                np.std(counters[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e]),\
                np.mean(rho_accuracy[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e]),\
                np.std(rho_accuracy[UNIVERSALSETSIZE_DEFAULT][s][RHO_STAR_DEFAULT][e])))

        """
        Defaults: LISTSIZE, EPS
        Non-defaults: SELECTLIST, RHO_STAR
        """

        for s in SELECTLIST:
            
            if UNIVERSALSETSIZE_DEFAULT <= s:
                break
            
            for rs in preferences.RHO_STAR:

                n_experiment = 0
                for n_experiment in range(preferences.MAX_EXPERIMENTS):

                    temp_counter, temp_rho_accuracy = tools.my_snippet(\
                                UNIVERSALSETSIZE_DEFAULT,\
                                s,\
                                rs,\
                                EPS_DEFAULT)

                        
                    counters[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT].append(temp_counter) 
                    rho_accuracy[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT].append(temp_rho_accuracy)
                        
                        
                if len(counters[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT]) != preferences.MAX_EXPERIMENTS:
                    print("Problem! len(counters[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT]) is {}. It should be {}.".format(\
                        len(counters[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT]), preferences.MAX_EXPERIMENTS))
                    sys.exit(0)
                        
                print('-------------------------')    
                print('Defaults:\t UNIVERSALSETSIZE_DEFAULT:{0:0.2f}\t EPS_DEFAULT: {1:0.2f}\t \t'.format(\
                      UNIVERSALSETSIZE_DEFAULT,EPS_DEFAULT,\
                      ))
    
     
                print('Non-defaults:\t SELECTLIST\t  RHO_STAR\t')
                print('Results:\t niter: {0:0.2f} pm {1:0.2f}\t  rho_accuracy: {2:0.2f} pm {3:0.2f}\t'.format(\
                np.mean(counters[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT]),\
                np.std(counters[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT]),\
                np.mean(rho_accuracy[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT]),\
                np.std(rho_accuracy[UNIVERSALSETSIZE_DEFAULT][s][rs][EPS_DEFAULT])))
                    
        """
        Defaults: SELECTLIST, RHO_STAR
        Non-defaults: LISTSIZE, EPS
        """

        for l in LISTSIZE:
            
            if l <= SUBSETSIZE_DEFAULT:
                break
            
            for e in preferences.EPS:
            
                n_experiment = 0
                for n_experiment in range(preferences.MAX_EXPERIMENTS):

                    temp_counter, temp_rho_accuracy = tools.my_snippet(\
                                l,\
                                SUBSETSIZE_DEFAULT,\
                                RHO_STAR_DEFAULT,\
                                e)

                    counters[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e].append(temp_counter) 
                    rho_accuracy[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e].append(temp_rho_accuracy)
                        
                if len(counters[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e]) != preferences.MAX_EXPERIMENTS:
                    print("Problem! len([l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e]) is {}. It should be {}.".format(\
                        len(counters[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e]), preferences.MAX_EXPERIMENTS))
                    sys.exit(0)
                    
                print('-------------------------')    
                print('Defaults:\t SUBSETSIZE_DEFAULT:{0:0.2f}\t RHO_STAR_DEFAULT: {1:0.2f}\t \t'.format(\
                      SUBSETSIZE_DEFAULT,RHO_STAR_DEFAULT,\
                      ))
    
                print('Non-defaults:\t LISTSIZE\t  EPS\t')
                print('Results:\t niter: {0:0.2f} pm {1:0.2f}\t  rho_accuracy: {2:0.2f} pm {3:0.2f}\t'.format(\
                np.mean(counters[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e]),\
                np.std(counters[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e]),\
                np.mean(rho_accuracy[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e]),\
                np.std(rho_accuracy[l][SUBSETSIZE_DEFAULT][RHO_STAR_DEFAULT][e])))

        """
        Defaults: SELECTLIST, EPS 
        Non-defaults: LISTSIZE, RHO_STAR
        """

        for l in LISTSIZE:
            
            if l <= SUBSETSIZE_DEFAULT:
                break
            
            for rs in preferences.RHO_STAR:
                
                n_experiment = 0
                for n_experiment in range(preferences.MAX_EXPERIMENTS):

                    temp_counter, temp_rho_accuracy = tools.my_snippet(\
                                l,\
                                SUBSETSIZE_DEFAULT,\
                                rs,\
                                EPS_DEFAULT)

                    counters[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT].append(temp_counter) 
                    rho_accuracy[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT].append(temp_rho_accuracy)
                        
                if len(counters[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT]) != preferences.MAX_EXPERIMENTS:
                    print("Problem! len(counters[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT]) is {}. It should be {}.".format(\
                        len(counters[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT]), preferences.MAX_EXPERIMENTS))
                    sys.exit(0)
                        
                print('-------------------------')    
                print('Defaults:\t SUBSETSIZE_DEFAULT:{0:0.2f}\t EPS_DEFAULT: {1:0.2f}\t \t'.format(\
                      SUBSETSIZE_DEFAULT,EPS_DEFAULT,\
                      ))
     
                print('Non-defaults:\t LISTSIZE\t  RHO_STAR\t')
                print('Results:\t niter: {0:0.2f} pm {1:0.2f}\t  rho_accuracy: {2:0.2f} pm {3:0.2f}\t'.format(\
                np.mean(counters[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT]),\
                np.std(counters[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT]),\
                np.mean(rho_accuracy[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT]),\
                np.std(rho_accuracy[l][SUBSETSIZE_DEFAULT][rs][EPS_DEFAULT]))) 

        """
        Defaults: RHO_STAR, EPS 
        Non-defaults: LISTSIZE, SELECTLIST
        """

        for l in LISTSIZE:
            for s in SELECTLIST:
                
                if not ( l <= s ) :
            
                    n_experiment = 0
                    for n_experiment in range(preferences.MAX_EXPERIMENTS):
    
                        temp_counter, temp_rho_accuracy = tools.my_snippet(\
                                    l,\
                                    s,\
                                    RHO_STAR_DEFAULT,\
                                    EPS_DEFAULT)
                            
                        counters[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT].append(temp_counter) 
                        rho_accuracy[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT].append(temp_rho_accuracy)
                            
                    if len(counters[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT]) != preferences.MAX_EXPERIMENTS:
                        print("Problem! len(counters[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT]) is {}. It should be {}.".format(\
                            len(counters[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT]), preferences.MAX_EXPERIMENTS))
                        sys.exit(0)
                        
                    print('-------------------------')    
                    print('Defaults:\t RHO_STAR_DEFAULT:{0:0.2f}\t EPS_DEFAULT: {1:0.2f}\t \t'.format(\
                          RHO_STAR_DEFAULT, EPS_DEFAULT\
                          ))
        
                    print('Non-defaults:\t LISTSIZE\t  SELECTLIST\t')
                    print('Results:\t niter: {0:0.2f} pm {1:0.2f}\t  rho_accuracy: {2:0.2f} pm {3:0.2f}\t'.format(\
                    np.mean(counters[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT]),\
                    np.std(counters[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT]),\
                    np.mean(rho_accuracy[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT]),\
                    np.std(rho_accuracy[l][s][RHO_STAR_DEFAULT][EPS_DEFAULT])))

        """
        Build output file name as
        YYY_MM_DD_hh_mm_ss_vars_and_outs_UNIVERSAL_DIST.pkl
        """

        now = datetime.datetime.now()
        fpath = str(now.year) + '_' + \
        str(now.month).zfill(2)  + '_' + \
        str(now.day).zfill(2) + '_' + \
        str(now.hour).zfill(2)  + '_' + \
        str(now.minute).zfill(2)  + '_' +\
        str(now.second).zfill(2)  + '_' +\
        'vars_and_outs_'+preferences.UNIVERSAL_DIST+'.pkl'
    
    
        with open(fpath, 'wb') as handle:
            pickle.dump([MAXITER,\
        preferences.MAX_EXPERIMENTS,\
        LISTSIZE, \
        SELECTLIST,\
        UNIVERSALSETSIZE_DEFAULT,\
        SUBSETSIZE_DEFAULT,\
        RHO_STAR_DEFAULT,\
        EPS_DEFAULT,\
        RHO_STAR,\
        EPS,\
        counters, \
        rho_accuracy], \
        handle, \
        protocol=pickle.HIGHEST_PROTOCOL)
             
        # Time elapsed 4412.87 sec
        elapsed_time = time.time() - start_time
        print('Time elapsed %2.2f sec' %elapsed_time)      
