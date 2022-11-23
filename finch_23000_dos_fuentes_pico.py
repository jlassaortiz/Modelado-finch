# -*- coding: utf-8 -*-
"""
Created on march 2017

@author: Gabo Mindlin

Integrator with rk4, and tube with delays

it creates wav


"""


import numpy as np
#import pylab      
from scipy.io.wavfile import write
import random
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io import wavfile

global alp
global feedback1 
global estimulo1
global destimulodt1
global b
    

for lazo in range(1):
 #   gamma=12500
    gamma=23000
#    uoch, uolb, uolg, rb, rdis = (350/2.8)*100000000, 0.0001 , 1/20., .35*1000000, 48*1000
#    uoch, uolb, uolg, rb, rdis = 45*3800*3800, 0.0001 , 1./1., .35*1000000, 3800/2.0    
#    uoch, uolg, rdis = 90000000, 1./1., 28000 # con 5000 de rdis se enfatiza la frecue  ncia oec, como cerca de 4700 si uoc=40 4700 4700
    uolb, uolg, rb, rdis = 1/200.0 , 1/40., 400000, 600000 # 24*10000 , y con 350/3.0, la frec de la oec en 4000 Hz
    beta, dt, t0, tf, L= -0.15, 1/882000.0, 0, 0.5, 0.036
    t=0
    fsamp=1/dt
    samplerate, data_real = wavfile.read('zfAB010-bi_BOS03.wav')
    tiempo_total=20*len(data_real)*(1/882000.)

    frequencias=np.zeros(np.int(tiempo_total/(dt)))
    tiempos=np.zeros(np.int(tiempo_total/(dt)))
    alpha=np.zeros(np.int(tiempo_total/(dt)))
    amplitudes=np.zeros(np.int(tiempo_total/(dt)))
    beta=np.zeros(np.int(tiempo_total/(dt)))
    ch=np.zeros(np.int(tiempo_total/(dt)))
    ch=ch+(350/1.50)*100000000
    fch=1.0

    frequencias2=np.zeros(np.int(tiempo_total/(dt)))
    tiempos2=np.zeros(np.int(tiempo_total/(dt)))
    alpha2=np.zeros(np.int(tiempo_total/(dt)))
    amplitudes2=np.zeros(np.int(tiempo_total/(dt)))
    beta2=np.zeros(np.int(tiempo_total/(dt)))
    ch2=np.zeros(np.int(tiempo_total/(dt)))
    ch2=ch2+(350/1.50)*100000000
    fch2=1.0


#    bes,was=np.loadtxt('b_w_12500.txt',unpack=True)
    bes,was=np.loadtxt('b_w_23000.txt',unpack=True)



    for i in range(np.int(tiempo_total/(dt))):
        tiempos[i]=i*dt
        beta[i]=0.15
        amplitudes[i]=0.
        alpha[i]=0.15
        beta2[i]=0.15
        amplitudes2[i]=0.
        alpha2[i]=0.15

    v=np.zeros(5)
    v[0], v[1], v[2], v[3], v[4] =0.01,0.001,0.001, 0.0001, 0.0001
