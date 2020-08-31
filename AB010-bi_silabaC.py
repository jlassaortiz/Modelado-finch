"""
Created on Tue Jul 21 10:28:48 2020

@author: javi_lassaortiz
"""

nombre_ave = 'AB010-bi_silabaC'
nombre_BOS = '/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/zfAB010-bi_BOS03_44100.wav'


# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales y amplitud
    
# expo(ti,tf,wi,wf,factor,frequencias,amplitudes)
# rectas(ti,tf,wi,wf,factor,frequencias,amplitudes)
# senito(ti,tf,media,amplitud,alphai,alphaf,factor,frequencias, amplitudes)


# C
#rectas(0.956319,0.969585,475,850,0.3498/0.944,frequencias, amplitudes)
rectas(0.969586,1.000902,850,850,0.4434/0.944,frequencias, amplitudes)