#!/usr/bin/python

# This module is for analyzing Raman spectra
# It has the following capabilities
#    - Gaussian peak fitting
#    - First derivatives via finite difference
#    - Differential Raman spectroscopy
# This file is the main driver for running things

# Dependecies:
#   numpy, lmfit, matplotlib

# created by: Wennie Wang (wwwennie@gmail.com)

if __name__=="__main__":

   # import user input
   from dat_wo3 import *
   #from dat_sto import *
 
   # import other functions
   from fitpeaks import *
   from interpdiff import * 
   from smooth import *
   from finite_diff import *
    
   #------ Main functionalities -------#
   ## fit spectra with decomposed peaks  and plot
   fitpeaks(filefit,initpar,typefit=2,shift=25)
   
   # take difference of two spectra
   interpdiff(file1,file2)

   # smooth peaks for easier peak finding and first-order derivatives
   smooth(filesmooth)

   # take first-derivative using finite difference
   finite_diff(filediff)
   


