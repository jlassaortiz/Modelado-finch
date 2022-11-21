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

import glob
import random
import numpy as np
import matplotlib.pyplot as plt

from copy import deepcopy
from scipy.io.wavfile import write, read
from scipy.signal import hilbert, savgol_filter, resample

global alp
global b
global estimulo
global destimulodt
global hilb
global tau

np.seterr(over='raise')


# -----------------------
# Definicion de funciones
# -----------------------

# Sistema de ecuaciones del modelo
# Se utiliza asi: rk4(ecuaciones,v,n,t,dt)
def ecuaciones(v, dv):
    x ,y,i1,i2,i3 = v
    dv[0]=y
    dv[1]= gamma*gamma*alp+ b *gamma*gamma*x-gamma*gamma*x*x*x-gamma*x*x*y+gamma*gamma*x*x-gamma*x*y
    dv[2]= i2
    
    # dv[3]=-uolg*Ch*i1-(Rh*uolb+Rh*uolg)*i2+(uolg*Ch-Rh*rb*uolg*uolb)*i3+uolg*destimulodt+Rh*uolg*uolb*estimulo
    # dv[4]=-(uolb/uolg)*i2-rb*uolb*i3+uolb*estimulo
    
    
    # Ecuaciones PRE 2011 (igual que las de arriba con pico pero mas legibles)
    
    dv[3] = - i1/(Lg*Ch) - Rh*i2*(1/Lb + 1/Lg) + i3*( 1/(Lg*Ch) - (Rb*Rh)/(Lb*Lg) ) + destimulodt/Lg + estimulo*Rh / (Lg*Lb)
    dv[4] = - Lg*i2/Lb - Rb*i3 / Lb + estimulo/Lb
    return dv

# Integrador RK4
def rk4(dv,v,n,dt): #  dv es la funcion ecuaciones()
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
def expo(ti,tf,wi,wf,frequencias, silabas_timestamp):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]=wf+(wi-wf)*np.exp(-3*(t-ti)/((tf-ti)))
        alpha[i+k]= -0.150 + 0.150*random.normalvariate(0, ruido_alfa) # alpha suficiente para fonar

    silabas_timestamp.append(i)
    silabas_timestamp.append(j)

    return frequencias, silabas_timestamp


def rectas(ti,tf,wi,wf,frequencias, silabas_timestamp):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]= wi + (wf-wi)*(t-ti)/(tf-ti)
        alpha[i+k]= -0.150 + 0.150*random.normalvariate(0, ruido_alfa) # alpha suficiente para fonar

    silabas_timestamp.append(i)
    silabas_timestamp.append(j)

    return frequencias, silabas_timestamp


def senito(ti,tf,media,amplitud,alphai,alphaf,frequencias, silabas_timestamp):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t = ti+k*dt
        frequencias[i+k]= media + amplitud * np.sin(alphai+(alphaf-alphai)*(t-ti)/(tf-ti))
        alpha[i+k]= -0.150 + 0.150*random.normalvariate(0, ruido_alfa) # alpha suficiente para fonar

    silabas_timestamp.append(i)
    silabas_timestamp.append(j)

    return frequencias,silabas_timestamp



def find_envolvente(sonido, sf): # tiene que ser un np.array

    paso = 1/sf

    # Calculo transformada de Hilbert
    envolvente_h = hilbert(sonido)

    # Integro para suavizar
    envolvente_int = []

    e = [0.0]

    for i in range(np.int(tiempo_total/(paso))):

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

        dt2=paso/2.0
        dt6=paso/6.0

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
            v1[x]=e[x]+paso*k3[x]

        xi = v1[x]
        k4[x] = -(1/tau) * xi + np.abs(hilb)

        for x in range(0, n):
            v1[x]=e[x]+paso*k4[x] #parece al pedo este paso

        for x in range(0, n):
            e[x]=e[x]+dt6*(2.0*(k2[x]+k3[x])+k1[x]+k4[x])

        envolvente_int.append(e[0])

    # Aplico filtro Savitzky-Golay
    envolvente = savgol_filter(envolvente_int, 513, 4)

    return envolvente



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

# Nombre archivo donde se calculan las frecuencias fundamentales del canto
# -----------------------------------------------------------------------

# ave_fname = 'segmentobk93.py' # Nature
# tiempo_total = 0.49 # segundos

ave_fname = '040-AmaNe.py'
tiempo_total = 3.68 # segundos

# ave_fname = '028-ViVe.py'
# tiempo_total = 3.20 # segundos

# ave_fname = '026-BN.py'
# tiempo_total = 2.25 # segundos

# ave_fname = 'zf-JL016-NaVe.py'
# tiempo_total = 2.96 # segundos

# ave_fname = 'AB010-bi.py'
# tiempo_total = 2.07 # segundos