# --------------------
# Function definitions
# --------------------
    def ecuaciones(v, dv):
        x,y,i1,i2,i3 = v
        dv[0]=y
        dv[1]=gamma*gamma*alp+b*gamma*gamma*x-gamma*gamma*x*x*x-gamma*x*x*y+gamma*gamma*x*x-gamma*x*y
        dv[2]= i2
        dv[3]=-uolg*uoch*i1-(rdis*uolb+rdis*uolg)*i2+(uolg*uoch-rdis*rb*uolg*uolb)*i3+uolg*destimulodt+rdis*uolg*uolb*estimulo
        dv[4]=-(uolb/uolg)*i2-rb*uolb*i3+uolb*estimulo
        return dv


    
    def expo(ti,tf,wi,wf,factor,fch,frequencias,beta,amplitudes,ch):
        i=np.int(ti/dt)
        j=np.int(tf/dt)
        for k in range((j-i)):
            t=ti+k*dt
            frequencias[i+k]=wf+(wi-wf)*np.exp(-3*(t-ti)/((tf-ti)))
            alpha[i+k]=-0.150
            #amplitudes[i+k]=(1/(1+np.exp(-(t-ti)/0.01))-1/(1+np.exp(-(t-tf)/0.01)))
            amplitudes[i+k]=1.*factor #factor*np.sin(np.pi*k/(j-i))
            ch[i+k]=fch*ch[i+k]
        return frequencias,beta,amplitudes,ch
    def expo2(ti,tf,wi,wf,factor,fch,frequencias2,beta2,amplitudes2,ch2):
        i=np.int(ti/dt)
        j=np.int(tf/dt)
        for k in range((j-i)):
            t=ti+k*dt
            frequencias2[i+k]=wf+(wi-wf)*np.exp(-3*(t-ti)/((tf-ti)))
            alpha2[i+k]=-0.150
            #amplitudes[i+k]=(1/(1+np.exp(-(t-ti)/0.01))-1/(1+np.exp(-(t-tf)/0.01)))
            amplitudes2[i+k]=1.*factor #factor*np.sin(np.pi*k/(j-i))
            ch2[i+k]=fch*ch2[i+k]
        return frequencias2,beta2,amplitudes2,ch2



    def rectas(ti,tf,wi,wf,factor,fch,frequencias,beta,amplitudes,ch):
        i=np.int(ti/dt)
        j=np.int(tf/dt)
        for k in range((j-i)):
            t=ti+k*dt
            frequencias[i+k]=wi+(wf-wi)*(t-ti)/(tf-ti)
            alpha[i+k]=-0.150
            #amplitudes[i+k]=(1/(1+np.exp(-(t-ti)/0.01))-1/(1+np.exp(-(t-tf)/0.01)))
            amplitudes[i+k]= 1.*factor #factor*np.sin(np.pi*k/(j-i))
#            amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*1/(1+np.exp(-(1/0.025)*(np.sin(np.pi*k/(j-i))-0.25)))
            #amplitudes[i+k]=factor*(1+.0*np.sin(150*np.pi*k/(j-i)))#/(1+np.exp(-(1/0.0075)*(np.sin(np.pi*k/(j-i))-0.25)))
            ch[i+k]=fch*ch[i+k]
        return frequencias,beta,amplitudes,ch
    def rectas2(ti,tf,wi,wf,factor,fch,frequencias2,beta2,amplitudes2,ch2):
        i=np.int(ti/dt)
        j=np.int(tf/dt)
        for k in range((j-i)):
            t=ti+k*dt
            frequencias2[i+k]=wi+(wf-wi)*(t-ti)/(tf-ti)
            alpha2[i+k]=-0.150
            #amplitudes[i+k]=(1/(1+np.exp(-(t-ti)/0.01))-1/(1+np.exp(-(t-tf)/0.01)))
            amplitudes2[i+k]= 1.*factor #factor*np.sin(np.pi*k/(j-i))
#            amplitudes[i+k]=factor*np.sin(np.pi*k/(j-i))*1/(1+np.exp(-(1/0.025)*(np.sin(np.pi*k/(j-i))-0.25)))
            #amplitudes[i+k]=factor*(1+.0*np.sin(150*np.pi*k/(j-i)))#/(1+np.exp(-(1/0.0075)*(np.sin(np.pi*k/(j-i))-0.25)))
            ch2[i+k]=fch*ch2[i+k]
        return frequencias2,beta2,amplitudes2,ch2    
    

    def senito(ti,tf,media,amplitud,alphai,alphaf,factor,fch,frequencias,beta,amplitudes,ch):
        i=np.int(ti/dt)
        j=np.int(tf/dt)
        for k in range((j-i)):
            t=ti+k*dt
            frequencias[i+k]=media+amplitud*np.sin(alphai+(alphaf-alphai)*(t-ti)/(tf-ti))
            alpha[i+k]=-0.150
            #amplitudes[i+k]=(1/(1+np.exp(-(t-ti)/0.01))-1/(1+np.exp(-(t-tf)/0.01)))
            amplitudes[i+k]=1.*factor #factor*np.sin(np.pi*k/(j-i))
            ch[i+k]=fch*ch[i+k]
        return frequencias,beta,amplitudes,ch
    def senito2(ti,tf,media,amplitud,alphai,alphaf,factor,fch,frequencias2,beta2,amplitudes2,ch2):
        i=np.int(ti/dt)
        j=np.int(tf/dt)
        for k in range((j-i)):
            t=ti+k*dt
            frequencias2[i+k]=media+amplitud*np.sin(alphai+(alphaf-alphai)*(t-ti)/(tf-ti))
            alpha2[i+k]=-0.150
            #amplitudes[i+k]=(1/(1+np.exp(-(t-ti)/0.01))-1/(1+np.exp(-(t-tf)/0.01)))
            amplitudes2[i+k]=1.*factor #factor*np.sin(np.pi*k/(j-i))
            ch2[i+k]=fch*ch2[i+k]
        return frequencias2,beta2,amplitudes2,ch2

    

    expo(0.021233,0.070797,850.3,400.2,2.,1,frequencias,beta,amplitudes,ch)
#    rectas2(0.021233,0.070797,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    rectas(0.1352,0.162,850.3,850.3,1.,1,frequencias,beta,amplitudes,ch)
#    rectas2(0.1352,0.162,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    expo(0.162,0.204,850.5,400,2.,1,frequencias,beta,amplitudes,ch)
#    rectas2(0.162,0.202,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    rectas(0.254,0.270,850.3,850.3,1.,1,frequencias,beta,amplitudes,ch)
#    rectas2(0.254,0.270,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    expo(0.270,0.313879,850.4,400.1,2.,1,frequencias,beta,amplitudes,ch)
 #   rectas2(0.270,0.313879,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    rectas(0.366,0.380,850.3,850.3,1.,1,frequencias,beta,amplitudes,ch)
  #  rectas2(0.366,0.380,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    expo(0.380,0.42770,850,400.1,2.,1,frequencias,beta,amplitudes,ch)
   # rectas2(0.380,0.42770,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    rectas(0.468,0.482,850.3,850.3,1.,1,frequencias,beta,amplitudes,ch)
    #rectas2(0.468,0.482,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)    
    expo(0.482,0.52770,850,400.1,2.,1,frequencias,beta,amplitudes,ch)
#    rectas2(0.482,0.52770,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    senito(0.57424,0.63,400.,150.,np.pi/2,np.pi,1.,1,frequencias,beta,amplitudes,ch)
 #   rectas2(0.57424,0.63,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    
    senito(.65,.66,1232,400,-np.pi/2,np.pi/2,1,1,frequencias,beta,amplitudes,ch)
  #  rectas2(0.65,0.33,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    senito(0.66,0.693,2534,563,-3*np.pi/2,15*np.pi/2,1,1,frequencias,beta,amplitudes,ch)
    rectas2(0.666,0.669,3900.3,3900.3,.5,1,frequencias2,beta2,amplitudes2,ch2)
    rectas2(0.672,0.675,3900.3,3900.3,.5,1,frequencias2,beta2,amplitudes2,ch2)
    rectas2(0.678,0.682,3900.3,3900.3,.5,1,frequencias2,beta2,amplitudes2,ch2)
    rectas2(0.684,0.689,3900.3,3900.3,.5,1,frequencias2,beta2,amplitudes2,ch2)
    rectas2(0.691,0.698,3900.3,3900.3,.5,1,frequencias2,beta2,amplitudes2,ch2)
    expo(.69391,0.723,1000,534,.5,1,frequencias,beta,amplitudes,ch)
    #rectas2(0.69391,0.723,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)

    senito(.77,.794,1132,300,-np.pi/2,np.pi/2,.5,1,frequencias,beta,amplitudes,ch)
#    rectas2(0.77,0.794,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    rectas(0.794424,0.824770,1550,1550,1.,1,frequencias,beta,amplitudes,ch)
 #   rectas2(0.794424,0.824770,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    expo(0.824771,0.929312,900,518.9,1.0,1,frequencias,beta,amplitudes,ch)#1110
  #  rectas2(0.824771,0.929312,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)    
    rectas(0.956319,0.969585,475,871,1.,1,frequencias,beta,amplitudes,ch)
   # rectas2(0.956319,0.969585,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    rectas(0.969586,1.000902,871,871,1.,1,frequencias,beta,amplitudes,ch)
    #rectas2(0.969586,1.000902,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)

    senito(1.03139,1.107158,542.72,40.4,0,np.pi,1.,1,frequencias,beta,amplitudes,ch)
#    rectas2(1.03139,1.107158,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)

   # senito(1.03,1.107,520,20,0,np.pi,2.,frequencias,beta,amplitudes)

    senito(1.134231,1.17,540,20,0,np.pi, 1.,1,frequencias,beta,amplitudes,ch)
 #   rectas2(1.134231,1.17,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
 
    senito(1.212321,1.223899,1132,400,-np.pi/2,np.pi/2,1.,1,frequencias,beta,amplitudes,ch)
  #  rectas2(1.212321,1.223899,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    senito(1.2240,1.258077,2534,963,-3*np.pi/2,15*np.pi/2,1.0,1,frequencias,beta,amplitudes,ch)
   # rectas2(1.2240,1.258077,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    expo(1.259591,1.284083,1263,803,.50,1,frequencias,beta,amplitudes,ch)
    #rectas2(1.259591,1.284083,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
 
    senito(1.347,1.357,1132,400,-np.pi/2,np.pi/2,1.,1,frequencias,beta,amplitudes,ch)
#    rectas2(1.347,1.357,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    senito(1.357033,1.382902,1592,40,0,np.pi,1.0,1,frequencias,beta,amplitudes,ch)
 #   rectas2(1.357033,1.382902,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    expo(1.382902,1.491083,1592,600,1.0,1,frequencias,beta,amplitudes,ch)
  #  rectas2(1.382902,1.491083,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
     

    rectas(1.521486,1.529366,520,903,1.0,1,frequencias,beta,amplitudes,ch)
   # rectas2(1.521486,1.529366,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    rectas(1.530969,1.564968,903,903,1.0,1,frequencias,beta,amplitudes,ch)
    #rectas2(1.530969,1.564968,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    
    senito(1.599836,1.686783,544,44,0,np.pi,1.0,1,frequencias,beta,amplitudes,ch)
#    rectas2(1.599836,1.686783,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
  
    senito(1.699486,1.746439,540.73,40.73,0,np.pi,1.0,1,frequencias,beta,amplitudes,ch)
 #   rectas2(1.699486,1.746439,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
 

    senito(1.775943,1.787108,1142,463,-np.pi,np.pi,1.0,1,frequencias,beta,amplitudes,ch)
  #  rectas2(1.775943,1.787108,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    senito(1.787778,1.8203,2414,927,-np.pi/2,15*np.pi/2,1.0,1,frequencias,beta,amplitudes,ch)
   # rectas2(1.787778,1.8203,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    
    expo(1.824992,1.848924,737,487,1.0,1,frequencias,beta,amplitudes,ch)
    #rectas2(1.824992,1.848924,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    
    senito(1.92,1.93,1132,400,-np.pi/2,np.pi/2,1.,1,frequencias,beta,amplitudes,ch)
