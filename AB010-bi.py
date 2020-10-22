"""
Created on Tue Jul 21 10:28:48 2020

@author: javi_lassaortiz
"""

nombre_ave = 'AB010-bi'
# nombre_BOS = '/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/zfAB010-bi_BOS03_44100.wav'
nombre_BOS = 'zfAB010-bi_BOS03_44100.wav'

# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales y silabas_timestamp
    
# expo(ti,tf,
# wi,wf,
# factor,frequencias, silabas_timestamp)

# rectas(ti,tf,
# wi,wf,factor,
# frequencias, silabas_timestamp)

# senito(ti,tf,
# media,amplitud,
# alphai,alphaf,
# factor,frequencias, silabas_timestamp)

# Notas intro

# i1
expo(0.021233, 0.070797,
     869.3, 430.0,
     0.2278,
     frequencias, silabas_timestamp)

#i2
expo(0.163317, 0.205335,
     825.5, 453.0,
     0.2731, 
     frequencias, silabas_timestamp)

# i3
rectas(0.25319, 0.269447,
       830.0, 830.0,
       0.07104, 
       frequencias, silabas_timestamp)
expo(0.269447, 0.313879,
     830.0, 430.0,
     0.3325, 
     frequencias, silabas_timestamp)

# i4
rectas(0.366935, 0.378824,
       850.0, 850.0,
       0.0874, 
       frequencias, silabas_timestamp)
expo(0.383282, 0.424622,
     850, 430.0,
     0.346,
     frequencias, silabas_timestamp)

# i5
rectas(0.467733, 0.483101,
       843.0, 843.0,
       0.08789,
       frequencias, silabas_timestamp)
expo(0.483101,0.526642,
     843.0,450.0,
     0.3283,
     frequencias, silabas_timestamp)


# A
rectas(0.59097,0.606553,
       550.0 ,550.0 ,
       0.3109,
       frequencias, silabas_timestamp)

rectas(0.606553,0.629293,
       550.0, 400.0,
       0.2937,
       frequencias, silabas_timestamp)


# B
senito(0.661079,0.692761,
       2500.0,900.0,
       3*np.pi/2, 19*np.pi/2,
       0.5227/2,
       frequencias, silabas_timestamp)

rectas(0.692761,0.699490,
       2000.0,2000.0,
       0.4112,
       frequencias, silabas_timestamp) 

expo(0.699490,0.724839,
     750.0,430.0,
     0.2258,
     frequencias, silabas_timestamp)


# C
rectas(0.781955,0.792721,
       700.0, 1500.0,
       0.08829,
       frequencias, silabas_timestamp) 

rectas(0.795595,0.803877,
       1600.0,1600.0,
       0.5502,
       frequencias, silabas_timestamp)

rectas(0.803877,0.822859,
       1600.0,1600.0,
       0.8584,
       frequencias, silabas_timestamp)

rectas(0.822859,0.825773,
       1600.0,1150.0,
       0.8642,
       frequencias, silabas_timestamp)

expo(0.825773, 0.929312,
     1150.0, 450.0,
     0.7624,
     frequencias, silabas_timestamp)


# D
rectas(0.956319,0.969585,
       475.0, 850.0,
       0.4216,
       frequencias, silabas_timestamp)

rectas(0.969585,1.000902,
       850.0, 850.0,
       0.4389,
       frequencias, silabas_timestamp)

# E
rectas(1.035681,1.108332,
       576.0, 576.0,
       0.9502,
       frequencias, silabas_timestamp)

# F
rectas(1.134231,1.158998,
       550.0,550.0,
       0.4627,
       frequencias, silabas_timestamp)

rectas(1.158998, 1.175064,
       550.0, 430.0,
       0.3988,
       frequencias, silabas_timestamp)


# G
rectas(1.2136,1.220276,
       800.0,1450.0,
       0.2095,
       frequencias, silabas_timestamp)

senito(1.220276, 1.249285,
       2500.0, 900.0,
       np.pi/2, 10*np.pi,
       0.3627/2,
       frequencias, silabas_timestamp)

rectas(1.249285, 1.255925,
       1800.0, 1600.0,
       0.2162,
       frequencias, silabas_timestamp)

rectas(1.255925, 1.259131,
       1600.0, 1500.0,
       0.03391,
       frequencias, silabas_timestamp)

expo(1.259591,1.284083,
     700.0 ,450.0,
     0.1756,
     frequencias, silabas_timestamp)


# H
rectas(1.341623, 1.352737,
       800.0, 1500.0,
       0.07736,
       frequencias, silabas_timestamp)

rectas(1.355512, 1.363994,
       1560.0, 1560.0,
       0.5309,
       frequencias, silabas_timestamp)

rectas(1.363994, 1.3832,
       1560.0, 1560.0,
       1.0,
       frequencias, silabas_timestamp)

expo(1.3832, 1.489505,
     1560.0, 450.0,
     0.97, 
     frequencias, silabas_timestamp)


# I
rectas(1.520093, 1.533520,
       500.0, 850.0,
       0.3243,
       frequencias, silabas_timestamp)

rectas(1.533520,1.566696,
       850,850,
       0.4615,
       frequencias, silabas_timestamp)


# J
rectas(1.599750, 1.670138,
       565.0, 565.0,
       0.7212,
       frequencias, silabas_timestamp)


# K
rectas(1.698986,1.725609,
       540.0,540.0,
       0.4762,
       frequencias, silabas_timestamp)

expo(1.725609, 1.739792,
       540.0,400.0,
       0.3274,
       frequencias, silabas_timestamp)


# L
rectas(1.778981,1.785611,
       750.0,1450.0,
       0.1903,
       frequencias, silabas_timestamp)

senito(1.785611, 1.815664,
       2300,900,np.pi/2, 10*np.pi,
       0.282/2,
       frequencias, silabas_timestamp)

rectas(1.815664, 1.821483,
       2000.0, 1500.0,
       0.1869,
       frequencias, silabas_timestamp)

rectas(1.821483, 1.824357,
       1500.0, 1500.0,
       0.03351,
       frequencias, silabas_timestamp)

expo(1.824357,1.850393,
     700.0 ,450.0,
     0.1653,
     frequencias, silabas_timestamp)


# M (versión mas sencilla de esta sílaba)
rectas(1.931650,1.948097,
       1550.0,1550.0,
       0.944,
       frequencias, silabas_timestamp)

expo(1.948099,2.06,
     1550.0,431.0,
     0.7555,
     frequencias, silabas_timestamp)
