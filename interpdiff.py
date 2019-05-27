#!/usr/bin/python

# created by: Wennie Wang (wwwennie@gmail.com)
# created on: 7 July 2016


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def interpdiff(file1,file2, outfile="out-interpdiff.dat"):
  """ 
   Takes difference of two Raman Spectra
   Requires interpolation since wavenum do not exactly match
   between measured spectra

   interpolated values are based on x-values of file1
  
   file1,file2: (string) name of files with data
           two-column (x,y) format
  """

  # Import data
  data1 = np.loadtxt(file1)
  data2 = np.loadtxt(file2)
  
  x1 = data1[:,0]
  y1 = data1[:,1]
  
  x2 = data2[:,0]
  y2 = data2[:,1]
  
  #== Interpolate ==#
  f2lin = interp1d(x2,y2)
  f2cub = interp1d(x2,y2,kind='cubic')
   
  cubdiff = abs(f2cub(x1)-y1)
  lindiff = abs(f2lin(x1)-y1)
  
  #== Save interpolation =="
  c = open('cub'+outfile,'w')
  outc = zip(x1,cubdiff)
  for line in outc:
      c.write("   ".join(str(x) for x in line) + "\n")
  
  l = open('lin'+outfile,'w')
  outl = zip(x1,lindiff)
  for line in outl:
      l.write("   ".join(str(x) for x in line) + "\n")
  
  #==========  Plotting results =============#
  #interpolation results
  plt.figure()
  plt.plot(x2,y2, label=file2,linewidth=2.0)
  plt.plot(x1,f2lin(x1),'k--',label='Linear Interp.')
  plt.plot(x1,f2cub(x1),'g-',label='Cubic Interp.')
  plt.legend(loc='best')
  plt.legend(loc='best')
  plt.xlabel("Wavenumber (cm^{-1})")
  plt.ylabel("Intensity (counts/s)")
  plt.title("Interpolation")
  
  #difference of spectra results
  plt.figure(2)
  plt.plot(x1,y1,'k-.',label=file1,linewidth=0.8)
  plt.plot(x2,y2,'k--',label=file2,linewidth=0.8)
  plt.plot(x1,cubdiff,'g-',label='Difference, Cubic Interp.',linewidth=2.0)
  plt.legend(loc='best')
  plt.xlabel("Wavenumber (cm^{-1})")
  plt.ylabel("Intensity (counts/s)")
  plt.title("Difference")
  
  plt.draw()
  plt.pause(0.001)
  input("Please press [enter] to continue")
