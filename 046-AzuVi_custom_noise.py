#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL046-AzuVi'
nombre_BOS = 'zf-JL046-AzuVi_BOS.wav'

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
rectas(0.099, 0.1125,
       470, 470,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(0.1125, 0.1974,
     470, 590-470,
     0 , np.pi,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

# i2
rectas(0.3313 , 0.3375,
       625, 625,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.3375, 0.3445,
       625, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.3445, 0.3498,
       960, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

expo(0.3498, 0.4102,
       960, 450,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# i3
rectas(0.3313 + 0.1713 , 0.3375 + 0.1713,
       625, 625,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.3375 + 0.1713, 0.3445 + 0.1713,
       625, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.3445 + 0.1713, 0.3498 + 0.1713,
       960, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

expo(0.3498 + 0.1713, 0.4102 + 0.1713,
       960, 450,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# i4
rectas(0.3313 + 0.3005, 0.3375 + 0.3005,
       625, 625,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.3375 + 0.3005, 0.3445 + 0.3005,
       625, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.3445 + 0.3005, 0.3498 + 0.3005,
       960, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

expo(0.3498 + 0.3005, 0.4102 + 0.3005,
       960, 450,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# A
rectas(0.7554, 0.7580,
       3000, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7580, 0.7606,
       7500, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.7606, 0.7635,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7635, 0.7655,
       3000, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7655, 0.7715,
       1400, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.7715, 0.7735,
     1400, 4800,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

senito(0.7735, 0.7879,
     3650, 1150,
     np.pi*1/4 , np.pi*17/4,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.7879, 0.8041,
       4400, 4900,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.8041, 0.8129,
       930, 930,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.8129, 0.8342,
       940, 940,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.8342, 0.8392,
       940, 1200,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

expo(0.8392, 0.8845,
       1200, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa




# B
rectas(0.9151, 0.9242,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.9242, 0.9265,
       700, 1360,
       frequencias, silabas_timestamp,
       ruido_beta_list, 0.1, ruido_alfa) # no se completa

rectas(0.9265, 0.9392,
       2000, 2000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9392, 0.9733,
       2000, 1500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9733, 1.0675,
       1500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.15) # no se completa



# C
rectas(1.1043, 1.1112,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.1112, 1.1577,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1577, 1.1739,
       500, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# D
rectas(1.1927, 1.1970,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1970, 1.2009,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2009, 1.2034,
       1600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2034, 1.2063,
       2800, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2063, 1.2083,
       7400, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2083, 1.2154,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.2154, 1.2243,
         1600, 500,
         np.pi , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, 0.1)

rectas(1.2243, 1.2284,
       1600, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.2) # no se completa

rectas(1.2284, 1.2631,
       1300, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.2631, 1.2672,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2672, 1.2742,
       1600, 600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2742, 1.2826,
       600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2826, 1.3245,
       1400, 300,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa


# E
rectas(1.3626, 1.3780,
       600, 950,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.3780, 1.4061,
       3800, 3700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.4061, 1.4402,
       2500, 1500 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.3) # no se completa

expo(1.4402, 1.5461,
       1400, 450 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# t1
senito(1.5996, 1.6197,
         760, 260,
         np.pi*3/2 , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, 0.1)

rectas(1.6197, 1.6459,
       760, 760 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.6459, 1.6595,
         400, 360,
         np.pi*1/2 , np.pi,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)


# t2
rectas(1.6851, 1.6933,
       600, 880 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.6933, 1.7047,
       880,  880,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.7047, 1.7110,
       880,  700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.7110, 1.7616,
       1000,  350,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa







# A
rectas(0.7554 + 1.0539, 0.7580 + 1.0539,
       3000, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7580 + 1.0539, 0.7606 + 1.0539,
       7500, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.7606 + 1.0539, 0.7635 + 1.0539,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7635 + 1.0539, 0.7655 + 1.0539,
       3000, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7655 + 1.0539, 0.7715 + 1.0539,
       1400, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.7715 + 1.0539, 0.7735 + 1.0539,
     1400, 4800,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

senito(0.7735 + 1.0539, 0.7879 + 1.0539,
     3650, 1150,
     np.pi*1/4 , np.pi*17/4,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.7879 + 1.0539, 0.8041 + 1.0539,
       4400, 4900,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.8041 + 1.0539, 0.8129 + 1.0539,
       930, 930,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.8129 + 1.0539, 0.8342 + 1.0539,
       940, 940,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.8342 + 1.0539, 0.8392 + 1.0539,
       940, 1200,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

expo(0.8392 + 1.0539, 0.8845 + 1.0539,
       1200, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa




# B
rectas(0.9151 + 1.0539, 0.9242 + 1.0539,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.9242 + 1.0539, 0.9265 + 1.0539,
       700, 1360,
       frequencias, silabas_timestamp,
       ruido_beta_list, 0.1, ruido_alfa) # no se completa

rectas(0.9265 + 1.0539, 0.9392 + 1.0539,
       2000, 2000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9392 + 1.0539, 0.9733 + 1.0539,
       2000, 1500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9733 + 1.0539, 1.0675 + 1.0539,
       1500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.15) # no se completa



# C
rectas(1.1043 + 1.0539, 1.1112 + 1.0539,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.1112 + 1.0539, 1.1577 + 1.0539,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1577 + 1.0539, 1.1739 + 1.0539,
       500, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# D
rectas(1.1927 + 1.0539, 1.1970 + 1.0539,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1970 + 1.0539, 1.2009 + 1.0539,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2009 + 1.0539, 1.2034 + 1.0539,
       1600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2034 + 1.0539, 1.2063 + 1.0539,
       2800, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2063 + 1.0539, 1.2083 + 1.0539,
       7400, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2083 + 1.0539, 1.2154 + 1.0539,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.2154 + 1.0539, 1.2243 + 1.0539,
         1600, 500,
         np.pi , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, 0.1)

rectas(1.2243 + 1.0539, 1.2284 + 1.0539,
       1600, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.2) # no se completa

rectas(1.2284 + 1.0539, 1.2631 + 1.0539,
       1300, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.2631 + 1.0539, 1.2672 + 1.0539,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2672 + 1.0539, 1.2742 + 1.0539,
       1600, 600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2742 + 1.0539, 1.2826 + 1.0539,
       600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2826 + 1.0539, 1.3245 + 1.0539,
       1400, 300,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa


# E
rectas(1.3626 + 1.0539, 1.3780 + 1.0539,
       600, 950,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.3780 + 1.0539, 1.4061 + 1.0539,
       3800, 3700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.4061 + 1.0539, 1.4402 + 1.0539,
       2500, 1500 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.3) # no se completa

expo(1.4402 + 1.0539, 1.5461 + 1.0539,
       1400, 450 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa








# t3
senito(2.6749, 2.7019,
         680, 100,
         np.pi*3/2 , np.pi*(3.5),
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)

expo(2.7019, 2.7473,
       580,  400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

# t1
senito(1.5996 + 1.1886, 1.6197 + 1.1886,
         760, 260,
         np.pi*3/2 , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, 0.1)

rectas(1.6197 + 1.1886, 1.6459 + 1.1886,
       760, 760 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.6459 + 1.1886, 1.6595 + 1.1886,
         400, 360,
         np.pi*1/2 , np.pi,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)

# t2
rectas(1.6851 + 1.1886, 1.6933 + 1.1886,
       600, 880 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.6933 + 1.1886, 1.7047 + 1.1886,
       880,  880,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.7047 + 1.1886, 1.7110 + 1.1886,
       880,  700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.7110 + 1.1886, 1.7616 + 1.1886,
       1000,  350,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa









# A
rectas(0.7554 + 2.2578, 0.7580 + 2.2578,
       3000, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7580 + 2.2578, 0.7606 + 2.2578,
       7500, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.7606 + 2.2578, 0.7635 + 2.2578,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7635 + 2.2578, 0.7655 + 2.2578,
       3000, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7655 + 2.2578, 0.7715 + 2.2578,
       1400, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.7715 + 2.2578, 0.7735 + 2.2578,
     1400, 4800,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

senito(0.7735 + 2.2578, 0.7879 + 2.2578,
     3650, 1150,
     np.pi*1/4 , np.pi*17/4,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.7879 + 2.2578, 0.8041 + 2.2578,
       4400, 4900,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.8041 + 2.2578, 0.8129 + 2.2578,
       930, 930,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.812 + 2.25789, 0.8342 + 2.2578,
       940, 940,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.8342 + 2.2578, 0.8392 + 2.2578,
       940, 1200,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

expo(0.8392 + 2.2578, 0.8845 + 2.2578,
       1200, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa




# B
rectas(0.9151 + 2.2578, 0.9242 + 2.2578,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.9242 + 2.2578, 0.9265 + 2.2578,
       700, 1360,
       frequencias, silabas_timestamp,
       ruido_beta_list, 0.1, ruido_alfa) # no se completa

rectas(0.9265 + 2.2578, 0.9392 + 2.2578,
       2000, 2000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9392 + 2.2578, 0.9733 + 2.2578,
       2000, 1500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9733 + 2.2578, 1.0675 + 2.2578,
       1500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.15) # no se completa



# C
rectas(1.1043 + 2.2578, 1.1112 + 2.2578,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.1112 + 2.2578, 1.1577 + 2.2578,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1577 + 2.2578, 1.1739 + 2.2578,
       500, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# D
rectas(1.1927 + 2.2578, 1.1970 + 2.2578,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1970 + 2.2578, 1.2009 + 2.2578,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2009 + 2.2578, 1.2034 + 2.2578,
       1600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2034 + 2.2578, 1.2063 + 2.2578,
       2800, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2063 + 2.2578, 1.2083 + 2.2578,
       7400, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2083 + 2.2578, 1.2154 + 2.2578,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.2154 + 2.2578, 1.2243 + 2.2578,
         1600, 500,
         np.pi , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, 0.1)

rectas(1.2243 + 2.2578, 1.2284 + 2.2578,
       1600, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.2) # no se completa

rectas(1.2284 + 2.2578, 1.2631 + 2.2578,
       1300, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.2631 + 2.2578, 1.2672 + 2.2578,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2672 + 2.2578, 1.2742 + 2.2578,
       1600, 600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2742 + 2.2578, 1.2826 + 2.2578,
       600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2826 + 2.2578, 1.3245 + 2.2578,
       1400, 300,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa


# E
rectas(1.3626 + 2.2578, 1.3780 + 2.2578,
       600, 950,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.3780 + 2.2578, 1.4061 + 2.2578,
       3800, 3700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.4061 + 2.2578, 1.4402 + 2.2578,
       2500, 1500 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.3) # no se completa

expo(1.4402 + 2.2578, 1.5461 + 2.2578,
       1400, 450 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa







# t3
senito(2.6749 + 1.2029, 2.7019 + 1.2029,
         680, 100,
         np.pi*3/2 , np.pi*(3.5),
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)

expo(2.7019 + 1.2029, 2.7473 + 1.2029,
       580,  400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# t1
senito(1.5996 + 2.3916, 1.6197 + 2.3916,
         760, 260,
         np.pi*3/2 , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, 0.1)

rectas(1.6197 + 2.3916, 1.6459 + 2.3916,
       760, 760 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.6459 + 2.3916, 1.6595 + 2.3916,
         400, 360,
         np.pi*1/2 , np.pi,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)

# t2
rectas(1.6851 + 2.3916, 1.6933 + 2.3916,
       600, 880 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.6933 + 2.3916, 1.7047 + 2.3916,
       880,  880,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.7047 + 2.3916, 1.7110 + 2.3916,
       880,  700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.7110 + 2.3916, 1.7616 + 2.3916,
       1000,  350,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa







# A
rectas(0.7554 + 3.4604, 0.7580 + 3.4604,
       3000, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7580 + 3.4604, 0.7606 + 3.4604,
       7500, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.7606 + 3.4604, 0.7635 + 3.4604,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7635 + 3.4604, 0.7655 + 3.4604,
       3000, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7655 + 3.4604, 0.7715 + 3.4604,
       1400, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.7715 + 3.4604, 0.7735 + 3.4604,
     1400, 4800,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

senito(0.7735 + 3.4604, 0.7879 + 3.4604,
     3650, 1150,
     np.pi*1/4 , np.pi*17/4,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.7879 + 3.4604, 0.8041 + 3.4604,
       4400, 4900,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.8041 + 3.4604, 0.8129 + 3.4604,
       930, 930,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.8129 + 3.4604, 0.8342 + 3.4604,
       940, 940,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.4) # no se completa

rectas(0.8342 + 3.4604, 0.8392 + 3.4604,
       940, 1200,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

expo(0.8392 + 3.4604, 0.8845 + 3.4604,
       1200, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa




# B
rectas(0.9151 + 3.4604, 0.9242 + 3.4604,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(0.9242 + 3.4604, 0.9265 + 3.4604,
       700, 1360,
       frequencias, silabas_timestamp,
       ruido_beta_list, 0.1, ruido_alfa) # no se completa

rectas(0.9265 + 3.4604, 0.9392 + 3.4604,
       2000, 2000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9392 + 3.4604, 0.9733 + 3.4604,
       2000, 1500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9733 + 3.4604, 1.0675 + 3.4604,
       1500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.15) # no se completa



# C
rectas(1.1043 + 3.4604, 1.1112 + 3.4604,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.1112 + 3.4604, 1.1577 + 3.4604,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1577 + 3.4604, 1.1739 + 3.4604,
       500, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# D
rectas(1.1927 + 3.4604, 1.1970 + 3.4604,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.1970 + 3.4604, 1.2009 + 3.4604,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2009 + 3.4604, 1.2034 + 3.4604,
       1600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2034 + 3.4604, 1.2063 + 3.4604,
       2800, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2063 + 3.4604, 1.2083 + 3.4604,
       7400, 7400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2083 + 3.4604, 1.2154 + 3.4604,
       7400, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.2154 + 3.4604, 1.2243 + 3.4604,
         1600, 500,
         np.pi , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, 0.1)

rectas(1.2243 + 3.4604, 1.2284 + 3.4604,
       1600, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.2) # no se completa

rectas(1.2284 + 3.4604, 1.2631 + 3.4604,
       1300, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa

rectas(1.2631 + 3.4604, 1.2672 + 3.4604,
       700, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2672 + 3.4604, 1.2742 + 3.4604,
       1600, 600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2742 + 3.4604, 1.2826 + 3.4604,
       600, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.2826 + 3.4604, 1.3245 + 3.4604,
       1400, 300,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.1) # no se completa


# E
rectas(1.3626 + 3.4604, 1.3780 + 3.4604,
       600, 950,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.3780 + 3.4604, 1.4061 + 3.4604,
       3800, 3700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.4061 + 3.4604, 1.4402 + 3.4604,
       2500, 1500 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, 0.3) # no se completa

expo(1.4402 + 3.4604, 1.5461 + 3.4604,
       1400, 450 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa




