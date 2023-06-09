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