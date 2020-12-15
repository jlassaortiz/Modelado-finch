#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL016-NaVe'
nombre_BOS = 'zf-JL016-NaVe_BOS_long_44100.wav'

# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales y silabas_timestamp
    
# expo(ti,tf,
# wi,wf,
# factor,
# frequencias, silabas_timestamp)

# rectas(ti,tf,
# wi,wf,factor,
# frequencias, 
# silabas_timestamp)

# senito(ti,tf,
# media,amplitud,
# alphai,alphaf,
# factor,frequencias, 
# silabas_timestamp)

# Notas intro

# i1
rectas(0.1817, 0.1961,
       3100.0, 3100.0,
       frequencias, silabas_timestamp)
expo(  0.1961, 0.2134,
       3100.0, 750.0,
       frequencias, silabas_timestamp)


# i2
rectas(0.2717, 0.2861,
       3100.0, 3100.0,
       frequencias, silabas_timestamp)
expo(  0.2861, 0.3034,
       3100.0, 750.0,
       frequencias, silabas_timestamp)


# A
rectas(0.3642, 0.3757,
       1200.0, 2400.0,
       frequencias, silabas_timestamp)
expo(  0.3757, 0.3990,
       2400.0, 750.0,
       frequencias, silabas_timestamp)


# B
rectas(0.4071, 0.4345,
       2700.0, 2400.0,
       frequencias, silabas_timestamp)
