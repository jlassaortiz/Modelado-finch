#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:41:21 2020

@author: javi_lassaortiz

Basado en: https://pythontic.com/visualization/signals/fouriertransform_fft


Grafica FFT del segmento especificado de BOS y SYN.


"""

import numpy as np     	
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from scipy.signal import find_peaks as find_peaks



# ----------------
# Defino variables
# ----------------

# Defino variables
nombre_BOS = '/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/cantos-AB010-bi/Resumen31-7-20/zfAB010-bi_BOS03_44100.wav'
#nombre_SYN = '/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/cantos-AB010-bi/Resumen31-7-20/AB010-bi_SYN_ruido.wav'
nombre_SYN = '/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/cantos-AB010-bi/Resumen31-7-20/AB010-bi_Y_ori.wav'

# Tiempos de la sílaba o segmento a analizar
ti = 1.03 # en segundos
tf = 1.11 # en segundos




# ------------------------
# Calculo FFT de BOS y SYN
# ------------------------

# Cargo BOS y SYN como np.array y conservo ademas los sampling rate
rate_bos, BOS = read(nombre_BOS)
rate_syn, SYN = read(nombre_SYN)
print(rate_bos)

# Conservo solo la parte del canto de interes
BOS = BOS[int(ti*rate_bos):int(tf*rate_bos)]
SYN = SYN[int(ti*rate_syn):int(tf*rate_syn)]

# Calculo fft de BOS y SYN
BOS_fft = np.fft.fft(BOS) /len(BOS)
SYN_fft = np.fft.fft(SYN) /len(SYN)

# No se bien porque pero necesito sacar las frecuencias de la mitad superior
BOS_fft = BOS_fft[range(int(len(BOS)/2))]
SYN_fft = SYN_fft[range(int(len(SYN)/2))]

# Hago vector de frecuencias para poder graficar
tpCount     = len(BOS)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/rate_bos
frequencies_BOS = values/timePeriod

tpCount     = len(SYN)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/rate_syn
frequencies_SYN = values/timePeriod


# ----------
# Ploteo FFT
# ----------

# Escala Log
plt.figure()
plt.plot(frequencies_BOS, abs(BOS_fft), label = 'BOS')
plt.plot(frequencies_SYN, abs(SYN_fft), label = 'SYN')
plt.yscale('log')
plt.xlim(0,10000)

plt.xlabel('Frecuencias')
plt.title(nombre_SYN)
plt.legend()
plt.show() 