# ave_fname = 'bu49.py'
# tiempo_total = 1.048 # segundos


# version = 'Nature-HS' # Este numero se usa para el nombre del archivo wav que se guarda
guardar_SYN  = True
guardar_fuente = False

# Frecuencia y ventana temporal
# -----------------------------

sampling_freq = 44100 * 20# Hz
dt = 1/sampling_freq
print(f'\nsampling freq: {sampling_freq}')


# Parametros del modelo
# ---------------------

# Parámetros de la fuente de sonido
mapa_b_w = glob.glob('*.txt') # Mapa b_w para determinado gamma
gamma = int(mapa_b_w[0][4:9]) # determino el gamma del nombre del archivo del mapa
print(f'\nmapa: {mapa_b_w[0]} \ngamma: {gamma}')

alpha = np.zeros(np.int(tiempo_total/(dt))) # Inicializo los parametros de control
beta = np.zeros(np.int(tiempo_total/(dt))) # Inicializo los parametros de control

for i in range(np.int(tiempo_total/(dt))):
    alpha[i] = 0.15 # sistema no fona en este valor
    beta[i]  = 0.15 # sistema no fona en este valor

# Parametros tracto vocal (filtro)
Ch = (3.0 * 1e-8) / 350 # calc_c(2000)*(1.0 **2) # / 1.0 # Capacitancia Helmholtz
Lg = 60 # 1.0 # Inductancia glotis Helmholtz
Rh = (100/2)*10000 # 5000 # Resistencia disipación Helmholtz

L  = np.round(0.036 * 1.0 , 3) # Longitud tubo (en metros) (0.036)
coef_reflexion = -0.1 # -0.35 
print(f'\nC: {Ch:.2e}  \nR: {Rh} \nLg: {Lg} \n \nlargo_traquea: {L} \ncoef. reflexión: {coef_reflexion}')

# Coef sans perl 2011
Lb = 1e4
Rb = (0.5)*1e7

version = 'nature-params_HS_r-01' # Este numero se usa para el nombre del archivo wav que se guarda


# Condiciones iniciales
v = np.zeros(5)
v[0], v[1], v[2], v[3], v[4] = 0.01, 0.001, 0.001, 0.0001, 0.0001


# Tamaño del sistema de ecuaciones
n = 5

# RUIDO: en todos los casos los parámetros son los SD de un ruido de dist normal con media = 0
ruido_beta = 0.04 # % del valor del beta
ruido_alfa = 0.005 # % del valor del alfa necesario para fonar (-0.15)
ruido_amplitud = 0.0 # % del valor de la amplitud maxima de la envolvente

print(f'\nruido beta: {ruido_beta} \nruido alfa: {ruido_alfa} \nruido amplitud: {ruido_amplitud}')

# ------------------------------------------------------------
# Calculamos trazas de frecuencias fundamentales y envolventes
# ------------------------------------------------------------

# Inicializo las frecuencias fundamentales y time_stamps de los gestos de ff
frequencias = np.zeros(np.int(tiempo_total * sampling_freq))
silabas_timestamp = []

# Corro scritp que genera la traza de ff
nombre_ave = '' #inicializo  pq es una variable q se define en otro script y sino me saltan carteles de error
nombre_BOS = '' #inicializo  pq es una variable q se define en otro script y sino me saltan carteles de error
with open(ave_fname) as f:
    code = compile(f.read(), ave_fname, 'exec')
    exec(code)

# Cargo el BOS
rate_bos, BOS = read(nombre_BOS)

# Calculo envolvente como en Boari 2015 ("automatic")
envolvente = find_envolvente(BOS, rate_bos)
envolvente = resample(envolvente, np.int(tiempo_total/(dt)))


# ----------------------------------------------
# Calculamos Beta (a partir de las trazas de ff)
# ----------------------------------------------

# Abro el archivo b_w (mapa de betas - ff)
bes,was = np.loadtxt(mapa_b_w[0] ,unpack=True)

# Ajustamos was vs bes a un polinomio de grado 6
# z es una lista de los coeficientes del polinomio ajustado
z = np.polyfit(was, bes, 6)

# Generamos objeto p, que es un polinomio (es z, hecho objeto)
p = np.poly1d(z)

# Calculamos beta como resultado de valuar p() en frecuencias fundamentales
for i in range(np.int(tiempo_total/(dt))):
    # if se cumple siempre que aplique senito(), recta() o exp()
    # es decir: si el sistema esta fonando
    if(alpha[i]<0):
        # beta es el polinomio p valuado en frecuencias[i]
        beta[i] = p(frequencias[i])

# Calculo máximo de beta para usarlo para generar el ruido
beta_max = np.max(np.abs(beta)) # no veo que se use en el código, se puede borrar?

