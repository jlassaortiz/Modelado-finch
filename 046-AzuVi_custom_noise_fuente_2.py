#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL046-AzuVi_fuente_2'
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
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.3375, 0.3445,
       625, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.3445, 0.3498,
       960, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.3498, 0.4102,
       960, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# i3
rectas(0.3313 + 0.1713 , 0.3375 + 0.1713,
       625, 625,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.3375 + 0.1713, 0.3445 + 0.1713,
       625, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.3445 + 0.1713, 0.3498 + 0.1713,
       960, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.3498 + 0.1713, 0.4102 + 0.1713,
       960, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# i4
rectas(0.3313 + 0.3005, 0.3375 + 0.3005,
       625, 625,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.3375 + 0.3005, 0.3445 + 0.3005,
       625, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.3445 + 0.3005, 0.3498 + 0.3005,
       960, 960,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.3498 + 0.3005, 0.4102 + 0.3005,
       960, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# A
rectas(0.7554, 0.7580,
       3000, 7500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7580, 0.7606,
       7500, 7500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.7606, 0.7635,
       7500, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7635, 0.7655,
       3000, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.7655, 0.7715,
       1400, 1400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

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
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.8129, 0.8342,
       940, 940,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.8342, 0.8392,
       940, 1200,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(0.8392, 0.8825,
       1200, 400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa




# B
rectas(0.9151, 0.9242,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9242, 0.9265,
       700, 1360,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9265, 0.9392,
       1350, 1350,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9392, 0.9733,
       2000, 1500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

#rectas(0.9733, 1.0675,
#       1500, 550,
#       frequencias, silabas_timestamp,
#       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.9733, 1.0675,
       1100, 350,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# C
rectas(1.1043, 1.1112,
       500, 500,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

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

rectas(1.2034, 1.2081,
       2800, 2800,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2081, 1.2109,
       3000, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2109, 1.2154,
       3000, 3000,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(1.2154, 1.2243,
         1600, 500,
         np.pi , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)

rectas(1.2243, 1.2284,
       1600, 1600,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.2284, 1.2631,
       1300, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

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
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa


# E
rectas(1.3626, 1.3780,
       600, 950,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.3780, 1.4061,
       3800, 3700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

#rectas(1.4061, 1.4402,
#       2100, 1400 ,
#       frequencias, silabas_timestamp,
#       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.4061, 1.4402,
       2000, 1200 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.4402, 1.5461,
       1400, 450 ,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# t1
senito(1.5996, 1.6197,
         760, 260,
         np.pi*3/2 , np.pi*2,
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)

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
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(1.7047, 1.7110,
       880,  700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

expo(1.7110, 1.7616,
       1000,  350,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa



# t3 (esta mucho mas adelante en el canto, lo hago antes para poner a punto el ruido)
senito(2.6749, 2.7019,
         680, 100,
         np.pi*3/2 , np.pi*(3.5),
         frequencias, silabas_timestamp,
         ruido_beta_list, ruido_beta, ruido_alfa)

expo(2.7019, 2.7473,
       580,  400,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa