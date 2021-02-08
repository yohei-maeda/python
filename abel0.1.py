# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:44:20 2021

@author: maeda youhei
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt



def abel_inv(dIdy, rframe, s) :     # dI/dy, 半径, ステップ
    return np.sum((-1.0/np.pi)*dIdy[s+1:]/np.sqrt(rframe[s+1:]**2 - rframe[s]**2))
    
def Abel(I, r, rframe) :
    
    tck = interpolate.splrep(r, I)      
    intensityspl = interpolate.splev(rframe, tck)
    
    dIdy = (intensityspl[1:] - intensityspl[:-1]) / (rframe[1:] - rframe[:-1])
    dIdy = np.append(dIdy, dIdy[-1])
    
    realintensity = np.zeros((len(rframe)))
    for i in np.arange(0, len(rframe) - 1) :
        realintensity[i] = abel_inv(dIdy, rframe, i)
    
    fig, ax = plt.subplots(1, 1)
    ax.scatter(r, I)
    ax.plot(rframe, intensityspl, label="Raw Intensity")
    ax.plot(rframe, realintensity, label="Abel Inversion")
    ax.set_ylim(0, ) # 最大値を指定しない
    ax.legend()
    plt.show()
    return intensityspl, dIdy, realintensity

intensity = [6., 8., 6., 3., 2., 1.]
rframe = np.linspace(0, 100, 13000)
r = [0, 20, 40, 60, 80, 99]         # 視線配置半径

intensityspl, dIdy, realintensity = Abel(intensity, r, rframe)