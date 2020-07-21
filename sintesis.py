"""
Creado en Junio 2020

autor version original: Gabo Mindlin
autor de version actual: Javier Lassa Ortiz

Integrator with rk4, and tube with delays
It creates .wav

Estructura del codigo:
    - Definicion de funciones
    - Definicion de parametros
    - Integracion
    - Guardo canto sintetico

"""

import numpy as np     	
from scipy.io.wavfile import write
import random
#from scipy import signal
import matplotlib.pyplot as plt

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
        alpha[i+k]=-0.150 # alpha suficiente para fonar
        #alpha[i+k]=-0.125
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) * (1+random.normalvariate(0.,.4)) +factor/10 * (1+random.normalvariate(0.,.02))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) * (1+random.normalvariate(0.,.2)) +factor/10 * (1+random.normalvariate(0.,.01))
    return frequencias,amplitudes


def rectas(ti,tf,wi,wf,factor,frequencias,amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]= wi + (wf-wi)*(t-ti)/(tf-ti) 
        alpha[i+k]=-0.150 # alpha suficiente para fonar
        #alpha[i+k]=-0.125
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.4))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.2))
    return frequencias,amplitudes


def senito(ti,tf,media,amplitud,alphai,alphaf,factor,frequencias, amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t = ti+k*dt
        frequencias[i+k]=media+amplitud*np.sin(alphai+(alphaf-alphai)*(t-ti)/(tf-ti))
        alpha[i+k]=-0.150 # alpha suficiente para fonar
        #alpha[i+k]=-0.125  
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.2))
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.1))
    return frequencias,amplitudes



# ----------------------
# Deficion de parametros
# ----------------------

# Nombre archivo de parámetros específicos del ave
# ------------------------------------------------

ave_fname = 'AB010-bi.py'



# Parametros especificos del modelo
# ---------------------------------

gamma = 12300 #12500

# Parametros tracto vocal
uoch = 40*2700*2700 # 40*2700*2700
uolg =  1./1. # 1./1.
rdis = 5000/1.0 # 5000/1.0

v = np.zeros(5)
v[0], v[1], v[2], v[3], v[4] =0.01,0.001,0.001, 0.0001, 0.0001

L =  0.036 # No se que es !!!
# L =  0.025



# Cargo los parametros especificos del canto
# ------------------------------------------

# Cargo datos básicos del canto y genero trazas de frec fundamental

with open(ave_fname) as f:
    code = compile(f.read(), ave_fname, 'exec')
    exec(code)





# ---------------
# Calculamos Beta
# ---------------

# Abro el archivo b_w (re)
bes,was = np.loadtxt('b_w_12300.txt',unpack=True)
print('bes:', bes[0])
print('was:',was[0])

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
N = int((L /(350*dt))//1)
fil1 = np.zeros(N)
back1 = np.zeros(N)
# feedback1 = 0

# Integro
for i in range(np.int(tiempo_total/(dt))):
    
    # Parametros dependientes del tiempo del sistema de ecuaciones
    # Variables globales ¿es necesario que asi lo sean?
    alp=alpha[i]
    #b=beta[i]*(1+random.normalvariate(0.,.3))
    b=beta[i]*(1+random.normalvariate(0.,.2)) 
    destimulodt = (fil1[N-1]-fil1[N-2])/dt
    
    # Integracion
    t =i*dt
    rk4(ecuaciones,v,n,t,dt) # modifica v
   
    
    # Actualizo las siguientes variables ?   
    estimulo=fil1[N-1]
    fil1[0]= v[1] + back1[N-1]
    back1[0]=-0.35*fil1[N-1]
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
  
   
#sonido = [s*1000 for s in sonido]
#s_max = max([abs(max(sonido)), abs(min(sonido))])
#sonido = [s + s_max*random.normalvariate(0.,.001) for s in sonido]
sonido = np.asarray(sonido)



# ----------------------
# Guardo canto sintetico
# ----------------------

# Este paso es necesario para que el archivo wav se guarde correctamente
# Ver la documentacion de: scipy.io.wavfile.write
#scaled = np.int16(sonido/np.max(np.abs(sonido)) * 32767)
scaled = np.int16(sonido/np.max(np.abs(sonido)) * 15000)

write('sintesis_finch_uolg_30.wav', 44100, scaled)

# Guardo salida de fuente.
y_scaled = np.int16(y_out/np.max(np.abs(y_out)) * 32767)
write('y_alpha.wav', 44100, y_scaled)



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

plt.plot(sonido/np.max(np.abs(sonido)) + 6, label= 'sonido')
plt.plot(x_out/np.max(np.abs(x_out)) + 4 ,label = 'x')
plt.plot(y_out/np.max(np.abs(y_out)) + 2, label = 'y')
plt.plot(forzado_out/np.max(np.abs(forzado_out)) , label = 'forzado')
plt.legend()




    























    

