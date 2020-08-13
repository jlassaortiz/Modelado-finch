#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:39:05 2020

@author: javi_lassaortiz

Análisis riqueza espectral

"""
import numpy as np     	
from scipy.io.wavfile import write, read
import random
#from scipy import signal
import matplotlib.pyplot as plt
import glob
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



# ----------------------
# Deficion de parametros
# ----------------------

# Nombre archivo donde se calculan las frecuencias fundamentales del canto
# -----------------------------------------------------------------------

ave_fname = 'AB010-bi.py'
tiempo_total = 2.07 # segundos


# ave_fname = 'bu49.py'
# tiempo_total = 1.048 # segundos

version = 'betaSinRuido_mapa_javi_1'

# T inicial y final en segundos de silabas que voy analisar y plotear
silabas = {'B':[0.794424, 0.824770], 
           'C':[0.969586,1.000902],
           'D':[1.035681,1.108332]}


# Parametros especificos del modelo
# ---------------------------------

# Parametros tracto vocal
uoch = 40*2700*2700 # 40*2700*2700
rdis = 5000/1.0 # 5000/1.0

uolg =  1./1. # 1./1.

# No se lo que es
L =  0.036 # No se que es !!! =  longitud tubo (charla con Camilo) 
# L =  0.025

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

# Lista con nombres de mapas b_w para para gamma
lista_mapas_b_w = glob.glob('/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/mapas_b_w/*.txt')




# Hago lista de valores de gamma de cada mapa
gammas = []
for mapa_fn in tqdm(lista_mapas_b_w):
    gamma = int(mapa_fn[86:91])
    gammas.append(gamma)
    
    
    
    # Abro el archivo b_w (re)
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
       
        
        # Actualizo las siguientes variables (?) 
        estimulo=fil1[N-1]
        fil1[0]= v[1] + back1[N-1]
        back1[0]=-0.35*fil1[N-1] #-0.35 coef de reflexion  
        fil1[1:]=fil1[:-1]
        back1[1:]=back1[:-1]
        #feedback1=back1[N-1]
    
    
        # Guardo resultado de integracion v[3] en sonido
        sonido.append(v[3]*amplitudes[i])
        
        
        # Guarda variables de interes de la integracion
        # no esta chequeado que ande
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
    write(f'{gamma}_{nombre_ave}_SYN_{version}.wav', int(sampling_freq), scaled)
    
    # Guardo salida de fuente.
    y_scaled = np.int16(y_out/np.max(np.abs(y_out)) * 32767)
    write(f'{gamma}_{nombre_ave}_Y_{version}.wav', int(sampling_freq), y_scaled)
    
    
    
    # -------
    # Ploteos
    # -------
    
    '''
    # Ploteo espectrograma del sonido
    # -------------------------------
    
    f, t, Sxx = signal.spectrogram(sonido, 44100, window=('gaussian',20*128),nperseg=10*1024,noverlap=18*512,scaling='spectrum')
    Sxx = np.clip(Sxx, a_min=np.amax(Sxx)/10**3, a_max=np.amax(Sxx))
    
    plt.pcolormesh(t,f,np.log10(Sxx),rasterized=True,cmap=plt.get_cmap('Greys'))
    #plt.pcolormesh(t,f,Sxx,cmap=plt.get_cmap('Greys'))
    plt.ylim(10,10000)
    #plt.ylabel('Frequency [Hz]')
    #plt.xlabel('Time [sec]')
    plt.axis('off')
    #plt.savefig('sonograma_{}.jpeg'.format(n_canto), dpi=50, facecolor='w', edgecolor='w',
                #orientation='portrait', papertype=None, format=None,
                #transparent=False, bbox_inches=None, pad_inches=0.1,
                #frameon=None)
    plt.show()
    '''
    
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
               
        # Defino comienzo y fin de la silaba
        ti = silaba[1][0]
        tf = silaba[1][1]
        silaba_id = silaba[0]
        
        # Conservo solo la parte del canto de interes
        BOS = BOS[int(ti*rate_bos):int(tf*rate_bos)]
        Y = Y[int(ti*rate_syn):int(tf*rate_syn)]
        SYN = SYN[int(ti*rate_syn):int(tf*rate_syn)]
               
        # Calculo fft
        BOS_fft = np.fft.fft(BOS) /len(BOS)
        Y_fft = np.fft.fft(Y) / len(Y)
        SYN_fft = np.fft.fft(SYN) /len(SYN)
        
        # No se bien porque pero necesito sacar las frecuencias de la mitad superior
        BOS_fft = BOS_fft[range(int(len(BOS)/2))]
        Y_fft = Y_fft[range(int(len(Y)/2))]
        SYN_fft = SYN_fft[range(int(len(SYN)/2))]
        
        
        # Hago vector de frecuencias para poder graficar
        tpCount     = len(BOS)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/rate_bos
        frequencies_BOS = values/timePeriod
        
        tpCount     = len(Y)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/rate_y
        frequencies_Y = values/timePeriod
        
        tpCount     = len(SYN)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/rate_syn
        frequencies_SYN = values/timePeriod
        
        
        # ----------
        # Ploteo FFT
        # ----------
        
        # Escala Log
        fig, axs = plt.subplots(3, 1,sharex=True, figsize=(60, 20))    
        
        fig.suptitle(f'{gamma}_silaba_{silaba_id}_{version}')
        
        axs[0].plot(frequencies_BOS, abs(BOS_fft))
        axs[0].set_title('BOS')
        axs[0].set_yscale('log')
        
        axs[1].plot(frequencies_Y, abs(Y_fft), 'tab:orange')
        axs[1].set_title('Y')
        axs[1].set_yscale('log')
        
        axs[2].plot(frequencies_SYN, abs(SYN_fft), 'tab:green')
        axs[2].set_title('SYN')
        axs[2].set_yscale('log')

        axs[2].set_xlim([0,10000])
        axs[2].set_xlabel('Frecuencias (Hz)')
        
        plt.savefig(f'/Users/javi_lassaortiz/Documents/LSD/Modelado cuarentena/Modelado-finch/analisis_riquesa_espectral/{gamma}_silaba_{silaba_id}.pdf')
        plt.show()
        #plt.close()
        


