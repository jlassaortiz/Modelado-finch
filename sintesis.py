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
from scipy.signal import hilbert, savgol_filter

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
    dv[3]= - uolg*uoch*i1 - (rdis*uolg)*i2 + uolg*destimulodt
    dv[4]=0.
    
    return dv


def takens(v, dv):
    x = v[0]
    dv[0] = -(1/tau) * x + np.abs(hilb)
    
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


def find_envolvente(sonido): # tiene que ser un np.array
    
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




# Inicializo generador de números pseudo-random para poder replicar resultados
random.seed(1992)




# ----------------------
# Deficion de parametros
# ----------------------

# Nombre archivo donde se calculan las frecuencias fundamentales del canto
# -----------------------------------------------------------------------

# ave_fname = 'zf-JL016-NaVe.py'
# tiempo_total = 2.96 # segundos

ave_fname = 'AB010-bi.py'
tiempo_total = 2.07 # segundos

# ave_fname = 'bu49.py'
# tiempo_total = 1.048 # segundos

version = 'intento_1'
guardar_SYN = True
guardar_fuente = False


# Frecuencia y ventana temporal
# -----------------------------

sampling_freq = 44100 # Hz
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
uoch = 6724000
rdis = 400
uolg = 1.0
L    = 0.036 # Longitud tubo (en metros) (0.036)
coef_reflexion = - 0.35 # -0.35 
print(f'\nC: {uoch} \nR: {rdis} \nLg: {uolg} \n \nlargo_traquea: {L} \ncoef. reflexión: {coef_reflexion}')

# Condiciones iniciales
v = np.zeros(5)
v[0], v[1], v[2], v[3], v[4] = 0.01, 0.001, 0.001, 0.0001, 0.0001

# Tamaño del sistema de ecuaciones
n = 5 

# RUIDO: en todos los casos los parámetros son los SD de un ruido de dist normal con media = 0
ruido_beta = 0.02 # % del valor del máximo beta en este canto
ruido_alfa = 0.001 # % del valor del alfa necesario para fonar (-0.15)

print(f'\nruido beta: {ruido_beta} \nruido alfa: {ruido_alfa}')

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

# Calculo envolvente como en Boari 2015 ("automatic")
envolvente = find_envolvente(BOS)

# Calculo máximo de beta para usarlo para generar el ruido
beta_max = max(beta)


# ----------------------------------------------
# Calculamos Beta (a partir de las trazas de ff)
# ----------------------------------------------

# Abro el archivo b_w (mapa de betas - ff)
bes,was = np.loadtxt(mapa_b_w[0] ,unpack=True)

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

v_3 = [] # Salida del modelo

# Otras variables intermedias de la integracion que quizas quiera guardar
# x_out = []
y_out = []
# tiempo1 = []
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
    b = beta[i] + beta_max*random.normalvariate(0, ruido_beta) # La media del error es cero y el SD es ruido_beta
    destimulodt = (fil1[N-1]-fil1[N-2])/dt
    
    # Integracion
    t =i*dt
    rk4(ecuaciones,v,n,t,dt) # modifica v
     
    # Actualizo las siguientes variables (retro-propagación)
    estimulo=fil1[N-1]
    fil1[0]= v[1] + back1[N-1]
    back1[0]= coef_reflexion * fil1[N-1] 
    fil1[1:]=fil1[:-1]
    back1[1:]=back1[:-1]
    #feedback1=back1[N-1]

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

v_3 = np.asarray(v_3) /max(np.abs(v_3)) # es necesario para encontrar k que escalee correctamente y evitar errores

# Inicializo vector k para re-escaleo. 
# Este vector k multiplicado por la salida del modelo (v[3]) va a dar el 
# sonido final (cuya envolvente va a ser muy similar a la del BOS)
k = deepcopy(envolvente)
k = np.asarray(k)

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
scaled = np.int16(sonido/np.max(np.abs(sonido)) * 32767)
if guardar_SYN:
    write(f'{nombre_ave}_SYN_{version}_rBeta_{ruido_beta}_rAlfa_{ruido_alfa}_rAmp_{ruido_amplitud}.wav', int(sampling_freq), scaled)

# # Guardo salida de fuente.
y_scaled = np.int16(y_out/np.max(np.abs(y_out)) * 32767)
if guardar_fuente:
    write(f'{nombre_ave}_Y_{version}.wav', int(sampling_freq), y_scaled)




# -------
# Ploteos
# -------

fig, axs = plt.subplots(4, sharex=True)

i = 0
axs[i].plot(y_scaled, '-k')
axs[i].legend(['fuente'], loc = 'lower left')

i = i+1
axs[i].plot(v_3, 'tab:gray')
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

fig.suptitle(f'{nombre_ave}_Y_{version}.wav')

plt.show()


















    