#    rectas2(1.92,1.93,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    senito(1.931650,1.948097,1550,50,0,np.pi, 1.0,1,frequencias,beta,amplitudes,ch)
 #   rectas2(1.931650,1.948097,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)
    expo(1.948099,2.06,1023,431,1.0,1,frequencias,beta,amplitudes,ch)
  #  rectas2(1.948099,2.06,1769.3,1769.3,2.,1,frequencias2,beta2,amplitudes2,ch2)

    
    
    
    z = np.polyfit(was, bes, 5)
    p = np.poly1d(z)
    for i in range(np.int(tiempo_total/(dt))):
        if(alpha[i]<0):
            beta[i]=p(frequencias[i])
    
    for i in range(np.int(tiempo_total/(dt))):
        if(alpha2[i]<0):
            beta2[i]=p(frequencias2[i])
#            beta2[i]=0

    

#%%




 


    def rk4(dv,v,n,t,dt):
        v1=[]
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
        dv(v1, k1)
        for x in range(0, n):
            v1[x]=v[x]+dt2*k1[x]
        dv(v1, k2)     
        for x in range(0, n):
            v1[x]=v[x]+dt2*k2[x]
        dv(v1, k3)
        for x in range(0, n):
            v1[x]=v[x]+dt*k3[x]
        dv(v1, k4)
        for x in range(0, n):
            v1[x]=v[x]+dt*k4[x]        
        for x in range(0, n):
            v[x]=v[x]+dt6*(2.0*(k2[x]+k3[x])+k1[x]+k4[x])
        return v