rectas(0.4345, 0.4571,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# C
rectas(0.4687, 0.4882,
       2700.0, 2400.0,
       frequencias, silabas_timestamp)
rectas(0.4882, 0.5075,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# D1
rectas(0.5567, 0.5622,
       900.0, 900.0,
       frequencias, silabas_timestamp)
rectas(0.5622, 0.5648,
       3200.0, 3200.0,
       frequencias, silabas_timestamp)
rectas(0.5648, 0.5720,
       1200.0, 750.0,
       frequencias, silabas_timestamp)
# # D2
# rectas(0.5872, 0.5916,
#         4800.0, 4800.0,
#         frequencias, silabas_timestamp)
# expo(  0.5916, 0.6151,
#         4800.0, 450.0,
#         frequencias, silabas_timestamp)
# D3
# rectas(0.6151, 0.6191,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6191, 0.6390,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D4
# rectas(0.6390, 0.6429,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6429, 0.6623,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D5
# rectas(0.6623, 0.6671,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6671, 0.6859,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D6
# rectas(0.6859, 0.6908,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6908, 0.7095,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D7
# rectas(0.7095, 0.7163,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.7163, 0.7373,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# D8
rectas(0.7373, 0.7408,
       3400.0, 3400.0,
       frequencias, silabas_timestamp)
expo(  0.7408, 0.7654,
       3400.0, 450.0,
       frequencias, silabas_timestamp)


# E
rectas(0.7993, 0.8255,
       470.0, 420.0,
       frequencias, silabas_timestamp)
expo(  0.8255, 0.8410,
       420.0, 250.0,
       frequencias, silabas_timestamp)


# F
rectas(0.8895, 0.8931,
       1500.0, 1500.0,
       frequencias, silabas_timestamp)
rectas(0.8985, 0.9160,
       1800.0, 1500.0,
       frequencias, silabas_timestamp)
expo(  0.9160, 0.9300,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# G 
rectas(0.9589, 0.9626,
       1000.0, 1000.0,
       frequencias, silabas_timestamp)
rectas(0.9659, 0.9743,
       2000.0, 2000.0,
       frequencias, silabas_timestamp)
rectas(0.9784, 0.9987,
       1750.0, 1500.0,
       frequencias, silabas_timestamp)
rectas(0.9987, 1.0054,
       1500.0, 1400.0,
       frequencias, silabas_timestamp)
rectas(1.0054, 1.0160,
       1400.0, 1400.0,
       frequencias, silabas_timestamp)


# H
rectas(1.0411, 1.0458,
       1200.0, 1600.0,
       frequencias, silabas_timestamp)
rectas(1.0458, 1.0633,
       2400.0, 2400.0,
       frequencias, silabas_timestamp)
rectas(1.0633, 1.0669,
       2400.0, 1400.0,
       frequencias, silabas_timestamp)
expo(  1.0669, 1.0958,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# D1'
rectas(0.5567 +0.5767, 0.5622 +0.5767,
       900.0, 900.0,
       frequencias, silabas_timestamp)
rectas(0.5622 +0.5767, 0.5648 +0.5767,
       3200.0, 3200.0,
       frequencias, silabas_timestamp)
rectas(0.5648 +0.5767, 0.5720 +0.5767,
       1200.0, 750.0,
       frequencias, silabas_timestamp)
# # D2'
# rectas(0.5872 +0.5767, 0.5916 +0.5767,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.5916 +0.5767, 0.6151 +0.5767,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D3'
# rectas(0.6151 +0.5767, 0.6191 +0.5767,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6191 +0.5767, 0.6390 +0.5767,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D4'
# rectas(0.6390 +0.5767, 0.6429 +0.5767,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6429 +0.5767, 0.6623 +0.5767,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D5'
# rectas(0.6623 +0.5767, 0.6671 +0.5767,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6671 +0.5767, 0.6859 +0.5767,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D6'
# rectas(0.6859 +0.5767, 0.6908 +0.5767,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6908 +0.5767, 0.7095 +0.5767,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D7'
# rectas(0.7095 +0.5767, 0.7163 +0.5767,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.7163 +0.5767, 0.7373 +0.5767,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# D8'
rectas(0.7373 +0.5767, 0.7408 +0.5767,
       3400.0, 3400.0,
       frequencias, silabas_timestamp)
expo(  0.7408 +0.5767, 0.7654 +0.5767,
       3400.0, 450.0,
       frequencias, silabas_timestamp)


# E'
rectas(0.7993 +0.5767, 0.8255 +0.5767,
       470.0, 420.0,
       frequencias, silabas_timestamp)
expo(  0.8255 +0.5767, 0.8410 +0.5767,
       420.0, 250.0,
       frequencias, silabas_timestamp)




# SEGUNDA REPETICIÓN DEL CANTO

# i2
rectas(0.2717 +1.3585, 0.2861 +1.3585,
       3100.0, 3100.0,
       frequencias, silabas_timestamp)
expo(  0.2861 +1.3585, 0.3034 +1.3585,
       3100.0, 750.0,
       frequencias, silabas_timestamp)


# A
rectas(0.3642 +1.3585, 0.3757 +1.3585,
       1200.0, 2400.0,
       frequencias, silabas_timestamp)
expo(  0.3757 +1.3585, 0.3990 +1.3585,
       2400.0, 750.0,
       frequencias, silabas_timestamp)


# B
rectas(0.4071 +1.3585, 0.4345 +1.3585,
       2700.0, 2400.0,
       frequencias, silabas_timestamp)
rectas(0.4345 +1.3585, 0.4571 +1.3585,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# C
rectas(0.4687 +1.3585, 0.4882 +1.3585,
       2700.0, 2400.0,
       frequencias, silabas_timestamp)
rectas(0.4882 +1.3585, 0.5075 +1.3585,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# D1
rectas(0.5567 +1.3585, 0.5622 +1.3585,
       900.0, 900.0,
       frequencias, silabas_timestamp)
rectas(0.5622 +1.3585, 0.5648 +1.3585,
       3200.0, 3200.0,
       frequencias, silabas_timestamp)
rectas(0.5648 +1.3585, 0.5720 +1.3585,
       1200.0, 750.0,
       frequencias, silabas_timestamp)
# # D2
# rectas(0.5872 +1.3585, 0.5916 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.5916 +1.3585, 0.6151 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D3
# rectas(0.6151 +1.3585, 0.6191 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6191 +1.3585, 0.6390 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D4
# rectas(0.6390 +1.3585, 0.6429 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6429 +1.3585, 0.6623 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D5
# rectas(0.6623 +1.3585, 0.6671 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6671 +1.3585, 0.6859 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D6
# rectas(0.6859 +1.3585, 0.6908 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6908 +1.3585, 0.7095 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D7
# rectas(0.7095 +1.3585, 0.7163 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.7163 +1.3585, 0.7373 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# D8
rectas(0.7373 +1.3585, 0.7408 +1.3585,
       3400.0, 3400.0,
       frequencias, silabas_timestamp)
expo(  0.7408 +1.3585, 0.7654 +1.3585,
       3400.0, 450.0,
       frequencias, silabas_timestamp)


# E
rectas(0.7993 +1.3585, 0.8255 +1.3585,
       470.0, 420.0,
       frequencias, silabas_timestamp)
expo(  0.8255 +1.3585, 0.8410 +1.3585,
       420.0, 250.0,
       frequencias, silabas_timestamp)


# F
rectas(0.8895 +1.3585, 0.8931 +1.3585,
       1500.0, 1500.0,
       frequencias, silabas_timestamp)
rectas(0.8985 +1.3585, 0.9160 +1.3585,
       1800.0, 1500.0,
       frequencias, silabas_timestamp)
expo(  0.9160 +1.3585, 0.9300 +1.3585,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# G 
rectas(0.9589 +1.3585, 0.9626 +1.3585,
       1000.0, 1000.0,
       frequencias, silabas_timestamp)
rectas(0.9659 +1.3585, 0.9743 +1.3585,
       2000.0, 2000.0,
       frequencias, silabas_timestamp)
rectas(0.9784 +1.3585, 0.9987 +1.3585,
       1750.0, 1500.0,
       frequencias, silabas_timestamp)
rectas(0.9987 +1.3585, 1.0054 +1.3585,
       1500.0, 1400.0,
       frequencias, silabas_timestamp)
rectas(1.0054 +1.3585, 1.0160 +1.3585,
       1400.0, 1400.0,
       frequencias, silabas_timestamp)


# H
rectas(1.0411 +1.3585, 1.0458 +1.3585,
       1200.0, 1600.0,
       frequencias, silabas_timestamp)
rectas(1.0458 +1.3585, 1.0633 +1.3585,
       2400.0, 2400.0,
       frequencias, silabas_timestamp)
rectas(1.0633 +1.3585, 1.0669 +1.3585,
       2400.0, 1400.0,
       frequencias, silabas_timestamp)
expo(  1.0669 +1.3585, 1.0958 +1.3585,
       1500.0, 750.0,
       frequencias, silabas_timestamp)


# D1'
rectas(0.5567 +0.5767 +1.3585, 0.5622 +0.5767 +1.3585,
       900.0, 900.0,
       frequencias, silabas_timestamp)
rectas(0.5622 +0.5767 +1.3585, 0.5648 +0.5767 +1.3585,
       3200.0, 3200.0,
       frequencias, silabas_timestamp)
rectas(0.5648 +0.5767 +1.3585, 0.5720 +0.5767 +1.3585,
       1200.0, 750.0,
       frequencias, silabas_timestamp)
# # D2'
# rectas(0.5872 +0.5767 +1.3585, 0.5916 +0.5767 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.5916 +0.5767 +1.3585, 0.6151 +0.5767 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D3'
# rectas(0.6151 +0.5767 +1.3585, 0.6191 +0.5767 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6191 +0.5767 +1.3585, 0.6390 +0.5767 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D4'
# rectas(0.6390 +0.5767 +1.3585, 0.6429 +0.5767 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6429 +0.5767 +1.3585, 0.6623 +0.5767 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D5'
# rectas(0.6623 +0.5767 +1.3585, 0.6671 +0.5767 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6671 +0.5767 +1.3585, 0.6859 +0.5767 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D6'
# rectas(0.6859 +0.5767 +1.3585, 0.6908 +0.5767 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.6908 +0.5767 +1.3585, 0.7095 +0.5767 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# # D7'
# rectas(0.7095 +0.5767 +1.3585, 0.7163 +0.5767 +1.3585,
#        4800.0, 4800.0,
#        frequencias, silabas_timestamp)
# expo(  0.7163 +0.5767 +1.3585, 0.7373 +0.5767 +1.3585,
#        4800.0, 450.0,
#        frequencias, silabas_timestamp)
# D8'
rectas(0.7373 +0.5767 +1.3585, 0.7408 +0.5767 +1.3585,
       3400.0, 3400.0,
       frequencias, silabas_timestamp)
expo(  0.7408 +0.5767 +1.3585, 0.7654 +0.5767 +1.3585,
       3400.0, 450.0,
       frequencias, silabas_timestamp)


# E'
rectas(0.7993 +0.5767 +1.3585, 0.8255 +0.5767 +1.3585,
       470.0, 420.0,
       frequencias, silabas_timestamp)
expo(  0.8255 +0.5767 +1.3585, 0.8410 +0.5767 +1.3585,
       420.0, 250.0,
       frequencias, silabas_timestamp)