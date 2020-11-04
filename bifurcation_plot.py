#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:08:02 2020

@author: javi_lassaortiz
"""
import numpy as np     	
import matplotlib.pyplot as plt


# Hopf
beta_h = np.arange(-0.5, 0, 0.001)
alpha_h = np.zeros(len(beta_h))

# SN
beta_range = np.arange(-0.4, 0.05, 0.001)
alpha_sn = []
beta_sn = []

for b in beta_range:
    if 1+3*b > 0:
        
        x1 = 1/3 + 1/3 * np.sqrt(1+3*b)
        a1 = -b*x1 - x1*x1 + x1*x1*x1
        
        x2 = 1/3 - 1/3 * np.sqrt(1+3*b)
        a2 = -b*x2 - x2*x2 + x2*x2*x2
        
        alpha_sn = alpha_sn + [a1, a2]
        beta_sn = beta_sn + [b, b]


# Rango betas para buscar los mapas b-w

beta_mapa = np.arange(-0.3, 0, 0.01 )
alpha_mapa = np.ones(len(beta_mapa))
alpha_mapa = alpha_mapa * (-0.15)


# Ploteo
plt.figure()        
plt.plot(alpha_sn, beta_sn, '.b', label ='SN')
plt.plot(alpha_h, beta_h, 'r-', label = 'Hopf')
plt.plot(alpha_mapa, beta_mapa, 'g-', label = 'rango beta de mapa b-w')

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta$')
plt.legend()

plt.show