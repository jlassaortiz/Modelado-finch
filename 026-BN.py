#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL026-BN'
nombre_BOS = 'zf-JL026-BN_BOS_44100_70dB_band.wav'

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


# I1
rectas(0.1237,0.1711,
500,500,
frequencias,
silabas_timestamp)


# I2
rectas(0.2092,0.2268,
900, 1000,
frequencias,
silabas_timestamp)

expo(0.2268,0.2760,
1000,500,
frequencias,
silabas_timestamp)


# I3
rectas(0.3030,0.3070,
2900,2900,
frequencias,
silabas_timestamp)

rectas(0.3070,0.3138,
2300,2300,
frequencias,
silabas_timestamp)

rectas(0.3138, 0.3166,
2100, 2100,
frequencias,
silabas_timestamp)

rectas(0.3166, 0.3267,
2000, 1100,
frequencias,
silabas_timestamp)

rectas(0.3267, 0.3300,
1500, 1500,
frequencias,
silabas_timestamp)

rectas(0.3300, 0.3407,
570,570,
frequencias,
silabas_timestamp)

rectas(0.3407, 0.3455,
2600, 2600,
frequencias,
silabas_timestamp)

rectas(0.3455, 0.3487,
1700,1700,
frequencias,
silabas_timestamp)

rectas(0.3487, 0.3536,
3100, 3100,
frequencias,
silabas_timestamp)

rectas(0.3536, 0.3581,
2200,2200,
frequencias,
silabas_timestamp)

rectas(0.3581, 0.3599,
1500,1500,
frequencias,
silabas_timestamp)

expo(0.3599,0.4126,
1500,900,
frequencias,
silabas_timestamp)


# A
rectas(0.4430, 0.4471,
1000, 1400,
frequencias,
silabas_timestamp)

rectas(0.4471, 0.4621,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.4621,0.4682,
1400,1000,
frequencias,
silabas_timestamp)

rectas(0.4682, 0.4798,
1100,1100,
frequencias,
silabas_timestamp)

rectas(0.4798,0.4867,
2300,2300,
frequencias,
silabas_timestamp)

rectas(0.4867, 0.4925,
2400,2400,
frequencias,
silabas_timestamp)

rectas(0.4925, 0.5143,
5000, 5000,
frequencias,
silabas_timestamp)

rectas(0.5143, 0.5287,
5000,5400,
frequencias,
silabas_timestamp)

rectas(0.5287,0.5435,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.5435, 0.5512,
1400,1000,
frequencias,
silabas_timestamp)

rectas(0.5512, 0.5688,
1000,1000,
frequencias,
silabas_timestamp)


# B
rectas(0.5947, 0.6000,
2600,2600,
frequencias,
silabas_timestamp)

rectas(0.6000,0.6030,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.6030,0.6107,
3600,3600,
frequencias,
silabas_timestamp)

expo(0.6107, 0.6207,
1300,1000,
frequencias,
silabas_timestamp)

rectas(0.6207, 0.6285,
2500,2500,
frequencias,
silabas_timestamp)

rectas(0.6285, 0.6321,
1500,1500,
frequencias,
silabas_timestamp)

rectas(0.6321,0.6510,
1500,1100,
frequencias,
silabas_timestamp)

rectas(0.6535, 0.6703,
1950,1800,
frequencias,
silabas_timestamp)

rectas(0.6703,0.6801,
1100,1100,
frequencias,
silabas_timestamp)

rectas(0.6801,0.7068,
1000,1000,
frequencias,
silabas_timestamp)

rectas(0.7068, 0.7668,
574,574,
frequencias,
silabas_timestamp)

rectas(0.7668, 0.8100,
1128,1128,
frequencias,
silabas_timestamp)

rectas(0.8100, 0.9311,
1128,610,
frequencias,
silabas_timestamp)

rectas(0.9311, 0.9470,
610,510,
frequencias,
silabas_timestamp)



# A'
rectas(0.4430 + 0.5867, 0.4471 + 0.5867,
1000, 1400,
frequencias,
silabas_timestamp)

rectas(0.4471 + 0.5867, 0.4621 + 0.5867,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.4621 + 0.5867, 0.4682 + 0.5867,
1400,1000,
frequencias,
silabas_timestamp)

rectas(0.4682 + 0.5867, 0.4798 + 0.5867,
1100,1100,
frequencias,
silabas_timestamp)

rectas(0.4798 + 0.5867, 0.4867 + 0.5867,
2300,2300,
frequencias,
silabas_timestamp)

rectas(0.4867 + 0.5867, 0.4925 + 0.5867,
2400,2400,
frequencias,
silabas_timestamp)

rectas(0.4925 + 0.5867, 0.5143 + 0.5867,
5000, 5000,
frequencias,
silabas_timestamp)

rectas(0.5143 + 0.5867, 0.5287 + 0.5867,
5000,5400,
frequencias,
silabas_timestamp)

rectas(0.5287 + 0.5867, 0.5435 + 0.5867,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.5435 + 0.5867, 0.5512 + 0.5867,
1400,1000,
frequencias,
silabas_timestamp)

