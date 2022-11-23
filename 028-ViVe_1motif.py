#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL028-ViVe'
nombre_BOS = 'zf-JL028-ViVe_BOS_44100_70dB_band_band_2.wav'

# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales

# expo(ti,tf,
# wi,wf,
# frequencias, 
# silabas_timestamp)

# rectas(ti,tf,
# wi,wf,
# frequencias,
# silabas_timestamp)

# senito(ti,tf,
# media,amplitud,
# alphai,alphaf,
# frequencias,
# silabas_timestamp)


# i1
expo(0.0604, 0.0762,
650,1620,
frequencias, 
silabas_timestamp)

rectas(0.0762, 0.0962,
1620,1500,
frequencias,
silabas_timestamp)

expo(0.0962, 0.1424,
1500,500,
frequencias, 
silabas_timestamp)


# i2
expo(0.2488, 0.2648,
650,1620,
frequencias, 
silabas_timestamp)

rectas(0.2648, 0.2848,
1620,1500,
frequencias,
silabas_timestamp)

expo(0.2848, 0.3287,
1500,500,
frequencias, 
silabas_timestamp)


# A
expo(0.3931, 0.4111,
650,1620,
frequencias, 
silabas_timestamp)

rectas(0.4111, 0.4275,
1620,1500,
frequencias,
silabas_timestamp)

expo(0.4275, 0.4706,
1500,500,
frequencias, 
silabas_timestamp)


# B
rectas(0.4768, 0.5092,
4400, 4400,
frequencias,
silabas_timestamp)

rectas(0.5092, 0.5259,
3400, 3400,
frequencias,
silabas_timestamp)


# C
rectas(0.5534, 0.5606,
1300,1100,
frequencias,
silabas_timestamp)

rectas(0.5606, 0.5652,
1100,2400,
frequencias,
silabas_timestamp)

rectas(0.5652, 0.5826,
2400,2400,
frequencias,
silabas_timestamp)

rectas(0.5826, 0.5884,
2400,800,
frequencias,
silabas_timestamp)

rectas(0.5884, 0.5967,
800,800,
frequencias,
silabas_timestamp)

rectas(0.5967, 0.6171,
600,600,
frequencias,
silabas_timestamp)

rectas(0.6171, 0.6309,
600,450,
frequencias,
silabas_timestamp)



# D
rectas(0.6612, 0.6697,
1200,1000,
frequencias,
silabas_timestamp)

rectas(0.6697, 0.6793,
1000,2100,
frequencias,
silabas_timestamp)

rectas(0.6793, 0.6911,
2100,2100,
frequencias,
silabas_timestamp)

expo(0.6911,0.7387,
2100, 400,
frequencias, 
silabas_timestamp)


# E1
rectas(0.7713, 0.7790,
850,850,
frequencias,
silabas_timestamp)

rectas(0.7790, 0.7831,
850,550,
frequencias,
silabas_timestamp)

rectas(0.7831, 0.8200,
550,550,
frequencias,
silabas_timestamp)

rectas(0.8200, 0.8415,
550,400,
frequencias,
silabas_timestamp)


# F
rectas(0.8729, 0.8777,
700,850,
frequencias,
silabas_timestamp)

rectas(0.8777, 0.8907,
850, 850,
frequencias,
silabas_timestamp)

expo(0.8907, 0.8960,
850, 700,
frequencias, 
silabas_timestamp)

expo(0.8960,0.9042,
700,1200,
frequencias, 
silabas_timestamp)

expo(0.9042,0.9096,
2200,4200,
frequencias, 
silabas_timestamp)

# DUDA
# que pasa en 0.9096, 0.9128

expo(0.9096,0.9159,
4500,1650,
frequencias, 
silabas_timestamp)

expo(0.9159,0.9208,
1650,1650,
frequencias, 
silabas_timestamp)

rectas(0.9208,0.9511,
400,400,
frequencias, 
silabas_timestamp)


# G
expo(0.9743,0.9812,
800,1600,
frequencias, 
silabas_timestamp)

rectas(0.9812, 0.9849,
2300,2300,
frequencias, 
silabas_timestamp)

rectas(0.9849,0.9914,
4400,4400,
frequencias,
silabas_timestamp)

rectas(0.9914,0.9979,
2100,1300,
frequencias,
silabas_timestamp)

expo(0.9979,1.0011,
1300,1550,
frequencias, 
silabas_timestamp)

expo(1.0011,1.0040,
1550,1200,
frequencias, 
silabas_timestamp)

expo(1.0040,1.0493,
1200, 400,
frequencias, 
silabas_timestamp)


# H / E2
rectas(0.7713 + 0.3082, 0.7790 + 0.3082,
850,850,
frequencias,
silabas_timestamp)

rectas(0.7790 + 0.3082, 0.7831 + 0.3082,
850,550,
frequencias,
silabas_timestamp)

rectas(0.7831 + 0.3082, 0.8200 + 0.3082,
550,550,
frequencias,
silabas_timestamp)

rectas(0.8200 + 0.3082, 0.8415 + 0.3082,
550,400,
frequencias,
silabas_timestamp)


# I
rectas(1.2153, 1.2179,
1000,2500,
frequencias,
silabas_timestamp)

rectas(1.2179, 1.2313,
2500,2500,
frequencias,
silabas_timestamp)

expo(1.2313,1.2835,
2500,430,
frequencias, 
silabas_timestamp)

rectas(1.2835,1.2994,
700,700,
frequencias,
silabas_timestamp)

expo(1.2994, 1.3075,
700,2300,
frequencias, 
silabas_timestamp)

rectas(1.3075, 1.3147,
2300, 2300,
frequencias,
silabas_timestamp)

expo(1.3147, 1.3191,
2300,1250,
frequencias,
silabas_timestamp)

expo(1.3191, 1.3227,
1250,1400,
frequencias, 
silabas_timestamp)

expo(1.3227,1.3260,
1400,950,
frequencias, 
silabas_timestamp)

rectas(1.3260, 1.3316,
950,950,
frequencias,
silabas_timestamp)

rectas(1.3316, 1.3395,
750,750,
frequencias,
silabas_timestamp)

rectas(1.3395,1.3709,
750,400,
frequencias,
silabas_timestamp)


# J / E3 
rectas(0.7713 + 0.6253, 0.7790 + 0.6253,
850,850,
frequencias,
silabas_timestamp)

rectas(0.7790 + 0.6253, 0.7831 + 0.6253,
850,550,
frequencias,
silabas_timestamp)

rectas(0.7831 + 0.6253, 0.8200 + 0.6253,
550,550,
frequencias,
silabas_timestamp)

rectas(0.8200 + 0.6253, 0.8415 + 0.6253,
550,400,
frequencias,
silabas_timestamp)


# K
rectas(1.5648, 1.5897,
500, 825,
frequencias,
silabas_timestamp)

rectas(1.5897,1.6500,
825,500,
frequencias,
silabas_timestamp)

# L
rectas(1.6917, 1.7237,
500,630,
frequencias,
silabas_timestamp)

rectas(1.7237, 1.8299,
630,630,
frequencias,
silabas_timestamp)

rectas(1.8299,1.8580,
630, 500,
frequencias,
silabas_timestamp)

# M
rectas(1.8968, 1.9111,
600, 820,
frequencias,
silabas_timestamp)

rectas(1.9111, 1.9407,
820, 820,
frequencias,
silabas_timestamp)

rectas(1.9407, 2.0196,
820,600,
frequencias,
silabas_timestamp)
