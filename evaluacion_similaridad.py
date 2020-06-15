"""
Created on Fri Jun 12 17:05:58 2020
@author: Javier Lassa Ortiz

Análisis de similaridad entre canto sintetico y canto original.
Genera graficos y tabla comparativa

Estructura del codigo:
    - Variables a completar por el usuario
    - Librerias necesarias
"""

# ------------------------------------
# Variables a completar por el usuario 
# ------------------------------------

# Directorio donde estan los archivos de audio del BOS y el SYN
# TIENEN QUE TENER EL MISMO SAMPLING RATE !
bos_path = "zfAB010-bi_BOS03_44100.wav"
syn_path = "sintesis_finch_2_0.wav" 

# --------------------
# Librerias necesarias 
# --------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import scipy.io.wavfile as scw
import scipy.signal as scs

# -------------------------
# Cargo canciones y comparo
# -------------------------

# LEO archivos
bos_s_rate, b = scw.read(bos_path)
syn_s_rate, s = scw.read(syn_path)

bos = np.copy(b)
syn = np.copy(s)

len_bos = len(bos)
len_syn = len(syn)
diff = abs(len_bos - len_syn)

# Obligo a tener exactamente el mismo tamaño
if len_bos > len_syn:
    bos.resize(len_syn)
elif len_bos < len_syn:
    syn.resize(len_bos)
    
    
# HILBERT 
bos_h = scs.hilbert(bos)
syn_h = scs.hilbert(syn)
    
diff_bos_syn = bos - syn

diff_h = bos_h - syn_h

if bos_s_rate != syn_s_rate:
    print('CUIDADO! ARCHIVOS .WAV TIENE DISTINTO SAMPLING RATE!')




# Calculo maximo de la correlacion cruzada
cross_corr = np.correlate(bos, syn, mode = 'same')
cross_corr_scs = scs.correlate(bos, syn, mode = 'same')

# Calculo maximo de la correlacion cruzada
cross_corr_h = np.correlate(bos_h, syn_h, mode = 'same')
cross_corr_scs_h = scs.correlate(bos_h, syn_h, mode = 'same')


plt.plot(cross_corr)

plt.figure()
plt.plot(cross_corr_scs)

plt.figure()
plt.plot(cross_corr_h)

plt.figure()
plt.plot(cross_corr_scs_h)

plt.figure()
plt.plot(bos)
plt.plot(syn)

plt.figure()
plt.plot(bos_h)
plt.plot(syn_h)


# Calculo delay al punto de mayor correlacion




