rectas(0.5512 + 0.5867, 0.5688 + 0.5867,
1000,1000,
frequencias,
silabas_timestamp)


# B'
rectas(0.5947 + 0.5867, 0.6000 + 0.5867,
2600,2600,
frequencias,
silabas_timestamp)

rectas(0.6000 + 0.5867, 0.6030 + 0.5867,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.6030 + 0.5867, 0.6107 + 0.5867,
3600,3600,
frequencias,
silabas_timestamp)

expo(0.6107 + 0.5867, 0.6207 + 0.5867,
1300,1000,
frequencias,
silabas_timestamp)

rectas(0.6207 + 0.5867, 0.6285 + 0.5867,
2500,2500,
frequencias,
silabas_timestamp)

rectas(0.6285 + 0.5867, 0.6321 + 0.5867,
1500,1500,
frequencias,
silabas_timestamp)

rectas(0.6321 + 0.5867, 0.6510 + 0.5867,
1500,1100,
frequencias,
silabas_timestamp)

rectas(0.6535 + 0.5867, 0.6703 + 0.5867,
1950,1800,
frequencias,
silabas_timestamp)

rectas(0.6703 + 0.5867, 0.6801 + 0.5867,
1100,1100,
frequencias,
silabas_timestamp)

rectas(0.6801 + 0.5867, 0.7068 + 0.5867,
1000,1000,
frequencias,
silabas_timestamp)

rectas(0.7068 + 0.5867, 0.7668 + 0.5867,
574,574,
frequencias,
silabas_timestamp)

rectas(0.7668 + 0.5867, 0.8100 + 0.5867,
1128,1128,
frequencias,
silabas_timestamp)

rectas(0.8100 + 0.5867, 0.9311 + 0.5867,
1128,610,
frequencias,
silabas_timestamp)

rectas(0.9311 + 0.5867, 0.9470 + 0.5867,
610,510,
frequencias,
silabas_timestamp)


# A''
rectas(0.4430 + 1.1749, 0.4471 + 1.1749,
1000, 1400,
frequencias,
silabas_timestamp)

rectas(0.4471 + 1.1749, 0.4621 + 1.1749,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.4621 + 1.1749, 0.4682 + 1.1749,
1400,1000,
frequencias,
silabas_timestamp)

rectas(0.4682 + 1.1749, 0.4798 + 1.1749,
1100,1100,
frequencias,
silabas_timestamp)

rectas(0.4798 + 1.1749, 0.4867 + 1.1749,
2300,2300,
frequencias,
silabas_timestamp)

rectas(0.4867 + 1.1749, 0.4925 + 1.1749,
2400,2400,
frequencias,
silabas_timestamp)

rectas(0.4925 + 1.1749, 0.5143 + 1.1749,
5000, 5000,
frequencias,
silabas_timestamp)

rectas(0.5143 + 1.1749, 0.5287 + 1.1749,
5000,5400,
frequencias,
silabas_timestamp)

rectas(0.5287 + 1.1749, 0.5435 + 1.1749,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.5435 + 1.1749, 0.5512 + 1.1749,
1400,1000,
frequencias,
silabas_timestamp)

rectas(0.5512 + 1.1749, 0.5688 + 1.1749,
1000,1000,
frequencias,
silabas_timestamp)


# B''
rectas(0.5947 + 1.1749, 0.6000 + 1.1749,
2600,2600,
frequencias,
silabas_timestamp)

rectas(0.6000 + 1.1749, 0.6030 + 1.1749,
1400,1400,
frequencias,
silabas_timestamp)

rectas(0.6030 + 1.1749, 0.6107 + 1.1749,
3600,3600,
frequencias,
silabas_timestamp)

expo(0.6107 + 1.1749, 0.6207 + 1.1749,
1300,1000,
frequencias,
silabas_timestamp)

rectas(0.6207 + 1.1749, 0.6285 + 1.1749,
2500,2500,
frequencias,
silabas_timestamp)

rectas(0.6285 + 1.1749, 0.6321 + 1.1749,
1500,1500,
frequencias,
silabas_timestamp)

rectas(0.6321 + 1.1749, 0.6510 + 1.1749,
1500,1100,
frequencias,
silabas_timestamp)

rectas(0.6535 + 1.1749, 0.6703 + 1.1749,
1950,1800,
frequencias,
silabas_timestamp)

rectas(0.6703 + 1.1749, 0.6801 + 1.1749,
1100,1100,
frequencias,
silabas_timestamp)

rectas(0.6801 + 1.1749, 0.7068 + 1.1749,
1000,1000,
frequencias,
silabas_timestamp)

rectas(0.7068 + 1.1749, 0.7668 + 1.1749,
574,574,
frequencias,
silabas_timestamp)

rectas(0.7668 + 1.1749, 0.8100 + 1.1749,
1128,1128,
frequencias,
silabas_timestamp)

rectas(0.8100 + 1.1749, 0.9311 + 1.1749,
1128,610,
frequencias,
silabas_timestamp)

rectas(0.9311 + 1.1749, 0.9470 + 1.1749,
610,510,
frequencias,
silabas_timestamp)



























