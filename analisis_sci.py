#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:39:05 2020

Calcula similitud entre fragmentos de cantos sintéticos y reales
usando un rango de parámetros para gamma (fuente sonora), R y C (filtros)

Devuelve el gamma, R y C que sintetiza el canto mas similar al canto real

BOS tiene que estar sampleado a 44100 Hz

@author: javi_lassaortiz

"""
import numpy as np     	
import random
import pandas as pd
import matplotlib.pyplot as plt
import glob

from scipy.io.wavfile import write, read
from scipy import signal
from scipy.signal import sosfiltfilt
from tqdm import tqdm


global alp
global b
global feedback1 
global estimulo1
global destimulodt1

    
# -----------------------
# Definicion de funciones
# -----------------------


# Sistema de ecuaciones del modelo
# Se utiliza asi: rk4(ecuaciones,v,n,t,dt)
def ecuaciones(v, dv):
    x ,y,i1,i2,i3 = v
    dv[0]=y
    dv[1]=gamma*gamma*alp+b*gamma*gamma*x-gamma*gamma*x*x*x-gamma*x*x*y+gamma*gamma*x*x-gamma*x*y
    dv[2]= i2
    dv[3]=-uolg*uoch*i1-(rdis*uolg)*i2+uolg*destimulodt
    dv[4]=0.
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




# Toma a la frec fundamental de cada silaba como una expo, recta o seno y
# modifica alpha para que fone el sistema y frecuencias y amplitudes
def expo(ti,tf,wi,wf,factor,frequencias,amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]=wf+(wi-wf)*np.exp(-3*(t-ti)/((tf-ti)))
        alpha[i+k]= -0.150 # alpha suficiente para fonar
        #alpha[i+k]=-0.125
        
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) * (1+random.normalvariate(0.,.4)) +factor/10 * (1+random.normalvariate(0.,.02))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) * (1+random.normalvariate(0.,.2)) +factor/10 * (1+random.normalvariate(0.,.01))
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) + factor/10
    
    
    return frequencias,amplitudes


def rectas(ti,tf,wi,wf,factor,frequencias,amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]= wi + (wf-wi)*(t-ti)/(tf-ti) 
        alpha[i+k]= -0.150 # alpha suficiente para fonar
        #alpha[i+k]=-0.125
        
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.4))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.2))
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))
    
    return frequencias,amplitudes


def senito(ti,tf,media,amplitud,alphai,alphaf,factor,frequencias, amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t = ti+k*dt
        frequencias[i+k]=media+amplitud*np.sin(alphai+(alphaf-alphai)*(t-ti)/(tf-ti))
        alpha[i+k]= -0.150 # alpha suficiente para fonar
        #alpha[i+k]=-0.125 
        
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.2))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.1))
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))
    
    return frequencias,amplitudes


# Genera FFT de np.array
def array2fft(npArray, samplingRate, ti, tf, log = False):
    
    # Conservo solo la parte de la señal de interes
    section = npArray[int(ti*samplingRate):int(tf*samplingRate)]
    
    # Calculo fft
    section_fft = np.fft.fft(section) /len(section)
 
    # No se bien porque pero necesito sacar las frecuencias de la mitad superior
    section_fft = abs(section_fft[range(int(len(section)/2))])   
    
    # Paso a escala log
    if log:
        section_fft = np.log(section_fft)                     
        
    # Hago vector de frecuencias para poder graficar
    tpCount     = len(section)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/samplingRate
   
    frequencies = values/timePeriod
    freq_sampligRate = max(frequencies) / len(frequencies) 
    
    return frequencies, freq_sampligRate, section_fft


# Filtra npArray y conserva ancho de banda 300Hz - 12000 Hz
def denoisear(npArray, samplingRate):
    
    sos1 = signal.butter(4, 300, 'high', fs = samplingRate, output ='sos')
    sos2 = signal.butter(4, 12000, 'low',fs = samplingRate, output ='sos')
    
    arrayFiltered = sosfiltfilt(sos1, npArray)
    arrayFiltered = sosfiltfilt(sos2, arrayFiltered)
    
    return arrayFiltered


# Calculo de Chi2 de dos FFT
def chi_2(fft1, fft2):
    
    chi = sum(abs(fft1 - fft2))
    mod = np.linalg.norm(fft1 - fft2)
        
    return chi, mod

# ----------------------
# Deficion de parametros
# ----------------------

# Nombre archivo donde se calculan las frecuencias fundamentales del canto
# -----------------------------------------------------------------------

# ave_fname = 'AB010-bi.py'
# tiempo_total = 2.07 # segundos

# ave_fname = 'bu49.py'
# tiempo_total = 1.048 # segundos

ave_fname = 'AB010-bi_silabaC.py'
tiempo_total = 2.07 # segundos

version = 'betaSinRuido_TEST_ajuste_GCR'

# T inicial y final en segundos de silabas que voy analisar y plotear

# silabas = {'B':[0.794424, 0.824770], 
#            'C':[0.969586,1.000902],
#            'D':[1.035681,1.108332]}

silabas = {'C':[0.969586,1.000902]}



# Parametros especificos del modelo
# ---------------------------------

# Parametros tracto vocal

f_rango = np.arange(1500, 6001, 500)
uoch_list = [f*f*40 for f in f_rango]
rdis_list = np.arange(3000, 25000, 5000)

# uoch_list = [int(40*2000*2000), int(40*2500*2500)]
# rdis_list = list(np.arange(3000.0, 25001.0, 11000.0))

# uoch_list = [40*2700*2700] # 40*2700*2700
# rdis_list = [5000/1.0] # 5000/1.0

uolg =  1./1. # 1./1.

L =  0.036 # longitud tubo ( en m? )

# Parametros de frecuencia y ventana temporal
sampling_freq = 44100 # Hz
dt = 1/sampling_freq

# Inicializo los parametros de control
alpha = np.zeros(np.int(tiempo_total/(dt)))
beta = np.zeros(np.int(tiempo_total/(dt)))

# Modifico valores variables que cree arriba
for i in range(np.int(tiempo_total/(dt))):
    alpha[i] = 0.15 # sistema no fona en este valor
    beta[i] = 0.15 # sistema no fona en este valor


# ----------------------------------------------
# Calculamos trazas de frecuencias fundamentales
# ----------------------------------------------

# Inicializo las frecuencias fundamentales y amplitudes
frequencias = np.zeros(np.int(tiempo_total/(dt)))
amplitudes = np.zeros(np.int(tiempo_total/(dt)))

with open(ave_fname) as f:
    code = compile(f.read(), ave_fname, 'exec')
    exec(code)



# ----------------------------------------------
# Calculamos Beta (a partir de las trazas de ff)
# ----------------------------------------------

# Lista con nombres de mapas b_w para cada gamma
lista_mapas_b_w = glob.glob('/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/mapas_b_w/*.txt')

# Listas donde guardo todos los valores de Chi, C, R y Gamma explorados
chi_resultados = []
modulo_resultados = []
c_resultados = []
r_resultados = []
gamma_resultados = []

# Para cada gamma calculo betas a partir de las trazas de frecuencias
for mapa_fn in tqdm(lista_mapas_b_w):
    gamma = int(mapa_fn[86:91]) # Extraigo valor del gamma del nombre del archivo
    
    # Abro el archivo b_w
    bes,was = np.loadtxt(mapa_fn ,unpack=True)
       
    # Ajustamos was vs bes a un polinomio de grado 5
    # z es una lista de los coeficientes del polinomio ajustado
    z = np.polyfit(was, bes, 5)
    
    # Generamos objeto p, que es un polinomio de grado 5 (es z, hecho objeto)
    p = np.poly1d(z)
    
    # Calculamos beta como resultado de valuar p() en frecuencias fundamentales
    for i in range(np.int(tiempo_total/(dt))):
        # if se cumple siempre que aplique senito(), recta() o exp()
        # es decir: si el sistema esta fonando
        if(alpha[i]<0):
            # beta es el polinomio p valuado en frecuencias[i]
            beta[i] = p(frequencias[i])
     
        
    
    # -----------
    # Integracion
    # -----------
    
    
    # Recorro grilla de valores de C y R (parametros del tracto vocal)
    for c in uoch_list:
        for r in rdis_list:
            
            uoch = c
            rdis = r
            
            # Condiciones iniciales
            v = np.zeros(5)
            v[0], v[1], v[2], v[3], v[4] =0.01,0.001,0.001, 0.0001, 0.0001
            
            
            n = 5 # TAMANO DEL SISTEMA DE ECUACIONES
            sonido = []
            
            # Variables intermedias  de la integracion que quizas quiera guardar
            x_out = []
            y_out = []
            #tiempo1 = []
            #amplitud1 = []
            forzado_out = []
            #dforzadodt1 = []
            #elbeta1 = []
            
            
            # No saco lo de abajo porque lo necesita destimulodt pero no se bien que hacen
            N = int((L /(350*dt))//1) # 350 velocidad sonido en el aire (charla con camilo)
            fil1 = np.zeros(N)
            back1 = np.zeros(N)
            # feedback1 = 0
            
            # Integro
            for i in range(np.int(tiempo_total/(dt))):
                
                # Parametros dependientes del tiempo del sistema de ecuaciones
                # Variables globales ¿es necesario que asi lo sean?
                alp=alpha[i]
                
                #b=beta[i]*(1+random.normalvariate(0.,.3))
                #b=beta[i]*(1+random.normalvariate(0.,.2))
                b=beta[i]
                
                destimulodt = (fil1[N-1]-fil1[N-2])/dt
                
                
                # Integracion
                t =i*dt
                rk4(ecuaciones,v,n,t,dt) # modifica v
               
                
                # Actualizo las siguientes variables
                estimulo=fil1[N-1]
                fil1[0]= v[1] + back1[N-1]
                back1[0]=-0.35*fil1[N-1] #-0.35 coef de reflexion  
                fil1[1:]=fil1[:-1]
                back1[1:]=back1[:-1]
                #feedback1=back1[N-1]
            
            
                # Guardo resultado de integracion v[3] en sonido
                sonido.append(v[3]*amplitudes[i])
                
                
                # Guarda variables intermedias de interes
                x_out.append(v[0])  
                y_out.append(v[1])
                #tiempo1.append(t)
                #amplitud1.append(amplitudes[i])
                forzado_out.append(estimulo)
                #dforzadodt1.append(destimulodt)
                #elbeta1.append(beta[i])
              
            
            sonido = np.asarray(sonido)
            
            
            
            # ----------------------
            # Guardo canto sintetico
            # ----------------------
            
            # Este paso es necesario para que el archivo wav se guarde correctamente
            # Ver la documentacion de: scipy.io.wavfile.write
            scaled = np.int16(sonido/np.max(np.abs(sonido)) * 32767)
            #write(f'{gamma}_{nombre_ave}_SYN_{version}.wav', int(sampling_freq), scaled)
            
            # Guardo salida de fuente.
            y_scaled = np.int16(y_out/np.max(np.abs(y_out)) * 32767)
            #write(f'{gamma}_{nombre_ave}_Y_{version}.wav', int(sampling_freq), y_scaled)
            
            # -------
            # Ploteos
            # -------
            
            # Ploteo sonido y otras salidas
            # -----------------------------
            
            # plt.figure()
            # plt.plot(sonido/np.max(np.abs(sonido)) + 6, label= 'sonido')
            # plt.plot(x_out/np.max(np.abs(x_out)) + 4 ,label = 'x')
            # plt.plot(y_out/np.max(np.abs(y_out)) + 2, label = 'y')
            # plt.plot(forzado_out/np.max(np.abs(forzado_out)) , label = 'forzado')
            # plt.legend()
            # plt.show()
             
            # plt.close()
            
            
            
            
            # ------------------------
            # Calculo FFT de BOS y SYN
            # ------------------------

            for silaba in silabas.items():
                    
                # Cargo BOS, fuente y SYN como np.array y conservo ademas los sampling rate
                rate_bos, BOS = read(nombre_BOS)
                rate_y , Y = sampling_freq, y_scaled
                rate_syn, SYN = sampling_freq, scaled
                
                # Filtro BOS y SYN
                BOS = denoisear(BOS, rate_bos)
                SYN = denoisear(SYN, rate_syn)
                       
                # Defino comienzo y fin de la silaba
                tin = silaba[1][0]
                tfin = silaba[1][1]
                silaba_id = silaba[0]
                
                frequencies_BOS, frequencies_BOS_sr, BOS_fft = array2fft(BOS, rate_bos, tin, tfin, log = True)
                frequencies_Y, frequencies_Y_sr, Y_fft = array2fft(Y, rate_y, tin, tfin, log = True)
                frequencies_SYN, frequencies_SYN_sr, SYN_fft = array2fft(SYN, rate_syn, tin, tfin, log = True)
                
                
                # ------------
                # Calculo Chi2
                # ------------
                
                chi2, modulo = chi_2(BOS_fft, SYN_fft)
                
                # ----------
                # Ploteo FFT
                # ----------
                
                # Escala Log
                fig, axs = plt.subplots(3, 1,sharex=True, figsize=(60, 20))    
                
                fig.suptitle(f'{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r}_chi2_{chi2}_mod_{modulo}')
                
                axs[0].plot(frequencies_BOS, abs(BOS_fft))
                axs[0].set_title('BOS')
                #axs[0].set_yscale('log')
                
                axs[1].plot(frequencies_Y, abs(Y_fft), 'tab:orange')
                axs[1].set_title('Y')
                #axs[1].set_yscale('log')
                
                axs[2].plot(frequencies_SYN, abs(SYN_fft), 'tab:green')
                axs[2].set_title('SYN')
                #axs[2].set_yscale('log')
        
                axs[2].set_xlim([0,10000])
                axs[2].set_xlabel('Frecuencias (Hz)')
                
                plt.savefig(f'/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/analisis_riquesa_espectral/{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r}.pdf')
                plt.show()
                #plt.close()
                
            chi_resultados.append(chi2)
            modulo_resultados.append(modulo)
            c_resultados.append(c)
            r_resultados.append(r)
            gamma_resultados.append(gamma)

resultados = {'G': gamma_resultados, 
              'C': c_resultados, 
              'R': r_resultados,
              'Chi2': chi_resultados,
              'Mod': modulo_resultados}

resultados = pd.DataFrame(resultados)
 
resultados

m = min(resultados.Mod)   
ch = min(resultados.Chi2)

print(resultados[resultados.Mod == m])

print(resultados[resultados.Chi2 == ch] )       
        
