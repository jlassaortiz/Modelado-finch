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
# modifica alpha para que fone el sistema y devuelve frecuencias y amplitudes
def expo(ti,tf,wi,wf,factor,frequencias,amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]=wf+(wi-wf)*np.exp(-3*(t-ti)/((tf-ti)))
        alpha[i+k]=-0.150 # alpha suficiente para fonar 150
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) * (1+random.normalvariate(0.,.4)) +factor/10 * (1+random.normalvariate(0.,.02))
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i)) * (1+random.normalvariate(0.,.1)) +factor/10 * (1+random.normalvariate(0.,.02))
    return frequencias,amplitudes


def rectas(ti,tf,wi,wf,factor,frequencias,amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t=ti+k*dt
        frequencias[i+k]=wi+(wf-wi)*(t-ti)/(tf-ti) 
        alpha[i+k]=-0.150 # alpha suficiente para fonar 150
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.4))
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.1))
    return frequencias,amplitudes #150*


def senito(ti,tf,media,amplitud,alphai,alphaf,factor,frequencias, amplitudes):
    i=np.int(ti/dt)
    j=np.int(tf/dt)
    for k in range((j-i)):
        t = ti+k*dt
        frequencias[i+k]=media+amplitud*np.sin(alphai+(alphaf-alphai)*(t-ti)/(tf-ti))
        alpha[i+k]=-0.150 # alpha suficiente para fonar 150
        amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.2))
        #amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*(1+random.normalvariate(0.,.1))
    return frequencias,amplitudes



# ----------------------
# Deficion de parametros
# ----------------------

