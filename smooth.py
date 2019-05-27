#!/usr/bin/python

# created by: Wennie Wang (wwwennie@gmail.com)
# created on: 31 July 2016

import numpy as np
import matplotlib.pyplot as plt

def smooth_spectra(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def smooth(filename,outfile="out-smooth.dat"):

   """ 
    For smoothing out spectra in order to find first-order derivative 
    and peaks easier
   
    filename, outfile: (string) name of input and output files
   """

   window =5 # window for moving-average convolution
   # Import data from filename
   data = np.loadtxt(filename)
   wavenum = data[:,0]         #x
   counts = data[:,1]    #y
   
   smoothcts = smooth_spectra(counts,window)
   
   #========== Save results =============#
   f = open(outfile,'w')
   outsmooth = zip(wavenum, smoothcts)
   for line in outsmooth:
       f.write("   ".join(str(x) for x in line) + "\n")
   
   #==========  Plotting results =============#
   #total results
   plt.figure()
   plt.plot(wavenum,counts, label='Measured',linewidth=2.0)
   plt.plot(wavenum,smoothcts,'k--',label='Smoothed',linewidth=2.0)
   plt.legend(loc='upper right')
   
   plt.draw()
   plt.pause(0.001)
   input("Please press [enter] to continue")
