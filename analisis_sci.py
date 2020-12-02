#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:39:05 2020

Calcula similitud entre fragmentos de cantos sintéticos y reales
usando un rango de parámetros para gamma (fuente sonora), R y C (filtros)

Devuelve el gamma, R y C que sintetiza el canto mas similar al canto real

** BOS tiene que estar sampleado a 44100 Hz **

@author: javi_lassaortiz

"""
    	
import random
import glob
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.feature_selection import mutual_info_regression
from scipy.io.wavfile import write, read
from scipy.signal import sosfiltfilt, butter, hilbert, savgol_filter
from scipy.stats import pearsonr, spearmanr, kendalltau
from sklearn.metrics import r2_score
from copy import deepcopy
from tqdm import tqdm

global alp
global b
global feedback1 
global estimulo1
global destimulodt1
global hilb
global tau



    
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


# Modela cada gesto de frec fundamental como una expo, recta o seno.
# Modifica alpha para que el sistema fone.
# Guarda inicio y finales de cada gestos de frecuencia.
def expo(ti,tf,wi,wf,factor,frequencias, silabas_timestamp):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]=wf+(wi-wf)*np.exp(-3*(t-ti)/((tf-ti)))
        alpha[i+k]= -0.150 # alpha suficiente para fonar
        
    silabas_timestamp.append(i)
    silabas_timestamp.append(j)
  
    return frequencias, silabas_timestamp


def rectas(ti,tf,wi,wf,factor,frequencias, silabas_timestamp):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]= wi + (wf-wi)*(t-ti)/(tf-ti) 
        alpha[i+k]= -0.150 # alpha suficiente para fonar
        
    silabas_timestamp.append(i)
    silabas_timestamp.append(j)     
        
    return frequencias, silabas_timestamp


def senito(ti,tf,media,amplitud,alphai,alphaf,factor,frequencias, silabas_timestamp):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t = ti+k*dt
        frequencias[i+k]= media + amplitud * np.sin(alphai+(alphaf-alphai)*(t-ti)/(tf-ti))
        alpha[i+k]= -0.150 # alpha suficiente para fonar
        
    silabas_timestamp.append(i)
    silabas_timestamp.append(j)
        
    return frequencias,silabas_timestamp


# Genera FFT de np.array
def array2fft(npArray, samplingRate, ti, tf, log = False):
    
    # Conservo solo la parte de la señal de interes
    section = npArray[int(ti*samplingRate):int(tf*samplingRate)]
    n = len(section)
    
    # Calculo el Power Frequencies (ver documentacion de np.fft)
    section_fft = np.absolute(np.fft.fft(section))**2

    # Saco frecuencias negativas (mitad superior del array. Ver documentacion np.fft)
    section_fft = section_fft[range(int(n/2))]

    # Paso a escala log
    if log:
        section_fft = np.log(section_fft, where=(section_fft != 0))  
    
    # Genero vector de Frecuencias (conservo solo las positivas)
    frequencies = np.fft.fftfreq(n , d = 1/samplingRate)
    frequencies = frequencies[range(int(n/2))] 
    
    return frequencies, section_fft


# Filtra npArray y conserva ancho de banda 300Hz - 12000 Hz
def denoisear(npArray, samplingRate):
    
    sos = butter(4, 300, 'high', fs = samplingRate, output ='sos')
    
    arrayFiltered = sosfiltfilt(sos, npArray)
    
    return arrayFiltered


# Calculo de Chi2 de dos señales tipo npArray 1D
def buen_ajuste(obs, pred): # obs = BOS,   pred = SYN
    
    # Traslado la señal para que no contengan ceros y chi2 esté bien definido siempre
    minimo = abs(min(pred)) + 1 
    obs_aux = obs + minimo
    pred_aux = pred + minimo

    # Calculo Chi2    
    chi = sum( ((obs_aux - pred_aux)**2)/ pred_aux )

    # Calculo varios parámetros de correlación
    pearson_r, p_value = pearsonr(obs, pred)
    sperman_r, p_value = spearmanr(obs, pred)
    kendal_t, p_value = kendalltau(obs, pred)
    
    # Calculo la información mutua
    info_m = mutual_info_regression(obs.reshape(-1,1), pred)[0]
    
    # Calculo el coeficiente de determinación
    R2 = r2_score(obs, pred)
    
    return chi, pearson_r, sperman_r, kendal_t, info_m, R2


# Extra pequeña sección de sonido al rededor de la máxima amplitud
def silaba_chopper(sound, ti, tf, fs):
    
    # Conservo silaba de interes
    silaba = sound[int(ti*fs):int(tf*fs)]
    
    # Conservo solo parte de la silaba de los alrededores de la máxima amplitud
    # la ventana que uso es tal que si la ff es de 300Hz, agarro 6 oscilaciones
    ventana = int( 0.010 * fs) # Ventana de 10 ms
    # ventana = int(0.005 * fs) # Ventana de 5 ms
    index_max = np.argmax(silaba)

    # Estrategia para salvar casos que el máximo esta muy cerca de los extremos de la silaba
    if index_max - ventana < 0 or index_max + ventana > len(silaba):
        mitad = int( len(silaba)/2 )
        ventana_5ms = int(0.002*fs)
        index_aux = np.argmax(silaba[mitad - ventana_5ms: mitad + ventana_5ms])        
        index_max = mitad + (index_aux - ventana_5ms)
    
    silaba = silaba[index_max - ventana : index_max + ventana]
    
    return silaba


def find_envolvente(sonido):
    
    # Calculo transformada de Hilbert
    envolvente_h = hilbert(sonido)
    
    # Integro para suavizar
    envolvente_int = []
    
    e = [0.0]    
    
    for i in range(np.int(tiempo_total/(dt))):
        
        hilb = envolvente_h[i]
        tau = 0.001
        
        # Integracion RK4
        n = 1 # dimensión del sistema
        
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
            v1[x]=e[x]
            
        xi = v1[x]
        k1[x] = -(1/tau) * xi + np.abs(hilb)       
                         
        for x in range(0, n):
            v1[x]=e[x]+dt2*k1[x]
            
        xi = v1[x]
        k2[x] = -(1/tau) * xi + np.abs(hilb)       
        
        for x in range(0, n):
            v1[x]=e[x]+dt2*k2[x]

        xi = v1[x]
        k3[x] = -(1/tau) * xi + np.abs(hilb)       
        
        for x in range(0, n):
            v1[x]=e[x]+dt*k3[x]

        xi = v1[x]
        k4[x] = -(1/tau) * xi + np.abs(hilb)       
        
        for x in range(0, n):
            v1[x]=e[x]+dt*k4[x] #parece al pedo este paso
            
        for x in range(0, n):
            e[x]=e[x]+dt6*(2.0*(k2[x]+k3[x])+k1[x]+k4[x])
                
        envolvente_int.append(e[0])
    
    # Aplico filtro Savitzky-Golay
    envolvente = savgol_filter(envolvente_int, 513, 4)
    
    return envolvente




# ----------------------
# Deficion de parametros
# ----------------------

# Inicializo generador de números pseudo-random para poder replicar resultados
random.seed(123)

# Nombre archivo donde se calculan las frecuencias fundamentales del canto
# -----------------------------------------------------------------------

ave_fname = 'AB010-bi.py'
tiempo_total = 2.07 # segundos 

version = 'variaciones_25929'

guardar_syn  = True
guardar_plot = True

# T inicial y final en segundos de silabas que voy analisar

silabas = {'D': [0.969586, 1.000902],
           'E': [1.035681, 1.108332],
           'C': [0.825773, 0.929312]}

# silabas = {'B_ds': [0.699490,0.724839],
#            'C_hs': [0.795595, 0.822859],
#            'C_ds:': [0.825773, 0.929312],
#            'D': [0.969586, 1.000902],
#            'E': [1.035681, 1.108332],
#            'F': [1.158998, 1.175064]}
         
  
         

# Frecuencia y ventana temporal
# -----------------------------

sampling_freq = 44100 # Hz
dt = 1/sampling_freq


# Parametros del modelo
# ---------------------

# Parámetros de la fuente
alpha = np.zeros(np.int(tiempo_total/(dt))) # Inicializo los parametros de control
beta = np.zeros(np.int(tiempo_total/(dt))) # Inicializo los parametros de control

for i in range(np.int(tiempo_total/(dt))):
    alpha[i] = 0.15 # sistema no fona en este valor
    beta[i]  = 0.15 # sistema no fona en este valor
    
# Lista con nombres de mapas b_w para cada gamma
lista_mapas_b_w = glob.glob('/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/mapas_b_w/*.txt')

# Parametros tracto vocal (filtro)
# f_rango = np.arange(500, 9001, 100) # 85 it
# uoch_list = [f*f*40 for f in f_rango] # rango 
# rdis_list = np.arange(1000, 40001, 1000) # 40 it

f_rango = np.arange(5010, 5200, 10)
uoch_list = [f*f*40 for f in f_rango]
rdis_list = np.arange(9100, 11000, 100) 

uolg =  1.0
L =  0.036 # Longitud tubo (en metros) (0.036)
coef_reflexion = - 0.35 # -0.35 

# Ruido
ruido_beta = 0.0 # 0.001 es el mínimo paso 
ruido_amplitud = 0.0 # porcentaje de la amplitud maxima del desvío del error

# Condiciones iniciales y tamaño del sistema de ecuaciones
v = np.zeros(5)
n = 5 # Tamaño del sistema de ecuaciones




# ---------------------------------------
# Listas donde vamos a guardar resultados
# ---------------------------------------

# Lista de parámetros de bondad de ajuste
chi2_log_resultados = []
pearsonR_log_resultados = []
spermanR_log_resultados = []
kendalT_log_resultados = []
infoM_log_resultados = []
R2_log_resultados = []

chi2_lin_resultados = []
pearsonR_lin_resultados = []
spermanR_lin_resultados = []
kendalT_lin_resultados = []
infoM_lin_resultados = []
R2_lin_resultados = []

chi2_s_resultados = []
pearsonR_s_resultados = []
spermanR_s_resultados = []
kendalT_s_resultados = []
infoM_s_resultados = []
R2_s_resultados = []

chi2_all_resultados = []
pearsonR_all_resultados = []
spermanR_all_resultados = []
kendalT_all_resultados = []
infoM_all_resultados = []
R2_all_resultados = []

# Lista de parámetros C, R y Gamma
c_resultados = []
r_resultados = []
gamma_resultados = []

# Lista de las sílabas
silabas_resultados = []

# Número de ID de set de parámetros (para facilitar la búsqueda)
Id = 0
Id_list = []

# Número de Iteración teniendo en cuenta el número de sílabas
it = 1 # Itereación actual
n_G = len(lista_mapas_b_w) # Total de gammas
n_R = len(rdis_list) # Total de R
n_C = len(uoch_list) # Total de C
n_s = len(silabas) # Total de sílabas 
it_totales = n_G * n_R * n_C * n_s

# ------------------------------------------------------------
# Calculamos trazas de frecuencias fundamentales y envolventes
# ------------------------------------------------------------

# Inicializo las frecuencias fundamentales y time_stamps de los gestos de ff
frequencias = np.zeros(np.int(tiempo_total/(dt)))
silabas_timestamp = []

# Corro scritp que genera la traza de ff
with open(ave_fname) as f:
    code = compile(f.read(), ave_fname, 'exec')
    exec(code)

# Cargo el BOS
rate_bos, BOS = read(nombre_BOS)
BOS = np.array(BOS, dtype= 'float64')

# Calculo envolvente como en Boari 2015 ("automatic")
envolvente = find_envolvente(BOS)




# ----------------------------------------------
# Calculamos Beta (a partir de las trazas de ff)
# ----------------------------------------------

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
        if (alpha[i]<0):
            # beta es el polinomio p valuado en frecuencias[i]
            beta[i] = p(frequencias[i])
     
        
    
    
    # --------------------------------
    # Integracion del sistema dinámico
    # --------------------------------
    
    # Recorro grilla de valores de C y R (parametros del tracto vocal)
    for c in uoch_list:
        for r in rdis_list:
            
            uoch = c
            rdis = r
            
            # Condiciones iniciales
            v[0], v[1], v[2], v[3], v[4] =0.01,0.001,0.001, 0.0001, 0.0001
            
            v_3 = [] # Salida del modelo
            sonido = [] # Salida del modelo escaleada con amplitud del BOS
            
            # Variables intermedias  de la integracion que quizas quiera guardar
            # x_out = []
            y_out = []
            # tiempo1 = []
            # amplitud1 = []
            # forzado_out = []
            # dforzadodt1 = []
            # elbeta1 = []
            
            N = int((L /(350*dt))//1) # 350 vel sonido en aire. N: cantidad segmentos en las que divido el tubo.
            fil1 = np.zeros(N)
            back1 = np.zeros(N)
            # feedback1 = 0
            
            # Integro
            for i in range(np.int(tiempo_total/(dt))):
                
                # Parametros dependientes del tiempo del sistema de ecuaciones
                # Variables globales ¿es necesario que asi lo sean?
                alp = alpha[i]
                b = beta[i] + random.normalvariate(0, ruido_beta)
                destimulodt = (fil1[N-1]-fil1[N-2])/dt
                
                # Integracion
                t =i*dt
                rk4(ecuaciones,v,n,t,dt) # modifica v
                
                # Actualizo las siguientes variables
                estimulo = fil1[N-1]
                fil1[0] = v[1] + back1[N-1]
                back1[0] = coef_reflexion * fil1[N-1] 
                fil1[1:] = fil1[:-1]
                back1[1:] = back1[:-1]
                # feedback1=back1[N-1]
                 
                # Guardo salida del modelo (falta escalearla con la envolvente)
                v_3.append(v[3])             
    
                # Guarda otras variables de interes de la integracion
                # x_out.append(v[0])  
                y_out.append(v[1]) # Salida de la fuente! 
                # tiempo1.append(t)
                # forzado_out.append(estimulo)
                # dforzadodt1.append(destimulodt)
                # elbeta1.append(beta[i])
            
            
            
            
            # --------------------------------------------------------
            # Escaleo amplitud de cada uno de los gestos de frecuencia
            # --------------------------------------------------------
            
            v_3 = np.asarray(v_3) /max(v_3) # es necesario para encontrar k que escalee correctamente y evitar errores
            
            # Inicializo vector k para re-escaleo. 
            # Este vector k multiplicado por la salida del modelo (v[3]) va a dar el 
            # sonido final (cuya envolvente va a ser muy similar a la del BOS)
            k = deepcopy(envolvente)
            k = np.asarray(k)
            
            # Agrego ruido para que el sonido final tenga una envolvente ruidosa y algo distinta a la del BOS
            if ruido_amplitud > 0:
                maximo_envolvente = max(k)
                for i in range(len(k)):
                    # El ruido tiene media cero y un desvío estandar del x % de la máxima amplitud
                    ruido = maximo_envolvente * random.normalvariate(0, ruido_amplitud)
                    k[i] = k[i] + ruido
            
            # Modifico vector k para que re-escale la salida del modelo v[3] correctamente
            i = 0
            while i < len(silabas_timestamp):
                
                # Tomo timestamp de inicio y final de cada gesto de frecuencia
                inicio = silabas_timestamp[i]
                fin = silabas_timestamp[i+1]
                
                # Calculo el maximo en cada uno de los gestos de frecuencia en la salida del modelo (v[3])
                maximo_v_3 = max(v_3[inicio:fin])
                  
                # Modifico k (era originalmente la envolvente)
                for j in np.arange(inicio, fin):
                    k[j] = k[j] / maximo_v_3
                
                # Paso al siguiente gesto de frecuencia
                i = i + 2
            
            # Salida del modelo escaleada a la envolvente del BOS mediante el factor k   
            sonido = v_3 * k 
            
            
            
            
            # ----------------------
            # Guardo canto sintetico
            # ----------------------
            
            # Este paso es necesario para que el archivo wav se guarde correctamente
            # Ver la documentacion de: scipy.io.wavfile.write
            scaled = np.int16(sonido/np.max(np.abs(sonido)) * 32767) # * (0.4434) Agrego factor de tamaño de la silaba.
            if guardar_syn:
                write(f'/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/analisis_riquesa_espectral/{Id}_{gamma}_{version}_C_{c}_R_{r}_{nombre_ave}_SYN.wav', int(sampling_freq), scaled)
                    
            # Guardo salida de fuente.
            y_scaled = np.int16(y_out/np.max(np.abs(y_out)) * 32767) # * (0.4434) Agrego factor de tamaño de la silaba.
            # write(f'{gamma}_{nombre_ave}_Y_{version}.wav', int(sampling_freq), y_scaled)
            
            
            
            
            # ------------------------------------
            # Calculo FFT de BOS, SYN y Fuente (Y)
            # ------------------------------------

            # Cargo SYN y FUENTE como npArray y conservo ademas los sampling rate
            rate_syn, SYN = sampling_freq, scaled
            SYN = np.array(SYN, dtype= 'float64')
            
            rate_Y, Y = sampling_freq, y_scaled
            Y = np.array(Y, dtype = 'float64')
            
            # # Filtro BOS y SYN
            # BOS = denoisear(BOS, rate_bos)
            # SYN = denoisear(SYN, rate_syn)
            
            # Calculo FFT de TODO el BOS y SYN
            frequencies_BOS_all, BOS_fft_all = array2fft(BOS, rate_bos, 0, tiempo_total, log = True)
            frequencies_SYN_all, SYN_fft_all = array2fft(SYN, rate_syn, 0, tiempo_total, log = True)
            frequencies_Y_all, Y_fft_all     = array2fft(Y,   rate_syn, 0, tiempo_total, log = True)
            
            # Calculo índices de bondad de ajuste del FFT y SYN completos
            chi2_all, pearsonR_all, spermanR_all, kendalT_all, infoM_all, R2_all = buen_ajuste(BOS_fft_all, SYN_fft_all)
            
            # # Guardo indices de bondad de ajuste del FFT del SYN completo            
            # silabas_resultados.append('SYN all') 
            # chi2_all_resultados.append(chi2_all)
            # pearsonR_all_resultados.append(pearsonR_all)
            # spermanR_all_resultados.append(spermanR_all)
            # kendalT_all_resultados.append(kendalT_all)
            # infoM_all_resultados.append(infoM_all)
            # R2_all_resultados.append(R2_all)  

            for silaba in silabas.items():
                
                # Print calculo actual
                print(f'\nSilaba: {silaba} \nGamma: {gamma} \nC: {c} \nR: {r} \nit: {it}/{it_totales}')
                it = it + 1 # Actualizo la iteración actual
                
                # Defino comienzo y fin de la silaba
                tin = silaba[1][0]
                tfin = silaba[1][1]
                silaba_id = silaba[0]
                
                # Calculo FFT de la sílaba de ineteres escala LOG
                frequencies_BOS, BOS_fft = array2fft(BOS, rate_bos, tin, tfin, log = True)
                frequencies_SYN, SYN_fft = array2fft(SYN, rate_syn, tin, tfin, log = True)
                frequencies_Y,   Y_fft   = array2fft(Y,   rate_Y,   tin, tfin, log = True)
                
                # Calculo FFT de la sílaba de ineteres escala LINEAL
                frequencies_BOS, BOS_fft_lin = array2fft(BOS, rate_bos, tin, tfin, log = False)
                frequencies_SYN, SYN_fft_lin = array2fft(SYN, rate_syn, tin, tfin, log = False)                
                
                # Extraigo pequeña parte del sonido de la sílaba de interes
                BOS_chop = silaba_chopper(BOS, tin, tfin, sampling_freq)
                SYN_chop = silaba_chopper(SYN, tin, tfin, sampling_freq)
    

    
        
                # -----------------------------------
                # Calculo indices de bondad de ajuste
                # -----------------------------------

                chi2_log, pearsonR_log, spermanR_log, kendalT_log, infoM_log, R2_log = buen_ajuste(BOS_fft, SYN_fft)
                chi2_lin, pearsonR_lin, spermanR_lin, kendalT_lin, infoM_lin, R2_lin = buen_ajuste(BOS_fft_lin, SYN_fft_lin)
                chi2_s, pearsonR_s, spermanR_s, kendalT_s, infoM_s, R2_s = buen_ajuste(BOS_chop, SYN_chop)
                
                
                # Guardo indices de bondad de ajuste             
                chi2_log_resultados.append(chi2_log)
                pearsonR_log_resultados.append(pearsonR_log)
                spermanR_log_resultados.append(spermanR_log)
                kendalT_log_resultados.append(kendalT_log)
                infoM_log_resultados.append(infoM_log)
                R2_log_resultados.append(R2_log)
                
                chi2_lin_resultados.append(chi2_lin)
                pearsonR_lin_resultados.append(pearsonR_lin)
                spermanR_lin_resultados.append(spermanR_lin)
                kendalT_lin_resultados.append(kendalT_lin)
                infoM_lin_resultados.append(infoM_lin)
                R2_lin_resultados.append(R2_lin)
                
                chi2_s_resultados.append(chi2_s)
                pearsonR_s_resultados.append(pearsonR_s)
                spermanR_s_resultados.append(spermanR_s)
                kendalT_s_resultados.append(kendalT_s)
                infoM_s_resultados.append(infoM_s)
                R2_s_resultados.append(R2_s)
                
                chi2_all_resultados.append(chi2_all)
                pearsonR_all_resultados.append(pearsonR_all)
                spermanR_all_resultados.append(spermanR_all)
                kendalT_all_resultados.append(kendalT_all)
                infoM_all_resultados.append(infoM_all)
                R2_all_resultados.append(R2_all)  
                
                c_resultados.append(c)
                r_resultados.append(r)
                gamma_resultados.append(gamma)
                
                silabas_resultados.append(silaba_id)
                
                Id_list.append(Id)

                
                
                
                # ----------
                # Ploteo FFT
                # ----------
                
                if guardar_plot:
                    
                    # Escala Log
                    fig, axs = plt.subplots(3, 1, figsize=(110, 100))    
                    
                    fig.suptitle(f'{Id}_{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r} \n chi2.Log_{round(chi2_log, 3)}    pearson.Log_{round(pearsonR_log, 3)}    spearman.Log_{round(spermanR_log, 3)}    kendal.Log_{round(kendalT_log, 3)}    infoM.Log_{round(infoM_log, 3)}    R2.Log_{round(R2_log, 3)} \n chi2.Lin_{round(chi2_lin, 3)}    pearson.Lin_{round(pearsonR_lin,3)}    spearman.Lin_{round(spermanR_lin, 3)}    kendal.Lin_{round(kendalT_lin, 3)}    infoM.Lin_{round(infoM_lin, 3)}    R2.Lin_{round(R2_lin, 3)} \n chi2.S_{round(chi2_s, 3)}    pearson.S_{round(pearsonR_s, 3)}    spearman.S_{round(spermanR_s, 3)}    kendal.S_{round(kendalT_s, 3)}    infoM.S_{round(infoM_s, 3)}    R2.S_{round(R2_s, 3)}')
                    
                    i = 0
                    axs[i].plot(frequencies_BOS, BOS_fft)
                    axs[i].plot(frequencies_SYN, SYN_fft, 'tab:green')
                    axs[i].plot(frequencies_Y, Y_fft, 'tab:orange', linestyle = 'dotted')
                    axs[i].legend(['BOS FFT','SYN FFT', 'Fuente FFT'])
                    #axs[i].set_yscale('log')
                    axs[i].set_xlim([0,sampling_freq/2])
                    axs[i].set_ylim([0,30])
                    axs[i].set_xlabel('Frecuencias (Hz)')
                    
                    i = i+1                
                    axs[i].plot(frequencies_BOS_all, BOS_fft_all)
                    axs[i].plot(frequencies_SYN_all, SYN_fft_all, 'tab:green')
                    axs[i].plot(frequencies_Y_all, Y_fft_all, 'tab:orange', linestyle = 'dotted')
                    axs[i].legend(['BOS FFT','SYN FFT', 'Fuente FFT'])
                    #axs[i].set_yscale('log')
                    axs[i].set_xlim([0,sampling_freq/2])
                    # axs[i].set_ylim([0,30])
                    axs[i].set_xlabel('Frecuencias (Hz)')
                    
                    i = i+1                
                    axs[i].plot(np.arange(len(BOS_chop))*1000/sampling_freq, BOS_chop)
                    axs[i].plot(np.arange(len(SYN_chop))*1000/sampling_freq, SYN_chop, 'tab:green')
                    axs[i].legend(['BOS sound', 'SYN sound'])
                    #axs[2].set_yscale('log')
                    axs[i].set_xlabel('ms')
                    
                    plt.savefig(f'/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/analisis_riquesa_espectral/{Id}_{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r}.pdf')
                    plt.close()     

            
            
            
            Id = Id + 1
            
            
            
            
# --------------------------------------
# Genero tabla con todos los resultados
# --------------------------------------

resultados = {'Id': Id_list,
              'G': gamma_resultados, 
              'C': c_resultados, 
              'R': r_resultados,
              'silaba': silabas_resultados,
              'Chi2_log': chi2_log_resultados,
              'Pearson_log': pearsonR_log_resultados,
              'Spearman_log': spermanR_log_resultados,
              'Kendal_log': kendalT_log_resultados,
              'Info_Mutua_log': infoM_log_resultados,
              'R2_log': R2_log_resultados,
              'Chi2_lin': chi2_lin_resultados,
              'Pearson_lin': pearsonR_lin_resultados,
              'Spearman_lin': spermanR_lin_resultados,
              'Kendal_lin': kendalT_lin_resultados,
              'Info_Mutua_lin': infoM_lin_resultados,
              'R2_lin': R2_lin_resultados,              
              'Chi2_s': chi2_s_resultados,
              'Pearson_s': pearsonR_s_resultados,
              'Spearman_s': spermanR_s_resultados,
              'Kendal_s': kendalT_s_resultados,
              'Info_Mutua_s': infoM_s_resultados,
              'R2_s': R2_s_resultados,
              'Chi2_all': chi2_all_resultados,
              'Pearson_all': pearsonR_all_resultados,
              'Spearman_all': spermanR_all_resultados,
              'Kendal_all': kendalT_all_resultados,
              'Info_Mutua_all': infoM_all_resultados,
              'R2_all': R2_all_resultados}

resultados = pd.DataFrame(resultados)



# Busco mejores ajuste FFT (resumen)
resumen = resultados[resultados.Chi2_log == min(resultados.Chi2_log)] 
resumen = resumen.append(resultados[resultados.Pearson_log == max(resultados.Pearson_log)][:1])
resumen = resumen.append(resultados[resultados.Spearman_log == max(resultados.Spearman_log)][:1])       
resumen = resumen.append(resultados[resultados.Kendal_log == max(resultados.Kendal_log)][:1])  
resumen = resumen.append(resultados[resultados.Info_Mutua_log == max(resultados.Info_Mutua_log)][:1])
resumen = resumen.append(resultados[resultados.R2_log == max(resultados.R2_log)][:1])  

resumen = resumen.append(resultados[resultados.Chi2_lin == min(resultados.Chi2_lin)][:1])
resumen = resumen.append(resultados[resultados.Pearson_lin == max(resultados.Pearson_lin)][:1])
resumen = resumen.append(resultados[resultados.Spearman_lin == max(resultados.Spearman_lin)][:1])       
resumen = resumen.append(resultados[resultados.Kendal_lin == max(resultados.Kendal_lin)][:1])  
resumen = resumen.append(resultados[resultados.Info_Mutua_lin == max(resultados.Info_Mutua_lin)][:1])
resumen = resumen.append(resultados[resultados.R2_lin == max(resultados.R2_lin)])  

resumen = resumen.append(resultados[resultados.Chi2_s == min(resultados.Chi2_s)][:1])
resumen = resumen.append(resultados[resultados.Pearson_s == max(resultados.Pearson_s)][:1])
resumen = resumen.append(resultados[resultados.Spearman_s == max(resultados.Spearman_s)][:1])       
resumen = resumen.append(resultados[resultados.Kendal_s == max(resultados.Kendal_s)][:1])  
resumen = resumen.append(resultados[resultados.Info_Mutua_s == max(resultados.Info_Mutua_s)][:1])
resumen = resumen.append(resultados[resultados.R2_s == max(resultados.R2_s)][:1])

resumen = resumen.append(resultados[resultados.Chi2_all == min(resultados.Chi2_all)][:1])
resumen = resumen.append(resultados[resultados.Pearson_all == max(resultados.Pearson_all)][:1])
resumen = resumen.append(resultados[resultados.Spearman_all == max(resultados.Spearman_all)][:1])       
resumen = resumen.append(resultados[resultados.Kendal_all == max(resultados.Kendal_all)][:1])  
resumen = resumen.append(resultados[resultados.Info_Mutua_all == max(resultados.Info_Mutua_all)][:1])
resumen = resumen.append(resultados[resultados.R2_all == max(resultados.R2_all)][:1])    


# Resumen promediando por cada combinación de C,R y G (promedio los indices de cada silaba y el SYN total)
indices = []
columnas = ['Id', 'G', 'C', 'R', 
            'Chi2_log', 'Pearson_log', 'Spearman_log', 'Kendal_log', 'Info_Mutua_log', 'R2_log', 
            'Chi2_lin', 'Pearson_lin', 'Spearman_lin', 'Kendal_lin', 'Info_Mutua_lin', 'R2_lin', 
            'Chi2_s',   'Pearson_s',   'Spearman_s',   'Kendal_s',   'Info_Mutua_s',   'R2_s', 
            'Chi2_all', 'Pearson_all', 'Spearman_all', 'Kendal_all', 'Info_Mutua_all', 'R2_all']
lista_promedios = []

for i in range(Id):
    indices.append(i)
    lista_promedios.append(list(resultados[resultados.Id == i].mean()))
     
resumen_promedios = pd.DataFrame(lista_promedios, columns= columnas)


# GUARDO todo en tabla resumen
resumen.to_csv('resumen_busqueda_GCR.csv', header=True, decimal=',', sep=' ', float_format='%.3f')
resumen_promedios.to_csv('resumen_promedios_busqueda_GCR.csv', header=True, decimal=',', sep=' ', float_format='%.3f')
resultados.to_csv('resultados_busqueda_GCR.csv', header=True, decimal=',', sep=' ', float_format='%.3f')