# Este for esta de mas pero me puede servir mas adelante 
# para sintetizar n cantos con variantes que proponga
for n_canto in range(1): 

    
    # Parametros especificos del modelo
    # ---------------------------------
    
    gamma = 12300 #12500 
    uoch, uolg, rdis = 40*2700*2700, 1./1., 5000/1.0 # Parametros tracto vocal
    v = np.zeros(5)
    v[0], v[1], v[2], v[3], v[4] =0.01,0.001,0.001, 0.0001, 0.0001

    L =  0.036 # No se que es !!!



    # Parametros especificos del canto
    # --------------------------------
    
    dt = 1/44100.0
    tiempo_total = 2.07
    
    # Inicializo las frecuencias fundamentales y amplitudes
    frequencias = np.zeros(np.int(tiempo_total/(dt)))
    amplitudes = np.zeros(np.int(tiempo_total/(dt)))
    
    # Inicializo los parametros de control
    alpha = np.zeros(np.int(tiempo_total/(dt)))
    beta = np.zeros(np.int(tiempo_total/(dt)))
    
    # Modifico valores variables que cree arriba
    for i in range(np.int(tiempo_total/(dt))):
        alpha[i] = 0.15 # sistema no fona en este valor
        beta[i] = 0.15 # ¿sistema no fona en este valor?


    # Para cada silaba defino: alpha, frecuencias fundamentales y amplitudes
    expo(0.021233,0.070797,869.3,475.2,0.2239/0.944,frequencias, amplitudes)
    expo(0.163317,0.205335,825.5,453,0.2714/0.944,frequencias, amplitudes)
    expo(0.271632,0.313879,847.4,475.1,0.3216/0.944,frequencias, amplitudes)
    expo(0.383282,0.425770,891,475.1,0.3449/0.944,frequencias, amplitudes)
    rectas(0.467733,0.479150,812.64,812.64,0.08789/0.944,frequencias, amplitudes)
    expo(0.479152,0.527799,897,518.9,0.325/0.944,frequencias,amplitudes)
    rectas(0.592287,0.631223,573,431,0.3074/0.944,frequencias, amplitudes)
    rectas(0.699323,0.726651,847.4,497,0.2258/0.944,frequencias, amplitudes)
    rectas(0.794424,0.824770,1550,1550,0.08599/0.944,frequencias, amplitudes)
    expo(0.824771,0.929312,900,518.9,0.7771/0.944,frequencias, amplitudes)#1110
    rectas(0.956319,0.969585,475,781,0.3498/0.944,frequencias, amplitudes)
    rectas(0.969586,1.000902,871,871,0.4434/0.944,frequencias, amplitudes)
    rectas(1.035779,1.036574,475,570,0.389/0.944,frequencias, amplitudes)
    rectas(1.036578,1.099138,579.72,559.72,0.9205/0.944,frequencias, amplitudes)
    rectas(1.099139,1.107158,579.72,409.4,0.2376/0.944,frequencias, amplitudes)
    rectas(1.134231,1.139772,935,1548,0.1221/0.944,frequencias, amplitudes)
    rectas(1.141474,1.160209,546.62,546.62,0.1221/0.944,frequencias, amplitudes)
    rectas(1.160210,1.173081,546.62,344,0.4057/0.944,frequencias, amplitudes)
    senito(1.212321,1.223899,1132,1877,-np.pi/2,np.pi/2,0.2076/0.944,frequencias, amplitudes)
    senito(1.2240,1.251077,2534,963,-3*np.pi/2,15*np.pi/2,0.3622/0.944,frequencias, amplitudes)
    expo(1.259591,1.284083,1263,803,0.3622/0.944,frequencias, amplitudes)
    rectas(1.357033,1.364902,1571,1571,0.531/0.944,frequencias, amplitudes)
    rectas(1.366208,1.382211,1592,1592,0.8903/0.944,frequencias,amplitudes)
    rectas(1.386501,1.486461,1023,475,0.7487/0.944,frequencias,amplitudes)
    rectas(1.521486,1.529366,497,847,0.3285/0.944,frequencias,amplitudes)
    rectas(1.530969,1.564968,977,828,0.4556/0.944,frequencias,amplitudes)
    rectas(1.599836,1.606783,497,565,0.3814/0.944,frequencias,amplitudes)
    rectas(1.606784,1.660270,558,558,0.7228/0.944,frequencias,amplitudes)
    rectas(1.660270,1.670171,558,387.5,0.4041/0.944,frequencias,amplitudes)
    rectas(1.699486,1.726439,540.73,540.73,0.4691/0.944,frequencias,amplitudes)
    rectas(1.726440,1.737927,540.73,365.6,0.2306/0.944,frequencias,amplitudes)
    senito(1.775943,1.787108,1142,563,-np.pi,np.pi,0.1919/0.944,frequencias, amplitudes)
    senito(1.787778,1.817603,2414,927,-np.pi/2,15*np.pi/2,0.2852/0.944,frequencias, amplitudes)
    expo(1.824992,1.848924,737,387,0.1677/0.944,frequencias,amplitudes)
    rectas(1.931650,1.948097,1550,1550,0.944/0.944,frequencias,amplitudes)
    expo(1.948099,2.06,1023,431,0.7555/0.944,frequencias,amplitudes)
    
    
    # Abro el archivo b_w que no se que es aun.
    bes,was = np.loadtxt('b_w_12300.txt',unpack=True)
    print('bes:', bes[0])
    print('was:',was[0])
    
    # Ajustamos was vs bes a un polinomio de grado 5
    # z es una lista de los coeficientes del polinomio ajustado
    #z = np.polyfit(was, bes, 5)
    z = np.polyfit(was, bes, 2)    
    
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

    # Una integracion A PARTIR DE ACA ME CUESTA ENTENDER EL CODIGO

    n = 5 # TAMANO DEL SISTEMA DE ECUACIONES
    sonido = []
    
    # Variables de interes de la integracion que quizas quiera guardar
    #x1 = []
    #y1 = []
    #tiempo1 = []
    #amplitud1 = []
    #forzado1 = []
    #dforzadodt1 = []
    #elbeta1 = []

    
    # No saco lo de abajo porque lo necesita destimulodt pero no se bien que hacen
    N = int((L /(350*dt))//1)
    fil1 = np.zeros(N)
    back1 = np.zeros(N)
    # feedback1 = 0
    

    for i in range(np.int(tiempo_total/(dt))):
        
        # Parametros dependientes del tiempo del sistema de ecuaciones
        # Variables globales ¿es necesario que asi lo sean?
        alp=alpha[i]
        b=beta[i]*(1+random.normalvariate(0.,.3))
        #b=beta[i]*(1+random.normalvariate(0.,.1)) 
        destimulodt = (fil1[N-1]-fil1[N-2])/dt
        
        # Integracion
        t =i*dt
        rk4(ecuaciones,v,n,t,dt) # modifica v
       
        
        # Actualizo las siguientes variables ?   
        #estimulo=fil1[N-1]
        fil1[0]=v[1]+back1[N-1]
        back1[0]=-0.35*fil1[N-1]
        fil1[1:]=fil1[:-1]
        back1[1:]=back1[:-1]
        #feedback1=back1[N-1]


        # Guardo resultado de integracion v[3] en sonido
        sonido.append(v[3]*amplitudes[i])
        
        # Guarda variables de interes de la integracion
        # no esta chequeado que ande
        #x1.append(v[0])  
        #y1.append(v[1])
        #tiempo1.append(t)
        #amplitud1.append(amplitudes[i])
        #forzado1.append(estimulo)
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
    scaled = np.int16(sonido/np.max(np.abs(sonido)) * 32767)
    write('sintesis_finch_{}.wav'.format(n_canto), 44100, scaled)


'''
    # -------------------------------
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

    

    

