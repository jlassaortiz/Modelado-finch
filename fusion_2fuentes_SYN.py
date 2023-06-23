# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:46:26 2023

@author: jlassa
"""

from scipy.io.wavfile import write, read
import numpy as np
import matplotlib.pyplot as plt


fuente_1_name ='zf-JL046-AzuVi_SYN_v-final_G_24000_lambdaCabeza_0.5_lambdaCuello_0.5_Ch_5.00e-12_Rh_1.20e+06_Lg_1.20e+02_Rb_1.60e+09_Lb_1.00e+04_Ltraquea_2.4300e-02_coefReflex_-0.5_rBeta_0.35_rAlpha_0.01_rAmpl_0.0.wav'
fuente_2_name = 'zf-JL046-AzuVi_fuente_2_SYN_v-final_G_24000_lambdaCabeza_0.5_lambdaCuello_0.5_Ch_5.00e-12_Rh_1.20e+06_Lg_1.20e+02_Rb_1.60e+09_Lb_1.00e+04_Ltraquea_2.4300e-02_coefReflex_-0.5_rBeta_0.35_rAlpha_0.01_rAmpl_0.0.wav'
version_syn = 'CaCh_CuCh'


nombre_BOS = 'zf-JL046-AzuVi_BOS.wav'


rate_syn, fuente_1 = read(fuente_1_name)
rate_syn, fuente_2 = read(fuente_2_name)
rate_bos, BOS = read(nombre_BOS)

fuente_1 = fuente_1/(max(np.abs(fuente_1)))
fuente_2 = fuente_2/max(np.abs(fuente_2))

SYN_final = (fuente_1 + fuente_2) /2

####
plt.figure()
plt.plot(SYN_final)



SYN_final[47570:59508] = SYN_final[47570:59508] * 2.65
SYN_final[94501:105848] = SYN_final[94501:105848] * 2.95
SYN_final[147219:158720] = SYN_final[147219:158720] * 2.85
SYN_final[200809:211887] = SYN_final[200809:211887] * 3.30

SYN_final[int(0.8966*rate_bos):int(1.0795*rate_bos)] = SYN_final[int(0.8966*rate_bos):int(1.0795*rate_bos)] * 1.40
SYN_final[int(1.9532*rate_bos):int(2.1395*rate_bos)] = SYN_final[int(1.9532*rate_bos):int(2.1395*rate_bos)] * 1.40
SYN_final[int(3.1554*rate_bos):int(3.3417*rate_bos)] = SYN_final[int(3.1554*rate_bos):int(3.3417*rate_bos)] * 1.70
SYN_final[int(4.3577*rate_bos):int(4.5473*rate_bos)] = SYN_final[int(4.3577*rate_bos):int(4.5473*rate_bos)] * 1.60


plt.figure()
plt.plot(SYN_final)

###

escala = np.max(np.abs(BOS))
if BOS.dtype == 'float32':
    escala = escala / 1
elif BOS.dtype == 'int32':
    escala = escala / 2147483647
elif BOS.dtype == 'int16':
    escala = escala / 32767
elif BOS.dtype == 'uint8':
    escala = escala / 25

scaled = np.int16(SYN_final * escala * 32767)




write(f'zf-JL046-AzuVi_SYN_' + version_syn + '.wav', int(rate_syn), scaled)


