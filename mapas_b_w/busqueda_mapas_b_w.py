#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:28:50 2020

@author: javi_lassaortiz

Determinacion de mapas beta-omega para gammas determinados

Secciones:
    
    - Definición de funciones
    - Definición de parámetros
    - Calculos de mapas b-w
"""
import numpy as np     	
#from scipy.io.wavfile import write, read
from scipy.signal import find_peaks
#import matplotlib.pyplot as plt
from tqdm import tqdm


global alp
global b
   

# -----------------------
# Definicion de funciones
# -----------------------

# Sistema de ecuaciones del modelo SOLO FUENTE
# Se utiliza asi: rk4(ecuaciones,v,n,t,dt)
def ecuaciones(v, dv):
    x ,y = v
    dv[0]=y
    dv[1]=gamma*gamma*alp+b*gamma*gamma*x-gamma*gamma*x*x*x-gamma*x*x*y+gamma*gamma*x*x-gamma*x*y
    return dv

# Integrador RK4
def rk4(dv,v,n,t,dt): #  dv es la funcion ecuaciones()
    v1=[]
    
    # Inicializo cuatro dv (aunque se llaman kx son dv)
    k1=[]
    k2=[]
    k3=[]
    k4=[]
    for x in range(0, n):
        v1.append(x)
        k1.append(x)
        k2.append(x)
        k3.append(x)
        k4.append(x)
        
    dt2=dt/2.0
    dt6=dt/6.0
    
    for x in range(0, n):
        v1[x]=v[x]
    dv(v1, k1) # modifica k1
                     
    for x in range(0, n):
        v1[x]=v[x]+dt2*k1[x]
    dv(v1, k2)  # modifica k2
    
    for x in range(0, n):
        v1[x]=v[x]+dt2*k2[x]
    dv(v1, k3) # modifica k3
    
    for x in range(0, n):
        v1[x]=v[x]+dt*k3[x]
    dv(v1, k4) # modifica k4
    
    for x in range(0, n):
        v1[x]=v[x]+dt*k4[x]
        
    for x in range(0, n):
        v[x]=v[x]+dt6*(2.0*(k2[x]+k3[x])+k1[x]+k4[x])
    return v

# Calculadora frecuencia fundamental (ff)
def find_ff(y_list, sampling_freq):
    
    # Calculo fft
    y_fft = np.fft.fft(y_list) / len(y_list)
    y_fft = abs(y_fft)
    y_fft = y_fft[range(int(len(y_list)/2))]
    #y_fft = np.log(y_fft) # Lo paso a escala log

    # Hago vector de frecuencias
    tpCount     = len(y_list)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/sampling_freq
    freq = values/timePeriod   
    
    # Busco picos en fft
    picos, info_picos = find_peaks(y_fft, height= max(y_fft)*0.5)
        
    # Busco que frecuencias corresponden a esos picos
    picos = [freq[pico] for pico in picos]
    picos.insert(0, 0) # Agrago el 0 al principio de la lista
    picos = np.array(picos)
    
    # Calculo diferencias entre picos
    w_list = np.diff(picos)
    
    print(w_list)
    
    # Calculo promedio de las diferencias
    w = np.mean(w_list)

    return w


# ---------------------
# Definicion parametros
# ---------------------

version = '1'

# GAMMAS
gammas = [25000]
#gammas = [16000, 24000, 29000]
#gammas = np.arange(16000, 24000, 29000)

# BETAS
# betas,was = np.loadtxt('b_w_12300.txt',unpack=True)
# betas =np.arange(-3.5, 0.001, 0.001)
betas =np.arange(-0.130 , 0.0, 0.0001)

# Parametros de frecuencia y ventana temporal
tiempo_total = 1.0 # segundos
sampling_freq = 44100 # Hz
dt = 1/sampling_freq

# TAMANO DEL SISTEMA DE ECUACIONES
n = 2 

# Alpha suficiente para fonar
alp = - 0.150 


# ---------------------
# Calculos de mapas b-w
# ---------------------

# Hago un mapa b-w para cada gamma
for g in tqdm(gammas):
    
    gamma = g
    ws = []
    betas_aux = []
    
    for b in tqdm(betas):
        
        # Condiciones iniciales
        v = np.zeros(2)
        v[0], v[1] = 0.01, 0.001
        
        # Variables intermedias  de la integracion que quizas quiera guardar
        x_out = []
        y_out = []
    
        # Integro
        for i in range(np.int(tiempo_total/(dt))):

            t =i*dt
            rk4(ecuaciones,v,n,t,dt) # modifica v
           
            # Guarda variables de interes de la integracion
            x_out.append(v[0])  
            y_out.append(v[1])
        
        w = find_ff(y_out, sampling_freq )
        
        if w > 300 and w < 2100:
            betas_aux.append(b)
            ws.append(w)
    
    b_w = [betas_aux, ws]
    b_w = np.array(b_w).T
        
    
    
    np.savetxt(f'b_w_{g}_javi_{version}.txt', b_w, delimiter = ' ', fmt = '%1.3f')
    
    
        
      
    
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    