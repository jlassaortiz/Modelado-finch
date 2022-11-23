"""
Creado en Junio 2020

autor version original: Gabo Mindlin
autor de version actual: Javier Lassa Ortiz

Integrator with rk4, and tube with delays
It creates .wav

Estructura del codigo:
    - Importo librerias y seteo variables globales
    - Definicion de funciones
    - Definicion de parametros
    - Calculamos trazas de frecuencias fundamentales
    - Calculamos beta
    - Integracion
    - Escaleo amplitud de cada uno de los gestos de frecuencia
    - Guardo canto sintetico
    - Ploteo
"""


# --------------------------------------------
# Importo librerias y seteo variables globales
# --------------------------------------------

import random
import numpy as np
import matplotlib.pyplot as plt
     
from scipy.io.wavfile import write
from scipy.signal import resample

global alp
global b
global feedback1 
global estimulo1
global destimulodt1
global hilb
global tau

np.seterr(over='raise')

   
# -----------------------
# Definicion de funciones
# -----------------------

# Sistema de ecuaciones del modelo
# Se utiliza asi: rk4(ecuaciones,v,n,t,dt)
def ecuaciones(v, dv):
    i1,i2 = v
    dv[0]= i2
    dv[1]= - 1/(Ch*Lg)*i1 - (Rh/Lg)*i2 + (1/Lg)*destimulodt
    
    return dv

def ecuaciones_beak(v, dv):
    
    # Params PRE Sanz Perl 2011

    i1, i2, i3 = v
    dv[0] = i2
    dv[1] = - i1/(Lg*Ch) - Rh*i2*(1/Lb + 1/Lg) + i3*( 1/(Lg*Ch) - (Rb*Rh)/(Lb*Lg) ) + destimulodt/Lg + estimulo*Rh / (Lg*Lb)
    dv[2] = - Lg*i2/Lb - Rb*i3 / Lb + estimulo/Lb
  
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



def array2fft(npArray, samplingRate, log = False):
    
    n = len(npArray)
    
    # Calculo el Power Frequencies (ver documentacion de np.fft)
    npArray_fft = np.absolute(np.fft.fft(npArray))**2

    # Saco frecuencias negativas (mitad superior del array. Ver documentacion np.fft)
    npArray_fft = npArray_fft[range(int(n/2))]

    # Paso a escala log
    if log:
        npArray_fft = np.log(npArray_fft, where=(npArray_fft != 0))  
    
    # Genero vector de Frecuencias (conservo solo las positivas)
    frequencies = np.fft.fftfreq(n , d = 1/samplingRate)
    frequencies = frequencies[range(int(n/2))] 
    
    return frequencies, npArray_fft


def sliding_window(signal, window_size, step):
    
    signal_out = []
    
    i = int(0)
    window_size = int(window_size)
    step = int(step)
    
    while i + window_size < len(signal):
        signal_out.append( np.mean( signal[ i : i + window_size] ) )
        i = i + step
        
    return signal_out


def calc_w(c):
    w = 1/(np.sqrt(c) * 2*np.pi)
    return w

def calc_c(w):
    c = 1/(2*np.pi * w)**2
    return c

# Inicializo generador de números pseudo-random para poder replicar resultados
random.seed(1992)




# ----------------------
# Deficion de parametros
# ----------------------

# 
# -----------------------------------------------------------------------

version = 'white_noise_beak-A'
guardar = False # guardo entrada y salida del filtro

# Frecuencia y ventana temporal
# -----------------------------

sampling_freq = 44100 # Hz
dt = 1/sampling_freq
print(f'\nsampling freq: {sampling_freq}')

tiempo_total = 5.0

# Parametros del modelo
# ---------------------

# Parametros tracto vocal (filtro)
Ch = (1.5 * 1e-8) / 350 # calc_c(2000)*(1.0 **2) # / 1.0 # Capacitancia Helmholtz
Lg = 20 # 1.0 # Inductancia glotis Helmholtz
Rh = 1000 # 5000 # Resistencia disipación Helmholtz

L  = np.round(0.036 * 1.0 , 3) # Longitud tubo (en metros) (0.036)
coef_reflexion = -0.95 # -0.35 
print(f'\nC: {Ch:.2e}  \nR: {Rh} \nLg: {Lg} \n \nlargo_traquea: {L} \ncoef. reflexión: {coef_reflexion}')

# Coef sans perl 2011
Lb = 1000
Rb = 100000
    

# Condiciones iniciales
v = np.zeros(3)
v[0], v[1], v[2] =  0.001, 0.0001, 0.0001


