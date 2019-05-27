#!/usr/bin/python

# created by: Wennie Wang (wwwennie@gmail.com)
# created on: 4 July 2016

import numpy as np
import matplotlib.pyplot as plt
from lmfit.models import GaussianModel,LorentzianModel,VoigtModel, ExponentialModel
import time

def fitpeaks(filename,initpar,typefit=1,shift=25):
  """
    This file is for fitting peaks in Raman spectra
    Uses Python's LMFIT to find peaks
    Timing for more complicated fits

    filename: (string) file pointing to data, e.g., Raman spectra
             two-column format (x, y), e.g., (wavenum, intensity)
    initpar: (dictionary) containing initial guesses; keys: "center", "sigma", "amplitude"
    typefit: (integer) type of fit
             1 = Gaussian (default), 2 = Loretzian , 3 = Voigt
    shift; (integer) data points to account for background shift in spectra; default 25
  """

  nfits = len(initpar['center'].values())
  start_time = time.time()
  
  # Import data from filename
  data = np.loadtxt(filename)
  wavenum = data[:,0]         #x
  counts = data[:,1]-shift    #y
  print("Imported data: %.2f s" % (time.time()-start_time))
  
  # need instantiate size of list first?
  mods = []
  prefixes = []
  if (typefit == 1):
     for i in range(nfits):
        prefixes.append( 'g'+str(i+1)+'_' )
        mods.append(GaussianModel(prefix=prefixes[i]))
  elif (typefit == 2):
     for i in range(nfits):
        prefixes.append('L'+str(i+1)+'_')
        mods.append(LorentzianModel(prefix=prefixes[i]))
  elif (typefit == 3):
     for i in range(nfits):
        prefixes.append('v'+str(i+1)+'_')
        mods.append(VoigtModel(prefix=prefixes[i]))
  
  # setting initial guesses in fits
  modpars = ['center','sigma','amplitude'] # adjustable parameters in peak-fit models
  pars = mods[0].make_params() # initiate starting parameters
  keys = []
  for peak in range(len(mods)):
     pars.update( mods[peak].make_params() )
     for i in range(len(modpars)):
        param = modpars[i]
        key = prefixes[peak]+param
        keys.append(key)      
  
        val = initpar[param][peak+1]['val']
        minim = initpar[param][peak+1]['min']
        maxim = initpar[param][peak+1]['max']
        
        pars[key].set(val,min=minim,max=maxim) # lmfit peeps used built-in function names...
  
  print("Set initial parameters: %.2f s" % (time.time()-start_time))
  
  ## Debugging, using testdata
  #mods.append(ExponentialModel(prefix='exp_'))
  #pars.update(mods[nfits].guess(counts,x=wavenum))  # vars switched in file
  #prefixes.append('exp_')  # note: not updated in plotting
  
  #=============  Evaluating model ===========#
  model = np.sum(mods)
  #initial model
  initguess = model.eval(pars,x=wavenum)
  #initial model, decomposed into constituents; dictionary indexed by prefixes
  initcomp = model.eval_components(params=pars,x=wavenum)
  
  # fit data
  out = model.fit(counts,pars,x=wavenum)
  fitpars = out.best_values # dictionary, indexed with keys
  print("Fit model: %.2f s" % (time.time()-start_time))
  
  #update parameters with best fit
  # is there a better way to update Parameters() with dictionary?
  bestpars=pars
  for i in range(len(keys)):
     val = fitpars[keys[i]]
     bestpars[keys[i]].set(val)
  
  bestcomp = model.eval_components(params=bestpars,x=wavenum)
  print("Updated parameters: %.2f s" % (time.time()-start_time))
  
  #========= Save and print report ==========#
  repout = out.fit_report(min_correl=0.5)
  print(repout)
  outfile=filename.split(".")[0]+".out"
  f = open(outfile,'w')
  f.write(repout)
  
  #==========  Plotting results =============#
  #total results
  plt.figure()
  plt.plot(wavenum,counts, label='Measured',linewidth=2.0)
  plt.plot(wavenum,initguess,'k--',label='Initial')
  plt.plot(wavenum,out.best_fit,'r--',label='Fit',linewidth=2.0)
  plt.legend(loc='upper right')
  plt.title("Total fits")
  
  #decomposed results
  fig,(axinit, axbest) = plt.subplots(2,1,sharex=True)
  axbest.plot(wavenum,counts,label='Measured',linewidth=2.0)
  for i in range(len(prefixes)):
      axbest.plot(wavenum,bestcomp[prefixes[i]],'--',linewidth=1.5)
  axbest.set_title("Decomposed Best Fits")
  
  axinit.plot(wavenum,counts,label='Measured')
  for i in range(len(prefixes)):
      axinit.plot(wavenum,initcomp[prefixes[i]],'--',linewidth=1.5)
  axinit.set_title("Decomposed Initial Fits")
  
  plt.draw()
  plt.pause(0.001)
  input("Please press [enter] to continue")
