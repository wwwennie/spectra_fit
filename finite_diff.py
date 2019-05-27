#!/usr/bin/python

# created by: Wennie Wang (wwwennie@gmail.com)
# created on: 31 July 2016

import numpy as np
import matplotlib.pyplot as plt

def finite_diff(filename,outfile="out-finitediff.dat"):
   """
   This file is for finding the first-order 
   derivative of a set of data (i.e, Raman peaks)
   using central difference

   filename, outfile: (string) input and output text files
   """
   # Import data from filename
   data = np.loadtxt(filename)
   wavenum = data[:,0]   #x
   counts = data[:,1]    #y
   
   #   TO DO
   # interpolate data for evenly spaced data points
   # minimize error of central difference
   
   fdcts = np.zeros(len(wavenum)) # first-order
   fd2cts = np.zeros(len(wavenum)) # second-order
   for i in range(len(wavenum)):
      # skip first and final points of data
      if (i == 0) or (i == len(wavenum)-1):
          continue
      else:
          width = wavenum[i+1]-wavenum[i-1]
          fdcts[i] = (counts[i+1] - counts[i-1])/(2*width)
          fd2cts[i] = (counts[i+1]-2*counts[i]-counts[i-1])/(width**2)
   
   #========== Save results =============#
   f = open(outfile,'w')
   outfd = zip(wavenum, fdcts)
   for line in outfd:
       f.write("   ".join(str(x) for x in line) + "\n")
   
   #==========  Plotting results =============#
   fig,ax1 = plt.subplots()
   ax2 = ax1.twinx()
   
   ax1.plot(wavenum,counts, label='Measured',linewidth=2.0)
   ax2.plot(wavenum,fdcts,'k--',label='First-order derivative',linewidth=2.0)
   ax2.plot(wavenum,fd2cts,'g:',label='Second-order deriviative',linewidth=3.0)
   
   ax1.set_xlabel('Wave number (cm^-1)')
   ax1.set_ylabel('Intensity counts')
   ax2.set_ylabel('Slope Intensity')
   plt.legend(loc='upper right')
   
   plt.draw()
   plt.pause(0.001)
   input("Please press [enter] to continue")
