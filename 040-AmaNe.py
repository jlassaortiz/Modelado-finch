#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:15:45 2020

@author: javi_lassaortiz
"""
nombre_ave = 'zf-JL040-AmaNe'
nombre_BOS = 'zf-JL040-AmaNe_BOS_44100Hz_band.wav'

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


 
# i1
expo(0.0686, 0.0736,
850,1350,
frequencias, 
silabas_timestamp)

expo(0.0736, 0.1424,
1350,350,
frequencias, 
silabas_timestamp)



# i2
expo(0.2142, 0.2233,
850,1300,
frequencias, 
silabas_timestamp)

expo(0.2233, 0.2900,
1300,375,
frequencias, 
silabas_timestamp)



# i3
rectas(0.3410, 0.3490,
900, 1200,
frequencias, 
silabas_timestamp)

expo(0.3490, 0.4061,
1300,420,
frequencias, 
silabas_timestamp)



# call-1
rectas(0.5077,0.5331,
650,750,
frequencias,
silabas_timestamp)

rectas(0.5331,0.5456,
750,900,
frequencias,
silabas_timestamp)

rectas(0.5456,0.5745,
900,1200,
frequencias,
silabas_timestamp)

rectas(0.5745,0.6022,
1200,900,
frequencias,
silabas_timestamp)

rectas(0.6022,0.6833,
900,475,
frequencias,
silabas_timestamp)



# call-2
rectas(0.5077 + 0.2087, 0.533 + 0.20871,
650,750,
frequencias,
silabas_timestamp)

rectas(0.5331 + 0.2087, 0.5456 + 0.2087,
750,900,
frequencias,
silabas_timestamp)

rectas(0.5456 + 0.2087, 0.5745 + 0.2087,
900,1200,
frequencias,
silabas_timestamp)

rectas(0.5745 + 0.2087, 0.6022 + 0.2087,
1200,900,
frequencias,
silabas_timestamp)

rectas(0.6022 + 0.2087, 0.6833 + 0.2087,
900,475,
frequencias,
silabas_timestamp)



# i1-2
expo(0.0686 + 1.0055, 0.0736 + 1.0055,
850,1350,
frequencias, 
silabas_timestamp)

expo(0.0736 + 1.0055, 0.1424 + 1.0055,
1350,350,
frequencias, 
silabas_timestamp)



# i2-2
expo(0.2142 + 1.0055, 0.2233 + 1.0055,
850,1300,
frequencias, 
silabas_timestamp)

expo(0.2233 + 1.0055, 0.2900 + 1.0055,
1300,375,
frequencias, 
silabas_timestamp)



# i3-2
expo(0.3410 + 1.0055, 0.3490 + 1.0055,
900, 1200,
frequencias, 
silabas_timestamp)

expo(0.3490 + 1.0055, 0.4061 + 1.0055,
1300,420,
frequencias, 
silabas_timestamp)

######################## Comienzo motivo (fin intro) ##########################

################################### A-1
rectas(1.4508,1.4567,
5000,3000,
frequencias,
silabas_timestamp)

rectas(1.4567,1.4636,
3000,2000,
frequencias,
silabas_timestamp)

rectas(1.4636,1.4747,
2000,700,
frequencias,
silabas_timestamp)

expo(1.4747,1.4859,
700,2000,
frequencias, 
silabas_timestamp)

rectas(1.4859,1.4906,
5500,5500,
frequencias, 
silabas_timestamp)

rectas(1.4906,1.4939,
6000,6000,
frequencias, 
silabas_timestamp)

rectas(1.4939,1.5033,
4700,4700,
frequencias, 
silabas_timestamp)

rectas(1.5033,1.5073,
6200,6200,
frequencias, 
silabas_timestamp)

rectas(1.5098,1.5149,
4000,4000,
frequencias, 
silabas_timestamp)

#################################### B-1
expo(1.5608,1.5686,
1200,2200,
frequencias,
silabas_timestamp)

rectas(1.5686,1.5833,
2200,2200,
frequencias,
silabas_timestamp)

rectas(1.5833,1.5886,
4500,4000,
frequencias,
silabas_timestamp)

expo(1.5886,1.5899,
4000,2300,
frequencias,
silabas_timestamp)

rectas(1.5899,1.6002,
2300,2300,
frequencias,
silabas_timestamp)

rectas(1.6025,1.6334,
4500,4500,
frequencias,
silabas_timestamp)

rectas(1.6334,1.6368,
1400,1400,
frequencias,
silabas_timestamp)

rectas(1.6368,1.6585,
680,680,
frequencias,
silabas_timestamp)

rectas(1.6585,1.6651,
680,600,
frequencias,
silabas_timestamp)

rectas(1.6651,1.7063,
600,350,
frequencias,
silabas_timestamp)


################################ C (HS)- 1
rectas(1.7093,1.7220,
460,600,
frequencias,
silabas_timestamp)

rectas(1.7220,1.7768,
600,600,
frequencias,
silabas_timestamp)

rectas(1.7768,1.7937,
600,450,
frequencias,
silabas_timestamp)


################################ D (montañita) - 1
rectas(1.8386  ,1.8616 , 
950,1200,
frequencias,
silabas_timestamp)

rectas(1.8616  ,1.8772 ,
1200,1200,
frequencias,
silabas_timestamp)

rectas(1.8772  ,1.8959 ,
1200,1150,
frequencias,
silabas_timestamp)

rectas(1.8959 ,1.9458,
1150,680,
frequencias,
silabas_timestamp)

rectas(1.9458 ,1.9847 ,
680,580,
frequencias,
silabas_timestamp)

rectas(1.9847 ,2.0038 ,
580,460,
frequencias,
silabas_timestamp)


################################################ E & E'- 1

# E
expo(2.0556,2.0940,
800,420,
frequencias,
silabas_timestamp)

# E'
expo(2.1322,2.1514,
1300,650,
frequencias,
silabas_timestamp)

expo(2.1514,2.1971,
650,400,
frequencias,
silabas_timestamp)


####################################################### A-2
rectas(1.4508 + 0.7829,1.4567 + 0.7829,
5000,3000,
frequencias,
silabas_timestamp)

rectas(1.4567 + 0.7829,1.4636 + 0.7829,
3000,2000,
frequencias,
silabas_timestamp)

rectas(1.4636 + 0.7829,1.4747 + 0.7829,
2000,700,
frequencias,
silabas_timestamp)

expo(1.4747 + 0.7829,1.4859 + 0.7829,
700,2000,
frequencias, 
silabas_timestamp)

rectas(1.4859 + 0.7829,1.4906 + 0.7829,
5500,5500,
frequencias, 
silabas_timestamp)

rectas(1.4906 + 0.7829,1.4939 + 0.7829,
6000,6000,
frequencias, 
silabas_timestamp)

rectas(1.4939 + 0.7829,1.5033 + 0.7829,
4700,4700,
frequencias, 
silabas_timestamp)

rectas(1.5033 + 0.7829,1.5073 + 0.7829,
6200,6200,
frequencias, 
silabas_timestamp)

rectas(1.5098 + 0.7829,1.5149 + 0.7829,
4000,4000,
frequencias, 
silabas_timestamp)



####################################################### B-2
expo(1.5608 + 0.7832,1.5686 + 0.7832,
1200,2200,
frequencias,
silabas_timestamp)

rectas(1.5686 + 0.7832,1.5833 + 0.7832,
2200,2200,
frequencias,
silabas_timestamp)

rectas(1.5833 + 0.7832,1.5886 + 0.7832,
4500,4000,
frequencias,
silabas_timestamp)

expo(1.5886 + 0.7832,1.5899 + 0.7832,
4000,2300,
frequencias,
silabas_timestamp)

rectas(1.5899 + 0.7832,1.6002 + 0.7832,
2300,2300,
frequencias,
silabas_timestamp)

rectas(1.6025 + 0.7832,1.6334 + 0.7832,
4500,4500,
frequencias,
silabas_timestamp)

rectas(1.6334 + 0.7832,1.6368 + 0.7832,
1400,1400,
frequencias,
silabas_timestamp)

rectas(1.6368 + 0.7832,1.6651 + 0.7832,
680,680,
frequencias,
silabas_timestamp)

rectas(1.6651 + 0.7832,1.7063 + 0.7832,
680,350,
frequencias,
silabas_timestamp)



################################################# C (HS)- 2
rectas(1.7093 + 0.7836,1.7220 + 0.7836,
460,600,
frequencias,
silabas_timestamp)

rectas(1.7220 + 0.7836,1.7768 + 0.7836,
600,600,
frequencias,
silabas_timestamp)

rectas(1.7768 + 0.7836,1.7937 + 0.7836,
600,450,
frequencias,
silabas_timestamp)


########################################### D (montañita) - 2
rectas(1.8386 + 0.7825  ,1.8616 + 0.7825 , 
950,1200,
frequencias,
silabas_timestamp)

rectas(1.8616 + 0.7825 ,1.8772 + 0.7825,
1200,1200,
frequencias,
silabas_timestamp)

rectas(1.8772 + 0.7825 ,1.8959 + 0.7825,
1200,1150,
frequencias,
silabas_timestamp)

rectas(1.8959 + 0.7825 ,1.9458 + 0.7825,
1150,680,
frequencias,
silabas_timestamp)

rectas(1.9458 + 0.7825 ,1.9847 + 0.7825 ,
680,580,
frequencias,
silabas_timestamp)

rectas(1.9847 + 0.7825 ,2.0038 + 0.7825 ,
580,460,
frequencias,
silabas_timestamp)



############################################### E''
rectas(2.9089, 2.9176,
1200, 1200,
frequencias, 
silabas_timestamp)

expo(2.9176, 2.9744,
1200, 350,
frequencias,
silabas_timestamp)




################################### A-3
rectas(1.4508 + 1.5638 ,1.4567 + 1.5638 ,
5000,3000,
frequencias,
silabas_timestamp)

rectas(1.4567 + 1.5638 ,1.4636 + 1.5638 ,
3000,2000,
frequencias,
silabas_timestamp)

rectas(1.4636 + 1.5638 ,1.4747 + 1.5638 ,
2000,700,
frequencias,
silabas_timestamp)

expo(1.4747 + 1.5638 ,1.4859 + 1.5638 ,
700,2000,
frequencias, 
silabas_timestamp)

rectas(1.4859 + 1.5638 ,1.4906 + 1.5638 ,
5500,5500,
frequencias, 
silabas_timestamp)

rectas(1.4906 + 1.5638 ,1.4939 + 1.5638 ,
6000,6000,
frequencias, 
silabas_timestamp)

rectas(1.4939 + 1.5638 ,1.5033 + 1.5638 ,
4700,4700,
frequencias, 
silabas_timestamp)

rectas(1.5033 + 1.5638 ,1.5073 + 1.5638 ,
6200,6200,
frequencias, 
silabas_timestamp)

rectas(1.5098 + 1.5638, 1.5149 + 1.5638 ,
4000,4000,
frequencias, 
silabas_timestamp)

#################################### B-3
expo(1.5608 + 1.5638 ,1.5686 + 1.5638 ,
1200,2200,
frequencias,
silabas_timestamp)

rectas(1.5686 + 1.5638 ,1.5833 + 1.5638 ,
2200,2200,
frequencias,
silabas_timestamp)

rectas(1.5833 + 1.5638 ,1.5886 + 1.5638 ,
4500,4000,
frequencias,
silabas_timestamp)

expo(1.5886 + 1.5638 ,1.5899 + 1.5638 ,
4000,2300,
frequencias,
silabas_timestamp)

rectas(1.5899 + 1.5638 ,1.6002 + 1.5638 ,
2300,2300,
frequencias,
silabas_timestamp)

rectas(1.6025 + 1.5638 ,1.6334 + 1.5638 ,
4500,4500,
frequencias,
silabas_timestamp)

rectas(1.6334 + 1.5638 ,1.6368 + 1.5638 ,
1400,1400,
frequencias,
silabas_timestamp)

rectas(1.6368 + 1.5638 ,1.6651 + 1.5638 ,
680,680,
frequencias,
silabas_timestamp)

rectas(1.6651 + 1.5638 ,1.7063 + 1.5638 ,
680,350,
frequencias,
silabas_timestamp)


################################ C (HS)- 3
rectas(1.7093 + 1.5638 ,1.7220 + 1.5638 ,
460,600,
frequencias,
silabas_timestamp)

rectas(1.7220 + 1.5638 ,1.7768 + 1.5638 ,
600,600,
frequencias,
silabas_timestamp)

rectas(1.7768 + 1.5638 ,1.7937 + 1.5638 ,
600,450,
frequencias,
silabas_timestamp)


################################ D (montañita) - 3
rectas(1.8386 + 1.5638 ,1.8616 + 1.5638, 
950,1200,
frequencias,
silabas_timestamp)

rectas(1.8616  + 1.5638,1.8772 + 1.5638,
1200,1200,
frequencias,
silabas_timestamp)

rectas(1.8772  + 1.5638,1.8959 + 1.5638,
1200,1150,
frequencias,
silabas_timestamp)

rectas(1.8959 + 1.5638, 1.9458+ 1.5638,
1150,680,
frequencias,
silabas_timestamp)

rectas(1.9458 + 1.5638 ,1.9847 + 1.5638 ,
680,580,
frequencias,
silabas_timestamp)

rectas(1.9847 + 1.5638 ,2.0038 + 1.5638 ,
580,460,
frequencias,
silabas_timestamp)




































