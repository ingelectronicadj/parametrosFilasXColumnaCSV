#Modulo en version python 3.4
# LEER ARCHIVOS TXT, YSP, S2P Y LOS CONVIERTE A MATRICES DE FLOTANTES
#el archivo texto.txt es un Y2P
# Autor: Jose Noe Poveda, jpoveda@udistrital.edu.co

import numpy as np
import math as mt
import sys

#leer archivo (probado)
def Leer_Y():
    #nombre=imput("Digite el nombre del archivo de datos")
    #3with open(nombre,"r") as datos
	while True:
		try:
			datos=open(input("digite el nombre del archivo: "),'r')
			break
		except ValueError:
			print ("archivo no encontrado")
	matriz=[]
	for dato in datos:
		dato=dato.strip()
		if dato[0] =='!':continue
		linea_de_matriz=[float(dato) for dato in dato.split()]
		matriz.append(linea_de_matriz)
	return matriz

#Convertir vector a parametros Y(probado)
def param(x):
    y=[]    
    for i in range(0,8,2):
        
        y.append(x[0][i+1]+x[0][i+2]*1j)
        
    return  y

#estabilidad (probado)
def linv(yi,yr,yf,yo):
        y=yr*yf
        c=abs(y)/(2*(yi.real*yo.real)-(y.real))
        return c

#Evaluacion de los parametros de transitor estable (probado)

def yio(yi,yr,yf,yo):
        y=yr*yf
        N=mt.sqrt(((2*yi.real*yo.real-(y.real))**2)-((abs(y))**2))
        Gi=N/(2*yo.real)
        Go=N/(2*yi.real)
        Bo=yo.imag-y.imag/(2*yi.real)
        Bi=yi.imag-y.imag/(2*yo.real)
        Yi=Gi+Bi*1j
        Yo=Go+Bo*1j
        MAG=((abs(yf))**2)/(4*yi.real*yo.real)
        Gt=((abs(yf))**2)/(((2*yi.real*yo.real-(y.real)))+N)
        return Yi, Yo, Gt, MAG

#Diseno de amplifcador inestabeles
def sturn(yi,yr,yf,yo):
        k=int(input("digite el valor de estabilidad K deseado: "))
        Rs=int(input("Digite el valor de Rs para mejor figura de ruido: "))
        y=yr*yf
        c=abs(y)/(2*(yi.real*yo.real)-(y.real))
        gl=(k*(abs(y)+y.real)/(2*((yi.real)+1000/Rs)))-yo.real
        Yo=yo
        Yi=yi-(y/(yo+(gl-Yo.imag*1j)))
        i=int(input("Indique el No. de iteraciones: "))

        while i!=0:
                Yo=yo-(y/(yi+(1000/Rs-Yi.imag*1j)))
                Yi=yi-(y/(yo+(gl-Yo.imag*1j)))  
                i-=1
                #print("Yi,Yo", Yi, Yo)
        
        Ys=(Yi.real-Yi.imag*1j)
        Yl=(gl-Yo.imag*1j)
        D=abs((yi+Ys)*(yo+Yl)-y)
        Gt=4*gl*(Yi.real)*(abs(yf)**2)/(D**2)
        return Ys, Yl, Gt

m=Leer_Y()
x=m[10:11]
s=param(x)
t=s[0]
c=linv(s[0], s[2], s[1], s[3])
if c<1:
        y=yio(s[0], s[2], s[1], s[3])
        print("La impedancia de entrada y de salida son:",
              "Yopt = ", y[0], "S, Yopt = ", y[1], "S")
else: y=sturn(s[0], s[2], s[1], s[3]); 
print("La impedancia de entrada y de salida  por desacople son:", "Ys = ", y[0], "S, YL = ", y[1], "S")


print("La frecuencia de trabajo es de: ", x[0][0], c)
