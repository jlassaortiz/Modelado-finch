#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL022-NeRo'
nombre_BOS = 'zf-JL022-NeRo_BOS_44100Hz_70dB_band.wav'

# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales

# expo(ti,tf,
# wi,wf,
# factor,
# frequencias, silabas_timestamp)

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
rectas(0.082,0.093,
       1250,1250,
       frequencias,
       silabas_timestamp)

rectas(0.093,0.106,
       1250,600,
       frequencias,
       silabas_timestamp)

rectas(0.106,0.129,
       600,600,
       frequencias,
       silabas_timestamp)

rectas(0.129, 0.153,
       600,370,
       frequencias,
       silabas_timestamp)


# A
rectas(0.256, 0.274,
       1350, 1350,
       frequencias,
       silabas_timestamp)

rectas(0.274, 0.289,
       1350, 600,
       frequencias,
       silabas_timestamp)

rectas(0.289, 0.309,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.309, 0.327,
       600, 400,
       frequencias,
       silabas_timestamp)


# B 
rectas(0.354, 0.360,
       1700, 1700,
       frequencias,
       silabas_timestamp)

rectas(0.360, 0.365,
       1300, 1300,
       frequencias,
       silabas_timestamp)

rectas(0.365, 0.377,
       2400, 2400,
       frequencias,
       silabas_timestamp)

rectas(0.377, 0.387,
       2400, 600,
       frequencias,
       silabas_timestamp)

rectas(0.387, 0.409,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.409, 0.425,
       600, 500,
       frequencias,
       silabas_timestamp)

# C
rectas(0.445, 0.455,
       3900, 3900,
       frequencias,
       silabas_timestamp)

rectas(0.455, 0.465,
       1000, 1000,
       frequencias,
       silabas_timestamp)

rectas(0.465, 0.505,
       530, 530,
       frequencias,
       silabas_timestamp)

rectas(0.505, 0.523,
       2600, 2600,
       frequencias,
       silabas_timestamp)


# D
rectas(0.551, 0.571,
       2900, 2900,
       frequencias,
       silabas_timestamp)

rectas(0.571, 0.578,
       3400, 3400,
       frequencias,
       silabas_timestamp)

rectas(0.578, 0.613,
       2900, 2900,
       frequencias,
       silabas_timestamp)

# E
rectas(0.649, 0.725,
       2300, 2300,
       frequencias,
       silabas_timestamp)

# F
rectas(0.759, 0.862,
       630, 630,
       frequencias,
       silabas_timestamp)

rectas(0.862, 0.892,
       2000, 2000,
       frequencias,
       silabas_timestamp)

# G
rectas(0.912, 0.919,
       970, 970,
       frequencias,
       silabas_timestamp)

rectas(0.919, 0.978,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.978, 1.024,
       420, 420,
       frequencias,
       silabas_timestamp)








# A2
rectas(0.256 + 0.875, 0.274 + 0.875,
       1350, 1350,
       frequencias,
       silabas_timestamp)

rectas(0.274 + 0.875, 0.289 + 0.875,
       1350, 600,
       frequencias,
       silabas_timestamp)

rectas(0.289 + 0.875, 0.309 + 0.875,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.309 + 0.875, 0.327 + 0.875,
       600, 400,
       frequencias,
       silabas_timestamp)


# B2
rectas(0.354 + 0.875, 0.360 + 0.875,
       1700, 1700,
       frequencias,
       silabas_timestamp)

rectas(0.360 + 0.875, 0.365 + 0.875,
       1300, 1300,
       frequencias,
       silabas_timestamp)

rectas(0.365 + 0.875, 0.377 + 0.875,
       2400, 2400,
       frequencias,
       silabas_timestamp)

rectas(0.377 + 0.875, 0.387 + 0.875,
       2400, 600,
       frequencias,
       silabas_timestamp)

rectas(0.387 + 0.875, 0.409+ 0.875, 
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.409 + 0.875, 0.425 + 0.875,
       600, 500,
       frequencias,
       silabas_timestamp)

# C2
rectas(0.445 + 0.875, 0.455 + 0.875,
       3900, 3900,
       frequencias,
       silabas_timestamp)

rectas(0.455 + 0.875, 0.465 + 0.875,
       1000, 1000,
       frequencias,
       silabas_timestamp)