# Tamaño del sistema de ecuaciones
n = 3


# -----------
# Integracion
# -----------

noise_in = [] # entrada filtro
noise_out = [] # salida filtro

# Otras variables intermedias de la integracion que quizas quiera guardar
# tiempo = []
# forzado_out = []
# dforzadodt1 = []
# elbeta1 = []

# Retro-propagación
N = int((L /(350*dt) ) // 1) # 350 velocidad sonido en el aire
fil1 = np.zeros(N)
back1 = np.zeros(N)
# feedback1 = 0


# Integro
# -------

for i in range(np.int(tiempo_total*sampling_freq)):
    
    noise = np.random.normal(-1.0, 1.0)
    
    # Parametros dependientes del tiempo del sistema de ecuaciones
    destimulodt = (fil1[N-1]-fil1[N-2])/dt
    estimulo=fil1[N-1]

    # Integracion
    t =i*dt
    v.astype('float64')
    rk4(ecuaciones_beak,v,n,t,dt) # modifica v
     
    # Actualizo las siguientes variables (retro-propagación)
    fil1[0]= noise + back1[N-1]
    back1[0]= coef_reflexion * fil1[N-1] 
    fil1[1:]=fil1[:-1]
    back1[1:]=back1[:-1]
    #feedback1=back1[N-1]

    # Guardo salida del modelo (falta escalearla con la envolvente)
    noise_in.append(noise)
    noise_out.append(v[2])
  
    
  
# noise_in_resample =  resample(noise_in, int(tiempo_total*44100))
# noise_out_resample = resample(noise_out, int(tiempo_total*44100))
# sampling_freq = 44100
# noise_in = noise_in_resample
# noise_out = noise_out_resample

# ----------------------
# Guardo canto sintetico
# ----------------------

# Guardo el SYN en formato 16-bit
# ver documentación de scipy.io.wavfile.read y scipy.io.wavfile.write 
out_scaled = np.int16(noise_out/np.max(np.abs(noise_out)) * 32767)
in_scaled = np.int16(noise_in/np.max(np.abs(noise_in)) * 32767)

out_scaled = np.int16(noise_out/np.max(np.abs(noise_out)) * 32767)
in_scaled = np.int16(noise_in/np.max(np.abs(noise_in)) * 32767)

if guardar:
    write(f'OUT_{version}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}.wav', int(sampling_freq), out_scaled)
    write(f'IN_{version}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}.wav', int(sampling_freq), in_scaled)




# Calculo el fft del BOS, SYN y fuente

freq_in, fft_in = array2fft(noise_in, sampling_freq, log = True)
freq_out, fft_out = array2fft(noise_out, sampling_freq, log = True)

Hz_ventana = 100
Hz_step = 10

# "suavizo" la fft 
ws = len(fft_in)* Hz_ventana /max(freq_in)
step = len(fft_in)* Hz_step /max(freq_in)
fft_in_smooth = sliding_window(fft_in, ws, step)
freq_in_smooth = sliding_window(freq_in, ws, step)

ws = len(fft_out)* Hz_ventana /max(freq_out)
step = len(fft_out)* Hz_step /max(freq_out)
fft_out_smooth = sliding_window(fft_out, ws, step)
freq_out_smooth = sliding_window(freq_out, ws, step)

# -------
# Ploteos
# -------

# SONIDO
fig, axs = plt.subplots(2, sharex=True, figsize=(12,9))

i = 0
axs[i].plot(noise_in, 'tab:orange')
axs[i].legend(['entrada'], loc = 'lower left')

i = i+1
axs[i].plot(noise_out)
axs[i].legend(['v[3]'], loc = 'lower left')

fig.suptitle(f'IN-OUT_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}')
plt.show()



# FFT
plt.figure(figsize=([16, 4]))
plt.plot(freq_out, fft_out)
plt.plot(freq_in, fft_in, ':r', alpha=0.4)
plt.legend(['out FFT','in FFT'])
plt.xlim([0,20000])
plt.xlabel('Frecuencias (Hz)')
plt.title(f'FFT-IN-OUT_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}')



# FFT SUAVIZADO
plt.figure(figsize=([16, 4]))
plt.plot(freq_out_smooth, fft_out_smooth)
plt.plot(freq_in_smooth,fft_in_smooth, 'r', alpha=0.4)
plt.legend(['out FFT_smooth','in FFT_smooth'])
plt.xlim([0,20000])
plt.xlabel('Frecuencias (Hz)')
plt.ylabel('power')
plt.title(f'FFT_SMOOTH-IN-OUT_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}')
