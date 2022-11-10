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


# -----------------------
# Definicion de funciones
# -----------------------

# Sistema de ecuaciones del modelo
# Se utiliza asi: rk4(ecuaciones,v,n,t,dt)
def modelo_finch(v0, b, alp, gamma, Ch, Lg, Rd, destimulodt):
    x ,y,i1,i2,i3 = v0
    dv = [0]*5

    dv[0]=y
    dv[1]= gamma*gamma*alp+ b *gamma*gamma*x-gamma*gamma*x*x*x-gamma*x*x*y+gamma*gamma*x*x-gamma*x*y
    dv[2]= i2
    dv[3]= - 1/(Ch*Lg)*i1 - (Rd/Lg)*i2 + (1/Lg)*destimulodt
    dv[4]=0.
    
    return dv

# Integrador RK4
def rk4(dv, v0, dt, *args, **kargs): #  dv es la funcion modelo_finch()
    
    v0 = np.asarray(v0)
    k1 = np.asarray( dv(v0, *args))
    k2 = np.asarray( dv(v0 + k1*dt/2, *args))
    k3 = np.asarray( dv(v0 + k2*dt/2, *args))
    k4 = np.asarray( dv(v0 + k3*dt, *args))

    v1 = v0 + (k1 + 2*k2 + 2*k3 + k4)*dt/6
    return v1


# ejemplo
def campo_vector(v0, a , b):
    # Como ahora las variables vienen en una lista (en el primer argumento: z)
    # primero las separamos para que sea más claro
    x , y = v0
    # Y ahora calculamos las derivadas
    dxdt = a*x+2*y # a = 4
    dydt = -17*x+b*y # b = -5
    return [dxdt, dydt]

# Integracion Runge-Kutta 4
dt = 0.01
tmax = 1
t = np.arange(0, tmax, dt)
plt.figure()
Xi = np.linspace(-4, 4, 4)
Yi = np.linspace(-4, 4, 4)
plt.figure()
for xi in Xi:
    for yi in Yi:
        
        # Definimos los vectores vacios
        xt = np.zeros_like(t)
        yt = np.zeros_like(t)

        # Definimos la condicion inicial
        xt[0], yt[0] = xi, yi

        for i in range(len(t)-1):
            xt[i+1], yt[i+1] = rk4(campo_vector, [xt[i], yt[i]], dt, 4, -5)

        # Ploteamos als soluciones
        plt.plot(xt, yt)