rectas(0.465 + 0.875, 0.505 + 0.875,
       530, 530,
       frequencias,
       silabas_timestamp)

rectas(0.505 + 0.875, 0.523 + 0.875,
       2600, 2600,
       frequencias,
       silabas_timestamp)


# D2
rectas(0.551 + 0.875, 0.571 + 0.875,
       2900, 2900,
       frequencias,
       silabas_timestamp)

rectas(0.571 + 0.875, 0.578 + 0.875,
       3400, 3400,
       frequencias,
       silabas_timestamp)

rectas(0.578 + 0.875, 0.613 + 0.875,
       2900, 2900,
       frequencias,
       silabas_timestamp)

# E2
rectas(0.649 + 0.875, 0.725 + 0.875,
       2300, 2300,
       frequencias,
       silabas_timestamp)

# F2
rectas(0.759 + 0.875, 0.862 + 0.875,
       630, 630,
       frequencias,
       silabas_timestamp)

rectas(0.862 + 0.875, 0.892 + 0.875,
       2000, 2000,
       frequencias,
       silabas_timestamp)

# G2
rectas(0.912 + 0.875, 0.919 + 0.875,
       970, 970,
       frequencias,
       silabas_timestamp)

rectas(0.919 + 0.875, 0.978 + 0.875,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.978 + 0.875, 1.024 + 0.875,
       420, 420,
       frequencias,
       silabas_timestamp)









# A3
rectas(0.256 + 1.749, 0.274 + 1.749,
       1350, 1350,
       frequencias,
       silabas_timestamp)

rectas(0.274 + 1.749, 0.289 + 1.749,
       1350, 600,
       frequencias,
       silabas_timestamp)

rectas(0.289 + 1.749, 0.309 + 1.749,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.309 + 1.749, 0.327 + 1.749,
       600, 400,
       frequencias,
       silabas_timestamp)


# B3
rectas(0.354 + 1.749, 0.360 + 1.749,
       1700, 1700,
       frequencias,
       silabas_timestamp)

rectas(0.360 + 1.749, 0.365 + 1.749,
       1300, 1300,
       frequencias,
       silabas_timestamp)

rectas(0.365 + 1.749, 0.377 + 1.749,
       2400, 2400,
       frequencias,
       silabas_timestamp)

rectas(0.377 + 1.749, 0.387 + 1.749,
       2400, 600,
       frequencias,
       silabas_timestamp)

rectas(0.387 + 1.749, 0.409 + 1.749,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.409 + 1.749, 0.425 + 1.749,
       600, 500,
       frequencias,
       silabas_timestamp)

# C3
rectas(0.445 + 1.749, 0.455 + 1.749,
       3900, 3900,
       frequencias,
       silabas_timestamp)

rectas(0.455 + 1.749, 0.465 + 1.749,
       1000, 1000,
       frequencias,
       silabas_timestamp)

rectas(0.465 + 1.749, 0.505 + 1.749,
       530, 530,
       frequencias,
       silabas_timestamp)

rectas(0.505 + 1.749, 0.523 + 1.749,
       2600, 2600,
       frequencias,
       silabas_timestamp)


# D3
rectas(0.551 + 1.749, 0.571 + 1.749,
       2900, 2900,
       frequencias,
       silabas_timestamp)

rectas(0.571 + 1.749, 0.578 + 1.749,
       3400, 3400,
       frequencias,
       silabas_timestamp)

rectas(0.578 + 1.749, 0.613 + 1.749,
       2900, 2900,
       frequencias,
       silabas_timestamp)

# E3
rectas(0.649 + 1.749, 0.725 + 1.749,
       2300, 2300,
       frequencias,
       silabas_timestamp)

# F3
rectas(0.759 + 1.749, 0.862 + 1.749,
       630, 630,
       frequencias,
       silabas_timestamp)

rectas(0.862 + 1.749, 0.892 + 1.749,
       2000, 2000,
       frequencias,
       silabas_timestamp)

# G3
rectas(0.912 + 1.749, 0.919 + 1.749,
       970, 970,
       frequencias,
       silabas_timestamp)

rectas(0.919 + 1.749, 0.978 + 1.749,
       600, 600,
       frequencias,
       silabas_timestamp)

rectas(0.978 + 1.749, 1.024 + 1.749,
       420, 420,
       frequencias,
       silabas_timestamp)

















