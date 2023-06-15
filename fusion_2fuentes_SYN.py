# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:46:26 2023

@author: jlassa
"""

from scipy.io.wavfile import write, read

fuente_1_name ='zf-JL046-AzuVi_fuente_2_SYN_v-final_G_24000_lambdaCabeza_1.0_lambdaCuello_1.0_Ch_4.00e-11_Rh_3.00e+05_Lg_6.00e+01_Rb_4.00e+08_Lb_5.00e+03_Ltraquea_4.8600e-02_coefReflex_-0.5_rBeta_0.05_rAlpha_0.01_rAmpl_0.0.wav'
fuente_2_name = 'zf-JL046-AzuVi_SYN_v-final_G_24000_lambdaCabeza_1.0_lambdaCuello_1.0_Ch_4.00e-11_Rh_3.00e+05_Lg_6.00e+01_Rb_4.00e+08_Lb_5.00e+03_Ltraquea_4.8600e-02_coefReflex_-0.5_rBeta_0.05_rAlpha_0.01_rAmpl_0.0.wav'

rate_syn, fuente_1 = read(fuente_1_name)
rate_syn, fuente_2 = read(fuente_2_name)

SYN_final = (fuente_1 + fuente_2) /2

write(f'SYN_final.wav', int(rate_syn), SYN_final)


