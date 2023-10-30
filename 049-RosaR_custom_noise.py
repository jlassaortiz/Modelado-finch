#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL049-RosaR'
nombre_BOS = 'zf-JL046-RosaR_BOS.wav'

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
rectas(0.1111, 0.1295,
       900, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.1295, 0.1366,
     700, 800,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.1366, 0.1506,
     800, 650,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.1506 , 0.1784,
       650, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) 

rectas(0.1784 , 0.1897,
       430, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)


# i2
rectas(0.2425, 0.2602,
       900, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.2602, 0.2658,
       700, 800,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.2658, 0.2800,
     800, 650,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.2800, 0.3103,
     650, 430,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.3103 , 0.3156,
       430, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)


# i3
rectas(0.3758, 0.3948,
       900, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.3948, 0.4000,
       700, 800,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.4000, 0.4159,
     800, 650,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.4159, 0.4433,
     650, 430,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.4433, 0.4499,
       430, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)


# i4
rectas(0.5139, 0.5279,
       900, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.5279, 0.5342,
       700, 800,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.5342, 0.5513,
     800, 650,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.5513, 0.5722,
     650, 430,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.5722, 0.5835,
       430, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)



# i5
rectas(0.6343, 0.6539,
       900, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.6539, 0.6602,
       700, 800,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.6602, 0.6772,
     800, 650,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.6772, 0.7045,
     650, 430,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.7045, 0.7119,
       430, 430,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)


# A
rectas(0.7515, 0.7582,
       700, 700,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.7582, 0.7858,
       2050, 2050,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)

rectas(0.7858, 0.8244,
       530, 530,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa)







expo(0.3498, 0.4102,
       960, 450,
       frequencias, silabas_timestamp,
       ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

senito(0.7735, 0.7879,
     3650, 1150,
     np.pi*1/4 , np.pi*17/4,
     frequencias, silabas_timestamp,
     ruido_beta_list, ruido_beta, ruido_alfa)




