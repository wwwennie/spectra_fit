#!/usr/bin/python

#========= USER INPUTS ========#
#==============================#

filefit = "./example-data/sto-raman-spectra.txt"
typefit = 1			# 1 = Gaussian, 2 = Lorentzian, 3 = Voigt type fits
shift = 20			# background shift

#================  Initial guesses =================#
# as nested dictionary
# adapt to different models by changing parameters
# use float("inf") for infinity or import math; math.inf
# default bounds:
#     center: [-inf:inf]
#     sigma:  [0:inf]
#     amplitude: [-inf:inf]


initpar = {'center': {1:{'val':130,'min':0,'max':150},\
                      2:{'val':175,'min':150,'max':200},\
                      3:{'val':260,'min':250,'max':275},\
                      4:{'val':300,'min':275,'max':310},\
                      5:{'val':375,'min':325,'max':400},\
                      6:{'val':410,'min':400,'max':435},\
                      7:{'val':630,'min':600,'max':650},\
                      8:{'val':670,'min':650,'max':700},\
                      9:{'val':730,'min':725,'max':780},\
                      10:{'val':800,'min':775,'max':825},\
                      11:{'val':1050,'min':1025,'max':1075},\
                      12:{'val':1250,'min':1200,'max':1350},\
                      13:{'val':1390,'min':1300,'max':1400}},\
           'sigma':{1:{'val':15,'min':1,'max':35},\
                    2:{'val':15,'min':1,'max':35},\
                    3:{'val':15,'min':1,'max':35},\
                    4:{'val':15,'min':1,'max':35},\
                    5:{'val':15,'min':1,'max':35},\
                    6:{'val':15,'min':1,'max':45},\
                    7:{'val':15,'min':1,'max':25},\
                    8:{'val':15,'min':1,'max':25},\
                    9:{'val':15,'min':1,'max':25},\
                   10:{'val':35,'min':1,'max':75},\
                   11:{'val':35,'min':1,'max':100},\
                   12:{'val':15,'min':1,'max':35},\
                   13:{'val':15,'min':1,'max':35}},\
           'amplitude':{1:{'val':3000,'min':10,'max':float("inf")},\
                        2:{'val':3000,'min':100,'max':float("inf")},\
                        3:{'val':5000,'min':2000,'max':float("inf")},\
                        4:{'val':6000,'min':2000,'max':float("inf")},\
                        5:{'val':5000,'min':2000,'max':float("inf")},\
                        6:{'val':5000,'min':500,'max':float("inf")},\
                        7:{'val':3000,'min':1000,'max':float("inf")},\
                        8:{'val':3000,'min':1000,'max':float("inf")},\
                        9:{'val':3000,'min':1000,'max':float("inf")},\
                       10:{'val':2000,'min':10,'max':float("inf")},\
                       11:{'val':2000,'min':10,'max':float("inf")},\
                       12:{'val':1500,'min':10,'max':float("inf")},\
                       13:{'val':1500,'min':10,'max':float("inf")}}\
          }

