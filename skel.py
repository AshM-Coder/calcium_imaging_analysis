#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:17:15 2022

@author: sschultz
"""

import numpy as np
import matplotlib.pyplot as plt

#%% 
dFonF1 = np.load("data/DFF_file3_ch1.npy")      # fluorescence time series ch1
nframes = np.size(dFonF1,1)
dFonF2 = np.load("data/DFF_file3_ch2.npy")      # channel 2
dFonF = np.concatenate((dFonF1,dFonF2[:,0:nframes])) # this now combines both channels
ncells = np.size(dFonF,0)
XY1 = np.load("data/coord_file3_ch1.npy")       # get coordinates of cells in space
XY2 = np.load("data/coord_file3_ch2.npy")
xc1 = XY1[0,:]       
yc1 = XY1[1,:]
xc2 = XY2[0,:]
yc2 = XY2[1,:]
xc = np.hstack((xc1,xc2+1500))                  # xc,yc are your coords
yc = np.hstack((yc1,yc2))
fr = 7.6                                        # frame rate in Hz
t = np.linspace(0,(nframes-1)*1.0/fr,nframes)

#%% 
# visualise cell locations

fig,ax = plt.subplots()

ax.scatter(xc,yc,2)
plt.show()

# this is just to get you started... now make a much nicer plot!
# ... and use an aspect ratio such that 1 mm on the x axis is 1 mm on y=the y axis

#%% plot an example fluorescence trace

fig,ax = plt.subplots()

ax.plot(t,dFonF[0,:])
plt.show()

#%% show image of traces
fig,ax = plt.subplots()
plt.imshow(dFonF,clim=[0,0.5],cmap=plt.cm.viridis)
plt.show()

# note that the colour limit of 0.5 has been chosen arbitrarily above. You should
# investigate the traces and see what is the most appropriate limits to use.
# please make sure you label your axes etc - I have left it for you to do!