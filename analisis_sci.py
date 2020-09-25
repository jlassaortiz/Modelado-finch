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
import numpy as np     	
import random
import pandas as pd
import matplotlib.pyplot as plt
import glob

from scipy.io.wavfile import write, read
from scipy.signal import sosfiltfilt, butter
from scipy.stats import pearsonr, spearmanr, kendalltau
from tqdm import tqdm
from sklearn.feature_selection import mutual_info_regression
from sklearn.metrics import r2_score


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
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) * (1+random.normalvariate(0.,.2)) +factor/10 * (1+random.normalvariate(0.,.01))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) + factor/10
    
    
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
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.2))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))
    
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
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.1))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))
    
    return frequencias,amplitudes


# Genera FFT de np.array
def array2fft(npArray, samplingRate, ti, tf, log = False):
    
    # Conservo solo la parte de la señal de interes
    section = npArray[int(ti*samplingRate):int(tf*samplingRate)]
    n = len(section)
    
    # Calculo el Power Frequencies (ver documentacion de np.fft)
    section_fft = abs(np.fft.fft(section))**2

    # Saco frecuencias negativas (mitad superior del array. Ver documentacion np.fft)
    section_fft = section_fft[range(int(n/2))]

    # Paso a escala log
    if log:
        section_fft = np.log(section_fft)  
    
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
    ventana = int((3/300)*fs) # Ventana de 10 ms
    # ventana = int(0.005 * fs) # Ventana de 5 ms
    index_max = np.argmax(silaba)
    
    silaba = silaba[index_max - ventana : index_max + ventana]
    
    return silaba

# ----------------------
# Deficion de parametros
# ----------------------

random.seed(123)

# Nombre archivo donde se calculan las frecuencias fundamentales del canto
# -----------------------------------------------------------------------

# ave_fname = 'AB010-bi.py'
# tiempo_total = 2.07 # segundos

# ave_fname = 'bu49.py'
# tiempo_total = 1.048 # segundos

ave_fname = 'AB010-bi_silabaC.py'
tiempo_total = 2.07 # segundos 

# ave_fname = 'test.py'
# tiempo_total = 1.2 # segundos 

version = 'betaSinRuido_TEST_ajuste_GCR'

# T inicial y final en segundos de silabas que voy analisar y plotear

# silabas = {'B':[0.794424, 0.824770], 
#            'C':[0.969586,1.000902],
#            'D':[1.035681,1.108332]}

silabas = {'C':[0.969586, 1.000902]}

# silabas = {'a':[0.09, 0.9]}



# Parametros especificos del modelo
# ---------------------------------

# Parametros tracto vocal

f_rango = np.arange(1500, 6001, 500)
uoch_list = [f*f*40 for f in f_rango]
rdis_list = np.arange(3000, 25000, 5000)

# uoch_list = [360000000]
# rdis_list = [3000]

uolg =  1./1. # 1./1.