# -----------
# Integracion
# -----------

v_3 = [] # Salida del modelo

# Otras variables intermedias de la integracion que quizas quiera guardar
# x_out = []
y_out = []
# tiempo = []
# forzado_out = []
# dforzadodt1 = []
# elbeta1 = []

# Retro-propagación
N = int((L /(350*dt))//1) # 350 velocidad sonido en el aire
fil1 = np.zeros(N)
back1 = np.zeros(N)
# feedback1 = 0


# Integro
# -------

for i in range(np.int(tiempo_total/(dt))):

    # Parametros dependientes del tiempo del sistema de ecuaciones (Variables globales ¿es necesario?)
    alp = alpha[i]
    b = beta[i]*(1+random.normalvariate(0., ruido_beta))
    destimulodt = (fil1[N-1]-fil1[N-2])/dt
    
    estimulo=fil1[N-1]

    # Integracion
    # t =i*dt
    v.astype('float64')
    rk4(ecuaciones,v,n,dt) # modifica v

    # Actualizo las siguientes variables (retro-propagación)
    fil1[0]= v[1] + back1[N-1]
    back1[0]= coef_reflexion * fil1[N-1]
    fil1[1:]=fil1[:-1]
    back1[1:]=back1[:-1]

    # Guardo salida del modelo (falta escalearla con la envolvente)
    v_3.append(v[4])

    # Guarda otras variables de interes de la integracion
    # x_out.append(v[0])
    y_out.append(v[1]) # Salida de la fuente!
    # tiempo.append(t)
    # dforzadodt1.append(destimulodt)
    # elbeta1.append(beta[i])




# --------------------------------------------------------
# Escaleo amplitud de cada uno de los gestos de frecuencia
# --------------------------------------------------------

v_3 = np.asarray(v_3) /max(np.abs(v_3)) # es necesario para encontrar k que escalee correctamente y evitar errores

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

# Ver la documentacion de: scipy.io.wavfile.write

# Genero factor para que el volumen de SYN sea igual al del BOS
escala = np.max(np.abs(BOS))
if BOS.dtype == 'float32':
    escala = escala / 1
elif BOS.dtype == 'int32':
    escala = escala / 2147483647
elif BOS.dtype == 'int16':
    escala = escala / 32767
elif BOS.dtype == 'uint8':
    escala = escala / 25

# Guardo el SYN en formato 16-bit
# ver documentación de scipy.io.wavfile.read y scipy.io.wavfile.write
scaled = np.int16(sonido/np.max(np.abs(sonido)) * escala * 32767)

if guardar_SYN:
    # write(f'{nombre_ave}_SYN_{version}_rBeta_{ruido_beta}_rAlfa_{ruido_alfa}_rAmp_{ruido_amplitud}.wav', int(sampling_freq), scaled)
    write(f'{nombre_ave}_SYN_v-{version}_G_{gamma}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}_rBeta_{ruido_beta}_rAlpha_{ruido_alfa}_rAmpl_{ruido_amplitud}.wav', int(sampling_freq), scaled)

# Guardo salida de fuente.
y_scaled = np.int16(y_out/np.max(np.abs(y_out)) * 32767)

if guardar_fuente:
    write(f'{nombre_ave}_Y_{version}.wav', int(sampling_freq), y_scaled)




# Calculo el fft del BOS, SYN y fuente

freq_BOS, fft_BOS = array2fft(BOS, rate_bos, log = True)
freq_SYN, fft_SYN = array2fft(scaled, sampling_freq, log = True)
freq_fuente, fft_fuente= array2fft(y_scaled, sampling_freq, log = True)

Hz_ventana = 100
Hz_step = 10

# "suavizo" la fft
ws = len(fft_BOS)* Hz_ventana /max(freq_BOS)
step = len(fft_BOS)* Hz_step /max(freq_BOS)
fft_BOS_smooth = sliding_window(fft_BOS, ws, step)
freq_BOS_smooth = sliding_window(freq_BOS, ws, step)

ws = len(fft_SYN)* Hz_ventana /max(freq_SYN)
step = len(fft_SYN)* Hz_step /max(freq_SYN)
fft_SYN_smooth = sliding_window(fft_SYN, ws, step)
freq_SYN_smooth = sliding_window(freq_SYN, ws, step)

ws = len(fft_fuente)* Hz_ventana /max(freq_fuente)
step = len(fft_fuente)* Hz_step /max(freq_fuente)
fft_fuente_smooth = sliding_window(fft_fuente, ws, step)
freq_fuente_smooth = sliding_window(freq_fuente, ws, step)

# -------
# Ploteos
# -------

fig, axs = plt.subplots(4, sharex=True, figsize=(12,9))

i = 0
axs[i].plot(y_scaled, '-k')
axs[i].legend(['fuente'], loc = 'lower left')

i = i+1
axs[i].plot(v_3, 'tab:gray')
axs[i].plot(k/max(k))
axs[i].legend(['v[3]'], loc = 'lower left')

# i = i+1
# axs[i].plot(k, 'tab:orange')
# axs[i].legend(['k'], loc = 'lower left')

i = i+1
axs[i].plot(sonido, 'tab:orange')
axs[i].plot(envolvente, 'tab:red')
axs[i].plot(-envolvente, 'tab:red')
axs[i].legend(['SYN', 'envolvente_BOS'], loc = 'lower left')

# i = i+1
# axs[i].plot(sonido/max(sonido), 'tab:orange')
# axs[i].plot(envolvente/max(envolvente), 'tab:red')
# axs[i].legend(['sonido_norm', 'envolvente_norm'], loc = 'lower left')

i = i+1
axs[i].plot(BOS/max(BOS))
axs[i].plot(envolvente/max(envolvente), 'tab:red')
axs[i].plot(-envolvente/max(envolvente), 'tab:red')
axs[i].legend(['BOS_norm', 'envolvente_BOS_norm'], loc = 'lower left')

fig.suptitle(f'{nombre_ave}_SYN_G_{gamma}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}_rBeta_{ruido_beta}_rAlpha_{ruido_alfa}_rAmpl_{ruido_amplitud}')

plt.show()


# FFT bos, syn, fuente
plt.figure(figsize=([16, 4]))
plt.plot(freq_BOS, fft_BOS)
plt.plot(freq_SYN, fft_SYN, 'tab:green')
plt.plot(freq_fuente, fft_fuente, ':r', alpha=0.2)
plt.legend(['BOS FFT','SYN FFT', 'Fuente FFT'])
plt.xlim([0,20000])
plt.xlabel('Frecuencias (Hz)')

fig.suptitle(f'{nombre_ave}_SYN_G_{gamma}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}_rBeta_{ruido_beta}_rAlpha_{ruido_alfa}_rAmpl_{ruido_amplitud}')


# FFT bos, syn, fuente SUAVE
plt.figure(figsize=([16, 4]))
plt.plot(freq_BOS_smooth, fft_BOS_smooth)
plt.plot(freq_SYN_smooth, fft_SYN_smooth, 'tab:green')
plt.plot(freq_fuente_smooth, fft_fuente_smooth, ':r', alpha=0.2)
plt.legend(['BOS FFT SMOOTH','SYN FFT SMOOTH', 'Fuente FFT SMOOTH'])
plt.xlim([0,20000])
plt.xlabel('Frecuencias (Hz)')

plt.title(f'{nombre_ave}_SYN_G_{gamma}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}_rBeta_{ruido_beta}_rAlpha_{ruido_alfa}_rAmpl_{ruido_amplitud}')


# FFT bos
plt.figure(figsize=([16, 4]))
plt.plot(freq_BOS, fft_BOS,'-k')
plt.plot(freq_BOS_smooth, fft_BOS_smooth, '-')
plt.legend(['BOS FFT','BOS FFT SMOOTH'])
plt.xlim([0,20000])
plt.xlabel('Frecuencias (Hz)')

plt.title(f'{nombre_ave}_SYN_G_{gamma}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}_rBeta_{ruido_beta}_rAlpha_{ruido_alfa}_rAmpl_{ruido_amplitud}')


# FFT syn
plt.figure(figsize=([16, 4]))
plt.plot(freq_SYN, fft_SYN,'-k')
plt.plot(freq_SYN_smooth, fft_SYN_smooth, 'tab:green')
plt.legend(['SYN FFT','SYN FFT SMOOTH'])
plt.xlim([0,20000])
plt.xlabel('Frecuencias (Hz)')

plt.title(f'{nombre_ave}_SYN_G_{gamma}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}_rBeta_{ruido_beta}_rAlpha_{ruido_alfa}_rAmpl_{ruido_amplitud}')


# FFT fuente
plt.figure(figsize=([16, 4]))
plt.plot(freq_fuente, fft_fuente,'-k')
plt.plot(freq_fuente_smooth, fft_fuente_smooth, 'tab:orange')
plt.legend(['FUENTE FFT','FUENTE FFT SMOOTH'])
plt.xlim([0,20000])
plt.xlabel('Frecuencias (Hz)')

plt.title(f'{nombre_ave}_SYN_G_{gamma}_C_{Ch:.2e}_R_{Rh}_Lg_{Lg}_Ltraquea_{L}_coefReflex_{coef_reflexion}_rBeta_{ruido_beta}_rAlpha_{ruido_alfa}_rAmpl_{ruido_amplitud}')
