"""
Created on Tue Jul 21 10:28:48 2020

@author: javi_lassaortiz
"""

nombre_ave = 'bu49'


# Calculamos trazas de frecuencias fundamentales de este canto en particular
# --------------------------------------------------------------------------

# Para cada silaba defino: alpha, frecuencias fundamentales y amplitud
    
# expo(ti,tf,wi,wf,factor,frequencias,amplitudes)
# rectas(ti,tf,wi,wf,factor,frequencias,amplitudes)
# senito(ti,tf,media,amplitud,alphai,alphaf,factor,frequencias, amplitudes)

# E
rectas(0.759502,0.773161,1322,659,0.009521/0.944,frequencias,amplitudes)
rectas(0.773161,0.838972,659,659,0.01624/0.944,frequencias,amplitudes)
rectas(0.838972,0.850792,659,523,0.01425/0.944,frequencias,amplitudes)


# F
expo(0.885326,0.924609,1900,585,0.06802/0.944,frequencias,amplitudes)
rectas(0.924609,0.985073,585,585,0.04819/0.944,frequencias,amplitudes)
rectas(0.985073,1.013016 ,585,430,0.04483/0.944,frequencias,amplitudes)


