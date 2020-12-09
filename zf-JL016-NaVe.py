#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'AB010-bi'
nombre_BOS = 'zfAB010-bi_BOS03_44100.wav'

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

# D2
rectas(0.5567, 0.5622,
       900.0, 900.0,
       frequencias, silabas_timestamp)
rectas(0.5622, 0.5648,
       3200.0, 3200.0,
       frequencias, silabas_timestamp)
rectas(0.5648, 0.5720,
       1200.0, 750.0,
       frequencias, silabas_timestamp)

# D3
rectas(0.5872, 0.5916,
       4800.0, 4800.0,
       frequencias, silabas_timestamp)
expo(  0.5916, 0.6151,
       4800.0, 450.0,
       frequencias, silabas_timestamp)

# D4
rectas(0.6151, 0.6191,
       4800.0, 4800.0,
       frequencias, silabas_timestamp)
expo(  0.6191, 0.6390,
       4800.0, 450.0,
       frequencias, silabas_timestamp)

# D5
rectas(0.6390, 0.6429,
       4800.0, 4800.0,
       frequencias, silabas_timestamp)
expo(  0.6429, 0.6623,
       4800.0, 450.0,
       frequencias, silabas_timestamp)

# D6
rectas(0.6623, 0.6671,
       4800.0, 4800.0,
       frequencias, silabas_timestamp)
expo(  0.6671, 0.6859,
       4800.0, 450.0,
       frequencias, silabas_timestamp)

# D7
rectas(0.6859, 0.7098,
       4800.0, 4800.0,
       frequencias, silabas_timestamp)
expo(  0.7098, 0.7373,
       4800.0, 450.0,
       frequencias, silabas_timestamp)

# D8
rectas(0.7373, 0.7408,
       3400.0, 3400.0,
       frequencias, silabas_timestamp)
expo(  0.7408, 0.7654,
       3400.0, 450.0,
       frequencias, silabas_timestamp)

# E
rectas(0.7993, 0.8255,
       930.0, 860.0,
       frequencias, silabas_timestamp)
expo(  0.8255, 0.8410,
       860.0, 500.0,
       frequencias, silabas_timestamp)

# F
rectas(0.8895, 0.8931,
       1500, 1500.0,
       frequencias, silabas_timestamp)
rectas(0.8985, 0.9160,
       1800, 1500.0,
       frequencias, silabas_timestamp)
expo(  0.9160, 0.9300,
       1500.0, 750.0,
       frequencias, silabas_timestamp)