"""
Created on Tue Jul 21 10:28:48 2020

@author: javi_lassaortiz
"""

nombre_ave = 'AB010-bi'
nombre_BOS = '/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/zfAB010-bi_BOS03_44100.wav'


# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales y amplitud
    
# expo(ti,tf,wi,wf,factor,frequencias,amplitudes)
# rectas(ti,tf,wi,wf,factor,frequencias,amplitudes)
# senito(ti,tf,media,amplitud,alphai,alphaf,factor,frequencias, amplitudes)

# Notas intro
expo(0.021233,0.070797,869.3,475.2,0.2239/0.944,frequencias, amplitudes)
expo(0.163317,0.205335,825.5,453,0.2714/0.944,frequencias, amplitudes)
expo(0.271632,0.313879,847.4,475.1,0.3216/0.944,frequencias, amplitudes)
expo(0.383282,0.425770,891,475.1,0.3449/0.944,frequencias, amplitudes)
rectas(0.467733,0.479150,812.64,812.64,0.08789/0.944,frequencias, amplitudes)
expo(0.479152,0.527799,897,518.9,0.325/0.944,frequencias,amplitudes)
rectas(0.592287,0.631223,573,431,0.3074/0.944,frequencias, amplitudes)
rectas(0.699323,0.726651,847.4,497,0.2258/0.944,frequencias, amplitudes)

# B
rectas(0.794424,0.824770,1550,1550,0.8599/0.944,frequencias, amplitudes) 
expo(0.824771,0.929312,900,518.9,0.7771/0.944,frequencias, amplitudes)

# C
rectas(0.956319,0.969585,475,850,0.3498/0.944,frequencias, amplitudes)
rectas(0.969586,1.000902,850,850,0.4434/0.944,frequencias, amplitudes)

# D
#rectas(1.035779,1.036574,475,570,0.389/0.944,frequencias, amplitudes)
#rectas(1.036578,1.099138,579.72,559.72,0.9205/0.944,frequencias, amplitudes)
#rectas(1.099139,1.107158,579.72,409.4,0.2376/0.944,frequencias, amplitudes)
rectas(1.035681,1.108332,576,576,0.9205/0.944,frequencias, amplitudes)


rectas(1.134231,1.139772,935,1548,0.1221/0.944,frequencias, amplitudes)
rectas(1.141474,1.160209,546.62,546.62,0.1221/0.944,frequencias, amplitudes)
rectas(1.160210,1.173081,546.62,344,0.4057/0.944,frequencias, amplitudes)

senito(1.212321,1.223899,1132,1877,-np.pi/2,np.pi/2,0.2076/0.944,frequencias, amplitudes)
senito(1.2240,1.251077,2534,963,-3*np.pi/2,15*np.pi/2,0.3622/0.944,frequencias, amplitudes)
expo(1.259591,1.284083,1263,803,0.3622/0.944,frequencias, amplitudes)

rectas(1.357033,1.364902,1571,1571,0.531/0.944,frequencias, amplitudes)
rectas(1.366208,1.382211,1592,1592,0.8903/0.944,frequencias,amplitudes)
rectas(1.386501,1.486461,1023,475,0.7487/0.944,frequencias,amplitudes)
rectas(1.521486,1.529366,497,847,0.3285/0.944,frequencias,amplitudes)
rectas(1.530969,1.564968,977,828,0.4556/0.944,frequencias,amplitudes)

# A2
#rectas(1.599836,1.606783,497,565,0.3814/0.944,frequencias,amplitudes)
#rectas(1.606784,1.660270,558,558,0.7228/0.944,frequencias,amplitudes)
#rectas(1.660270,1.670171,558,387.5,0.4041/0.944,frequencias,amplitudes)
rectas(1.599836,1.670171,564,564.5,0.7228/0.944,frequencias,amplitudes)

rectas(1.699486,1.726439,540.73,540.73,0.4691/0.944,frequencias,amplitudes)
rectas(1.726440,1.737927,540.73,365.6,0.2306/0.944,frequencias,amplitudes)
senito(1.775943,1.787108,1142,563,-np.pi,np.pi,0.1919/0.944,frequencias, amplitudes)
senito(1.787778,1.817603,2414,927,-np.pi/2,15*np.pi/2,0.2852/0.944,frequencias, amplitudes)
expo(1.824992,1.848924,737,387,0.1677/0.944,frequencias,amplitudes)
rectas(1.931650,1.948097,1550,1550,0.944/0.944,frequencias,amplitudes)
expo(1.948099,2.06,1023,431,0.7555/0.944,frequencias,amplitudes)
