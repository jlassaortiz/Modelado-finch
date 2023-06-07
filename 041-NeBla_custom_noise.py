#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL041-NeBla'
nombre_BOS = 'zf-JL041-NeBla_BOS.wav'

# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales

# expo(ti,tf,
# wi,wf,
# frequencias, silabas_timestamp, # no se completa
# ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa


# rectas(ti,tf,
# wi,wf,
# frequencias, silabas_timestamp, # no se completa
# ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa


# senito(ti,tf,
# media,amplitud,
# alphai,alphaf,
# frequencias, silabas_timestamp, # no se completa
# ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa



# i1
rectas(0.1588,0.1784,
1200,500,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa

rectas(0.1784,0.2336,
500,300,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa


# i2
rectas(0.2949,0.3028,
1700,900,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa

rectas(0.3028,0.3201,
900,600,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa

rectas(0.3201,0.3847,
600,300,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa


# i3
rectas(0.2949 + 0.1198 ,0.3028 + 0.1198,
1700,900,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa

rectas(0.3028 + 0.1198, 0.3201 + 0.1198,
900,600,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa

rectas(0.3201 + 0.1198,0.3847 + 0.1198,
600,300,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa


# i4
rectas(0.2949 + 0.2497 ,0.3028 + 0.2497 ,
1700,900,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa

rectas(0.3028 + 0.2497 , 0.3201 + 0.2497 ,
900,600,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,  0.3) # no se completa

rectas(0.3201 + 0.2497 ,0.3847 + 0.2497 ,
600,300,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,   0.3) # no se completa


# i5
rectas(0.2949 + 0.3726 ,0.3028 + 0.3726 ,
1700,900,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,  0.3) # no se completa

rectas(0.3028 + 0.3726 , 0.3201 + 0.3726 ,
900,600,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,  0.3) # no se completa

rectas(0.3201 + 0.3726 ,0.3847 + 0.3726 ,
600,300,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,  0.3) # no se completa


# i6
rectas(0.2949 + 0.4954 ,0.3028 + 0.4954 ,
1700,900,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,  0.3) # no se completa

rectas(0.3028 + 0.4954 , 0.3201 + 0.4954 ,
900,600,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,  0.3) # no se completa

rectas(0.3201 + 0.4954 ,0.3847 + 0.4954 ,
600,300,
frequencias, silabas_timestamp, # no se completa
ruido_beta_list, ruido_beta,  0.3) # no se completa


t_dif = 0
dif_t = np.round(1.8603 - 0.9199, 4)

for i in range(4):
    
    # A
    rectas(0.9192 + t_dif ,0.9245 + t_dif ,
    1100,1150,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, 0.9, ruido_alfa) # no se completa
    
    rectas(0.9245  + t_dif, 0.9366 + t_dif,
    1150,1250,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(0.9366  + t_dif,0.9594 + t_dif,
    1250,1300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(0.9594 + t_dif ,0.9707 + t_dif,
    1300,1275,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(0.9707 + t_dif ,0.9805 + t_dif,
    1275,1200,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(0.9805 + t_dif ,0.9956 + t_dif,
    1200,1000,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    expo(0.9956 + t_dif ,1.0735 + t_dif,
    1000,600,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(1.0735 + t_dif ,1.0840 + t_dif,
    600,500,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    
    
    # B
    rectas(1.1344+ t_dif ,1.1410+ t_dif,
    700,950,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    expo(1.1410+ t_dif ,1.1794+ t_dif,
    950,400,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(1.1794+ t_dif ,1.1865 + t_dif,
    400,350,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    
    
    # C
    rectas(1.2190 + t_dif ,1.2218 + t_dif,
    4600,4600,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(1.2218 + t_dif ,1.2243 + t_dif,
    4600,3000,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(1.2243 + t_dif ,1.2271 + t_dif,
    3000,3000,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    expo(1.2271 + t_dif ,1.2406 + t_dif,
    3000,700,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  0.5) # no se completa
    
    rectas(1.2406 + t_dif ,1.2474 + t_dif,
    700,700,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  0.5) # no se completa
    
    rectas(1.2474 + t_dif ,1.2524 + t_dif,
    700,1600,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  0.5) # no se completa
    
    rectas(1.2524 + t_dif ,1.2552 + t_dif,
    2500,2500,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    expo(1.2552 + t_dif ,1.2913 + t_dif,
    2400,700,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  0.5) # no se completa
    
    
    
    # D
    rectas(1.3181 + t_dif, 1.3276 + t_dif,
    1100, 1100,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, 0.3) # opcional completar
    
    rectas(1.3276 + t_dif, 1.3381 + t_dif,
    2300, 2300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, 0.4, 0.1) # opcional completar
    
    rectas(1.3381 + t_dif, 1.3425 + t_dif,
    2300, 2300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    senito(1.3425 + t_dif, 1.3520 + t_dif,
    6000,500,
    0,3*np.pi,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, 0.5,  0.5) # no se completa
    
    senito(1.3520 + t_dif, 1.3643 + t_dif,
    6000,500,
    0,3*np.pi,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    senito(1.3643 + t_dif, 1.3780 + t_dif,
    5600,600,
    -0.8*np.pi , 0.8*np.pi,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(1.3808 + t_dif, 1.3852 + t_dif,
    3300, 3300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, 0.3, ruido_alfa) # opcional completar
    
    rectas(1.3863 + t_dif, 1.3884 + t_dif,
    3300, 3300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    
    # E
    senito(1.4003 + t_dif, 1.4058 + t_dif,
    2000,500,
    -0.8*np.pi , -0.2*np.pi,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  0.4) # no se completa
    
    rectas(1.4058 + t_dif, 1.4103 + t_dif,
    6000, 6000,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, 0.4) # opcional completar
    
    rectas(1.4103 + t_dif, 1.4129 + t_dif,
    6000, 6500,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, 0.4) # opcional completar
    
    rectas(1.4129 + t_dif, 1.4177 + t_dif,
    6500, 6500,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, 0.4) # opcional completar
    
    rectas(1.4177 + t_dif, 1.4232 + t_dif,
    2400, 2400,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    rectas(1.4232 + t_dif, 1.4270 + t_dif,
    4000, 3800,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, 0.4) # opcional completar
    
    expo(1.4270 + t_dif ,1.4383 + t_dif,
    3800,2300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  0.3) # no se completa
    
    rectas(1.4419 + t_dif, 1.4496 + t_dif,
    4200, 4200,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    rectas(1.4496 + t_dif, 1.4618 + t_dif,
    4300, 4300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, 0.4, 0.4) # opcional completar
    
    rectas(1.4618 + t_dif, 1.4697 + t_dif,
    4300, 4300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, 0.2) # opcional completar
    
    rectas(1.4697 + t_dif, 1.4734 + t_dif,
    4300, 5900,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    rectas(1.4734 + t_dif, 1.4778 + t_dif,
    5900, 5600,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    expo(1.4778 + t_dif ,1.4854 + t_dif,
    5600,700,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    rectas(1.4854 + t_dif ,1.5101 + t_dif,
    700,500,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    expo(1.5101 + t_dif ,1.5497 + t_dif,
    500,300,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
    
    
    # F 
    rectas(1.5909 + t_dif, 1.6003 + t_dif, 
    2300, 2200,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    rectas(1.6003 + t_dif, 1.6185 + t_dif,
    2200, 2200,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, 0.2) # opcional completar
    
    rectas(1.6185 + t_dif, 1.6382 + t_dif,
    2200, 1400,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, 0.2, 0.3) # opcional completar
    
    rectas(1.6382 + t_dif, 1.7012 + t_dif,
    1400, 650,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, 0.2, 0.3) # opcional completar
    
    
    # G
    rectas(1.7107 + t_dif, 1.7207 + t_dif,
    500, 600,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    rectas(1.7207 + t_dif, 1.7743 + t_dif,
    600, 600,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    rectas(1.7743 + t_dif, 1.7914 + t_dif,
    600, 550,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    rectas(1.7914 + t_dif, 1.8035 + t_dif,
    550, 500,
    frequencias, silabas_timestamp, # no se completa
    ruido_beta_list, ruido_beta, ruido_alfa) # opcional completar
    
    t_dif = t_dif + dif_t