L =  0.036 # longitud tubo ( en m )

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
        if (alpha[i]<0):
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
            N = int((L /(350*dt))//1) # 350 vel sonido en aire. N: cantidad segmentos en las que divido el tubo.
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
            scaled = np.int16(sonido/np.max(np.abs(sonido)) * 32767 * 0.4434) # * 0.4434 Agrego factor de tamaño de la silaba.
            # write(f'{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r}_{nombre_ave}_SYN.wav', int(sampling_freq), scaled)
                    
            # Guardo salida de fuente.
            y_scaled = np.int16(y_out/np.max(np.abs(y_out)) * 32767 * 0.4434) # * 0.4434 Agrego factor de tamaño de la silaba.
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

            # Cargo BOS, fuente y SYN como npArray y conservo ademas los sampling rate
            rate_bos, BOS = read(nombre_BOS)
            rate_y , Y = sampling_freq, y_scaled
            rate_syn, SYN = sampling_freq, scaled
            
            BOS = np.array(BOS, dtype= 'float64')
            SYN = np.array(SYN, dtype= 'float64')
            
            # # Filtro BOS y SYN
            # BOS = denoisear(BOS, rate_bos)
            # SYN = denoisear(SYN, rate_syn)
        

            for silaba in silabas.items():
                 
                
                # Defino comienzo y fin de la silaba
                tin = silaba[1][0]
                tfin = silaba[1][1]
                silaba_id = silaba[0]
                
                
                
                
                ##### GUARDO AUDIO SYN #####
                write(f'/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/analisis_riquesa_espectral/{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r}_{nombre_ave}_SYN.wav', int(sampling_freq), scaled)
                

                
                # Calculo FFT de la sílaba de ineteres escala LOG
                frequencies_BOS, BOS_fft = array2fft(BOS, rate_bos, tin, tfin, log = True)
                frequencies_Y, Y_fft = array2fft(Y, rate_y, tin, tfin, log = True)
                frequencies_SYN, SYN_fft = array2fft(SYN, rate_syn, tin, tfin, log = True)
                
                # Calculo FFT de la sílaba de ineteres escala LINEAL
                frequencies_BOS, BOS_fft_lin = array2fft(BOS, rate_bos, tin, tfin, log = False)
                frequencies_Y, Y_fft_lin = array2fft(Y, rate_y, tin, tfin, log = False)
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
                
                
                # ----------
                # Ploteo FFT
                # ----------
                
                # Escala Log
                # fig, axs = plt.subplots(3, 1,sharex=True, sharey = True, figsize=(150, 70))    
                fig, axs = plt.subplots(3, 1, figsize=(110, 100))    

                
                fig.suptitle(f'{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r} \n chi2.Log_{round(chi2_log, 3)}    pearson.Log_{round(pearsonR_log, 3)}    spearman.Log_{round(spermanR_log, 3)}    kendal.Log_{round(kendalT_log, 3)}    infoM.Log_{round(infoM_log, 3)}    R2.Log_{round(R2_log, 3)} \n chi2.Lin_{round(chi2_lin, 3)}    pearson.Lin_{round(pearsonR_lin,3)}    spearman.Lin_{round(spermanR_lin, 3)}    kendal.Lin_{round(kendalT_lin, 3)}    infoM.Lin_{round(infoM_lin, 3)}    R2.Lin_{round(R2_lin, 3)} \n chi2.S_{round(chi2_s, 3)}    pearson.S_{round(pearsonR_s, 3)}    spearman.S_{round(spermanR_s, 3)}    kendal.S_{round(kendalT_s, 3)}    infoM.S_{round(infoM_s, 3)}    R2.S_{round(R2_s, 3)}')
                
                axs[0].plot(frequencies_BOS, BOS_fft)
                axs[0].plot(frequencies_SYN, SYN_fft, 'tab:green')
                #axs[0].set_title('BOS & SYN')
                axs[0].legend(['BOS FFT','SYN FFT'])
                
                #axs[0].set_yscale('log')
                
                axs[1].plot(frequencies_Y, abs(Y_fft), 'tab:orange')
                #axs[1].set_title('Y')
                axs[1].legend(['Fuente FFT'])
                #axs[1].set_yscale('log')
                
                # diff_BOS_SYN_FFT = abs(BOS_fft - SYN_fft)
                # axs[2].plot(frequencies_BOS, diff_BOS_SYN_FFT, 'tab:gray')
                # #axs[2].set_title('abs(BOS - SYN)')
                # axs[2].legend(['abs(BOS - SYN)'])
                # #axs[2].set_yscale('log')
                
                axs[2].plot(np.arange(len(BOS_chop))*1000/sampling_freq, BOS_chop)
                axs[2].plot(np.arange(len(SYN_chop))*1000/sampling_freq, SYN_chop, 'tab:green')
                #axs[2].set_title('abs(BOS - SYN)')
                axs[2].legend(['BOS sound', 'SYN sound'])
                #axs[2].set_yscale('log')
        
                axs[0].set_xlim([0,sampling_freq/2])
                axs[0].set_ylim([0,30])
                axs[0].set_xlabel('Frecuencias (Hz)')
                
                axs[1].set_xlim([0,sampling_freq/2])
                axs[1].set_ylim([0,30])
                axs[1].set_xlabel('Frecuencias (Hz)')
                
                axs[2].set_xlabel('ms')
                
                plt.savefig(f'/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/analisis_riquesa_espectral/{gamma}_silaba_{silaba_id}_{version}_C_{c}_R_{r}.pdf')
                #plt.show()
                plt.close()
                
                # plt.plot(BOS_chop)
                # plt.plot(SYN_chop)
                # print(xxx)
                
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
                
                c_resultados.append(c)
                r_resultados.append(r)
                gamma_resultados.append(gamma)

resultados = {'G': gamma_resultados, 
              'C': c_resultados, 
              'R': r_resultados,              
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
              'R2_s': R2_s_resultados}

# Genero tabla con todos los resultados
resultados = pd.DataFrame(resultados)


# ------------------------
# Busco mejores ajuste FFT 
# ------------------------

# Genero tabla resumen
resumen = resultados[resultados.Chi2_log == min(resultados.Chi2_log)] 
resumen = resumen.append(resultados[resultados.Pearson_log == max(resultados.Pearson_log)])
resumen = resumen.append(resultados[resultados.Spearman_log == max(resultados.Spearman_log)])       
resumen = resumen.append(resultados[resultados.Kendal_log == max(resultados.Kendal_log)])  
resumen = resumen.append(resultados[resultados.Info_Mutua_log == max(resultados.Info_Mutua_log)])
resumen = resumen.append(resultados[resultados.R2_log == max(resultados.R2_log)])  

resumen = resumen.append(resultados[resultados.Chi2_lin == min(resultados.Chi2_lin)])
resumen = resumen.append(resultados[resultados.Pearson_lin == max(resultados.Pearson_lin)])
resumen = resumen.append(resultados[resultados.Spearman_lin == max(resultados.Spearman_lin)])       
resumen = resumen.append(resultados[resultados.Kendal_lin == max(resultados.Kendal_lin)])  
resumen = resumen.append(resultados[resultados.Info_Mutua_lin == max(resultados.Info_Mutua_lin)])
resumen = resumen.append(resultados[resultados.R2_lin == max(resultados.R2_lin)])  

resumen = resumen.append(resultados[resultados.Chi2_s == min(resultados.Chi2_s)])
resumen = resumen.append(resultados[resultados.Pearson_s == max(resultados.Pearson_s)])
resumen = resumen.append(resultados[resultados.Spearman_s == max(resultados.Spearman_s)])       
resumen = resumen.append(resultados[resultados.Kendal_s == max(resultados.Kendal_s)])  
resumen = resumen.append(resultados[resultados.Info_Mutua_s == max(resultados.Info_Mutua_s)])
resumen = resumen.append(resultados[resultados.R2_s == max(resultados.R2_s)])  

# GUARDO todo en tabla resumen
resumen.to_csv('resumen.csv', header=True, decimal=',', sep=' ', float_format='%.3f')
resultados.to_csv('resultados.csv', header=True, decimal=',', sep=' ', float_format='%.3f')









