#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL044-AmA'
nombre_BOS = 'zf-JL044-AmA_BOS_44100_70dB_band.wav'

# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales

# expo(ti,tf,
# wi,wf,
# frequencias, silabas_timestamp) # no se completa

# rectas(ti,tf,
# wi,wf,
# frequencias, silabas_timestamp) # no se completa

# senito(ti,tf,
# media,amplitud,
# alphai,alphaf,
# frequencias, silabas_timestamp) # no se completa


# i1
rectas(0.0807,0.0878,
900,900,
frequencias,
silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.0878,0.0944,
400,460,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.0944, 0.1010,
460, 460,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.1010, 0.1090,
460, 570,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.1090, 0.1234, 
570, 700,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.1234, 0.1403,
700,700 ,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

expo(0.1403, 0.1610,
700,600 ,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa


# i2
rectas(0.2319, 0.2367,
600, 600,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

expo(0.2367, 0.2452,
600, 1030,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

expo(0.2452, 0.2951,
1030, 400,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa


# i3
rectas(0.4115, 0.4155,
550, 550,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa


rectas(0.4155, 0.4304,
550, 760,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.4304, 0.4505,
760, 720,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa
 
rectas(0.4505, 0.4579,
720, 680,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.4579, 0.4678,
680, 570,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa



######################## Comienzo motivo (fin intro) ##########################

################################### A
expo(0.4897, 0.4972,
680, 780,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.4972, 0.5080,
800, 800,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta, ruido_alfa) # no se completa

rectas(0.5080, 0.5178,
1200,1200,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3, 0.7) # no se completa

rectas(0.5178, 0.5356,
2700, 2700,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3, 0.7) # no se completa

expo(0.5356, 0.5648,
2700, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2, 0.6) # no se completa

expo(0.5648, 0.6020,
1200, 850,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.6020, 0.6264,
850, 550,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa


################################### B
senito(0.6751, 0.6983,
3800,1000,
np.pi/2 ,np.pi*17/2,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa) # no se completa

rectas(0.6983, 0.7165,
4800, 4800, 
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7165, 0.7218,
1100, 1400,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.3)

rectas(0.7218, 0.7288,
1400, 1300,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.3)

rectas(0.7288, 0.7371,
1300, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.3)

rectas(0.7371, 0.7413,
1200, 1400, 
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.4)

rectas(0.7413, 0.7517,
1400, 1000,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.4)

rectas(0.7517, 0.7665,
1000, 900, 
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.4)

rectas(0.7665, 0.7700,
900, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.4)

rectas(0.7700, 0.7980,
1200, 700,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.4)


################################### C1
expo(0.8167, 0.8248,
700, 1400,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.5)

expo(0.8248, 0.8302,
1400, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.5)

rectas(0.8302, 0.8394,
1300, 1300,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.5)

rectas(0.8394, 0.8576,
1300, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.8576, 0.8684,
1200, 1100,
frequencias, silabas_timestamp,
ruido_beta_list, 0.1,  0.2)

rectas(0.8684, 0.8939,
1100, 900,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.5)



################################### D1
rectas(0.9397, 0.9563,
900, 1400,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9563, 0.9643,
3800, 4100,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9643, 0.9805,
4100, 4100,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9805, 0.9886,
4100, 3600,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)



rectas(0.9884, 0.9928,
1800, 2100,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.2)

rectas(0.9928, 1.0008,
2100, 2100,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.2)

rectas(1.0008, 1.0051,
2100, 1900,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.2)

expo(1.0051, 1.0225,
1900, 1400,
frequencias, silabas_timestamp,
ruido_beta_list, 0.2,  0.2)

expo(1.0225, 1.0861,
1400, 700,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)




rectas(1.0861, 1.0957,
700, 600,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.0957, 1.1158,
600,500,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)






##############################   Transición   #################################

rectas(1.1581, 1.1629,
700, 800,
frequencias,silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.1629, 1.1699,
800, 800,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.1699, 1.1758,
800, 700,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.1758, 1.1802,
1200, 1200, 
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

expo(1.1802, 1.2280,
1200, 400,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)



################################### B'

senito(1.2663, 1.3026,
3800, 1200, 
np.pi/2, np.pi* 21/2,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.3026, 1.3240,
4600, 4600,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7165 + 0.6075, 0.7218 + 0.6075,
1100, 1400,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7218 + 0.6075, 0.7288 + 0.6075,
1400, 1300,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7288 + 0.6075, 0.7371 + 0.6075,
1300, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7371 + 0.6075, 0.7413 + 0.6075,
1200, 1400, 
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7413 + 0.6075, 0.7517 + 0.6075,
1400, 1000,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7517 + 0.6075, 0.7665 + 0.6075,
1000, 900, 
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7665 + 0.6075, 0.7700 + 0.6075,
900, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.7700 + 0.6075, 0.7980 + 0.6075,
1200, 700,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)




################################### C2
expo(0.8167 + 0.6075, 0.8248 + 0.6075,
700, 1400,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.6)

expo(0.8248 + 0.6075, 0.8302 + 0.6075,
1400, 1200,
frequencias, silabas_timestamp,
ruido_beta_list, 0.3,  0.6)

rectas(0.8302 + 0.6075, 0.8939 + 0.6075,
1300, 1000,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)


################################### D2
rectas(0.9397 + 0.6075, 0.9563 + 0.6075,
900, 1400,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9563 + 0.6075, 0.9643 + 0.6075,
3800, 4100,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9643 + 0.6075, 0.9805 + 0.6075,
4100, 4100,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9805 + 0.6075, 0.9886 + 0.6075,
4100, 3600,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9884 + 0.6075, 0.9928 + 0.6075,
1800, 2100,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(0.9928 + 0.6075, 1.0008 + 0.6075,
2100, 2100,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.0008 + 0.6075, 1.0051 + 0.6075,
2100, 1900,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

expo(1.0051 + 0.6075, 1.0861 + 0.6075,
1900, 700,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.0861 + 0.6075, 1.0957 + 0.6075,
700, 600,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)

rectas(1.0957 + 0.6075, 1.1158 + 0.6075,
600,500,
frequencias, silabas_timestamp,
ruido_beta_list, ruido_beta,  ruido_alfa)









