# una integracion

    n=5 #Cantidad de variables   
    x1=[]
    y1=[]
    tiempo1=[]
    sonido=[]
    sonido_total=[]
    amplitud1=[]
    forzado1=[]
    dforzadodt1=[]
    elbeta1=[]
    
    cont1=0
    N=int((L/(350*dt))//1)
    fil1=np.zeros(N)
    back1=np.zeros(N)
    feedback1=0

#while t<tf:
    for i in range(np.int(tiempo_total/(dt))):
        alp=alpha[i]*(1+random.normalvariate(0,0.1))
        b=beta[i]*(1+random.normalvariate(0,0.1))
        uoch=ch[i]
        t=i*dt
        estimulo=fil1[N-1]
        destimulodt=(fil1[N-1]-fil1[N-2])/dt
        rk4(ecuaciones,v,n,t,dt)
        fil1[0]=v[1]*(1+random.normalvariate(0,0.05))+back1[N-1]
 #       back1[0]=-0.35*fil1[N-1]
        back1[0]=-0.25*fil1[N-1]
        fil1[1:]=fil1[:-1]
        back1[1:]=back1[:-1]
        feedback1=back1[N-1]
        
        x1.append(cont1)  #ACÁ ARMO LOS ARREGLOS DE X Y Z CON LOS RESULTADOS QUE VA LARGANDO "V"
        y1.append(cont1)
        tiempo1.append(cont1)
        sonido.append(cont1)
        sonido_total.append(cont1)
        amplitud1.append(cont1)
        forzado1.append(cont1)
        dforzadodt1.append(cont1)
        elbeta1.append(cont1)
        
        x1[cont1]=v[0]
        y1[cont1]=v[1]
        tiempo1[cont1]=t
        sonido[cont1]=v[3]*amplitudes[i]*(1+random.normalvariate(0,0.05))
        sonido_total[cont1]=0
        amplitud1[cont1]=amplitudes[i]
        forzado1[cont1]=estimulo
        dforzadodt1[cont1]=destimulodt
        elbeta1[cont1]=beta[i]

        cont1=cont1+1

# otra integracion
    n=5 #Cantidad de variables   
    x2=[]
    y2=[]
    tiempo2=[]
    sonido2=[]
    amplitud2=[]
    forzado2=[]
    dforzadodt2=[]
    elbeta2=[]
    
    cont2=0
    N=int((L/(350*dt))//1)
    fil2=np.zeros(N)
    back2=np.zeros(N)
    feedback2=0

#while t<tf:
    for i in range(np.int(tiempo_total/(dt))):
        alp=alpha2[i]*(1+random.normalvariate(0,0.1))
        b=beta2[i]*(1+random.normalvariate(0,0.1))
        uoch=ch2[i]
        t=i*dt
        estimulo=fil2[N-1]
        destimulodt=(fil2[N-1]-fil2[N-2])/dt
        rk4(ecuaciones,v,n,t,dt)
        fil2[0]=v[1]*(1+random.normalvariate(0,0.05))+back1[N-1]
 #       back1[0]=-0.35*fil1[N-1]
        back2[0]=-0.25*fil2[N-1]
        fil2[1:]=fil2[:-1]
        back2[1:]=back2[:-1]
        feedback2=back2[N-1]
        x2.append(cont2)  #ACÁ ARMO LOS ARREGLOS DE X Y Z CON LOS RESULTADOS QUE VA LARGANDO "V"
        y2.append(cont2)
        tiempo2.append(cont2)
        sonido2.append(cont2)
        amplitud2.append(cont2)
        forzado2.append(cont2)
        dforzadodt2.append(cont2)
        elbeta2.append(cont2)
        x2[cont2]=v[0]
        y2[cont2]=v[1]
        tiempo2[cont2]=t
        sonido2[cont2]=v[3]*amplitudes2[i]*(1+random.normalvariate(0,0.05))
        amplitud2[cont2]=amplitudes2[i]
        forzado2[cont2]=estimulo
        dforzadodt2[cont2]=destimulodt
        elbeta2[cont2]=beta2[i]

        cont2=cont2+1







        
    cont3=0
    abs_env=[]
    tiempo_total=[]
    env=[]
#    samplerate, data_real = wavfile.read('zfAB010-bi_BOS03.wav')
    for i in range(len(data_real)):
        for j in range(20):
            abs_env.append(cont3)
            tiempo_total.append(cont3)
            env.append(cont3)
            abs_env[cont3]=np.abs(data_real[i])
            env[cont3]=0
            tiempo_total[cont3]=cont3*(1/(samplerate*20))
            if(cont3>0):
                env[cont3]=env[cont3-1]+(-200.5*env[cont3-1]+abs_env[cont3-1])*(1/(20*samplerate))
            cont3=cont3+1
            



    for i in range(len(sonido)):
        sonido_total[i]=(sonido[i]+sonido2[i]+80*random.uniform(-1.0,1.0))*env[i]


#pylab.plot(tiempo3,sonido_total)
#pylab.xlabel(r'$t\;/\mathrm{sec}$')
#pylab.ylabel(r'$sonido total\;/\mathrm{arb. units}$')
#pylab.show() 
#%%


    sonido_total=np.asarray(sonido_total)
#    sonido2=np.asarray(sonido2)

#    f, t, Sxx = signal.spectrogram(sonido, 882000, window=('gaussian',20*128),nperseg=10*1024,noverlap=18*512,scaling='spectrum')
#    Sxx = np.clip(Sxx, a_min=np.amax(Sxx)/10**3, a_max=np.amax(Sxx))

#    plt.pcolormesh(t,f,np.log10(Sxx),rasterized=True,cmap=plt.get_cmap('Greys'))
#plt.pcolormesh(t,f,Sxx,cmap=plt.get_cmap('Greys'))
#    plt.ylim(10,10000)
#    plt.ylabel('Frequency [Hz]')
#    plt.xlabel('Time [sec]')
#    plt.axis('off')
#    plt.savefig('sonograma_{}.jpeg'.format(lazo), dpi=50, facecolor='w', edgecolor='w',
#                orientation='portrait', papertype=None, format=None,
#                transparent=False, bbox_inches=None, pad_inches=0.1,
#                frameon=None)
#    plt.show()

    scaled = np.int16(sonido_total/np.max(np.abs(sonido_total)) * 32767)
    write('test_23000_dos_fuentes_noisy_pico_{}.wav'.format(lazo), 882000, scaled)
    

#    scaled2 = np.int16(sonido2/np.max(np.abs(sonido2)) * 32767)
#    write('test_23000_dos_fuentes_sonido2_{}.wav'.format(lazo), 882000, scaled2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    