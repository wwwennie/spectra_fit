#!/usr/bin/python

#==============================#
#========= USER INPUTS ========#
#==============================#


# take difference of two spectra, and interpolate
file1 = "./example-data/wo3-side1.txt"
file2 = "./example-data/wo3-side2.txt"

# take first derivative of spectra
filediff=file1

# smooth spectra, with convolution
filesmooth="./example-data/smooth_me.txt"

# peak fiting
filefit = file1
nfits = 12			# number of peaks to fit
typefit = 2			# 1 = Gaussian, 2 = Lorentzian, 3 = Voigt type fits
shift = 25			# background shift

#================  Initial guesses =================#
# as nested dictionary
# adapt to different models by changing parameters
# use float("inf") for infinity or import math; math.inf
# default bounds:
#     center: [-inf:inf]
#     sigma:  [0:inf]
#     amplitude: [-inf:inf]

# the initial guesses for center are based on phonon modes calculated from DFPT 
initpar = {'center': {1:{'val':90,'min':0,'max':120},\
                      2:{'val':93,'min':0,'max':120},\
                      3:{'val':133,'min':100,'max':150},\
                      4:{'val':180,'min':150,'max':225},\
                      5:{'val':225,'min':200,'max':275},\
                      6:{'val':275,'min':250,'max':300},\
                      7:{'val':350,'min':300,'max':400},\
                      8:{'val':610,'min':570,'max':650},\
                      9:{'val':650,'min':600,'max':700},\
                     10:{'val':720,'min':675,'max':800},\
                     11:{'val':810,'min':775,'max':850},\
                     12:{'val':1100,'min':1000,'max':1500}},\
           'sigma':{1:{'val':15,'min':1,'max':35},\
                    2:{'val':15,'min':1,'max':35},\
                    3:{'val':15,'min':1,'max':55},\
                    4:{'val':15,'min':1,'max':35},\
                    5:{'val':15,'min':1,'max':35},\
                    6:{'val':15,'min':1,'max':45},\
                    7:{'val':15,'min':1,'max':45},\
                    8:{'val':15,'min':1,'max':35},\
                    9:{'val':15,'min':1,'max':35},\
                   10:{'val':15,'min':1,'max':35},\
                   11:{'val':15,'min':1,'max':25},\
                   12:{'val':15,'min':1,'max':100}},\
           'amplitude':{1:{'val':30000,'min':10,'max':float("inf")},\
                        2:{'val':30000,'min':100,'max':float("inf")},\
                        3:{'val':10000,'min':2000,'max':float("inf")},\
                        4:{'val':10000,'min':1000,'max':float("inf")},\
                        5:{'val':10000,'min':1000,'max':float("inf")},\
                        6:{'val':5000,'min':0,'max':float("inf")},\
                        7:{'val':5000,'min':0,'max':float("inf")},\
                        8:{'val':5000,'min':0,'max':float("inf")},\
                        9:{'val':5000,'min':0,'max':float("inf")},\
                       10:{'val':5000,'min':500,'max':float("inf")},\
                       11:{'val':2000,'min':500,'max':float("inf")},\
                       12:{'val':2000,'min':500,'max':float("inf")}}\
          }

