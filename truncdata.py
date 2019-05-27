#!/usr/bin/python

# created by: Wennie Wang (wwwennie@gmail.com)
# created on: 20 July 2016

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#==============================#
#========= USER INPUTS ========#
#==============================#

def trunc_data(filename,min_index,max_index,outfile="out-truncdata.dat"):
   """ Truncate dat within specified range """
   # Import data
   data = np.loadtxt(infile)
   
   x = data[:,0]
   y = data[:,1]
   
   #== Save interpolation =="
   c = open(outfile+'trunc','w')
   outc = zip(x1,cubdiff)
   for line in outc:
       c.write("   ".join(str(x) for x in line) + "\n")
   
   #==========  Plotting truncated data  =============#
   #interpolation results
   plt.figure(1)
   plt.plot(x2,y2, label=file2,linewidth=2.0)
   plt.legend(loc='best')
   plt.xlabel("Wavenumber (cm^{-1})")
   plt.ylabel("Intensity (counts/s)")
   
   plt.draw()
   plt.pause(0.001)
   input("Please press [enter] to continue")
