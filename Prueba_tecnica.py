from email.mime import base
import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
Estacion='Estacion_9' #Variable que controla la estacion que se estara analizando () 

def Promedio_año (base , año): #Funcion que calcula el promedio por año de acuerdo con la base de datos y el año.
    con1 = 0                   #Tambien funciona como filtro de datos, en caso las estaciones no pueda registrar alguno (NAN) 
    con2 = 0
    prom = 0
    df=pd.read_csv(base)
    while df['year'].values[con1] < año:
        if pd.isna(df[Estacion].values[con1]) == False and df['year'].values[con1] == año -1    :
            prom= prom +  df[Estacion].values[con1]
            con2 = con2 + 1
        con1 = con1 + 1
        
    if con2 == 0:
        return 0
    else:
        return round (prom / (con2-1),2)

def complemento(base): #Es un complemento a la funcion Promedio_año el cual calcula solo el promedio del ultimo año registrado.
    proma=0
    coma = 0
    b=9861
    df=pd.read_csv(base)
    while b < 10226:
        if pd.isna(df[Estacion].values[b]) == False:
            proma= proma+df[Estacion].values[b]
            coma = coma +1
        b= b+1
    if coma ==0:
        return 0
    else:
        promdio = proma / coma
        return round(promdio,2) 

def Datos_CSV(lista1=[], lista2=[], lista3=[], lista4=[] ): #Funcion que crea un archivo CSV, de los datos de los promedios
    
    nom={'Año':lista4,'Tmax_to':lista1, 'Tmin_to':lista2, 'Prec_to':lista3}
    da=pd.DataFrame(nom)
    da.to_csv('Estacion9.csv')

def graficas_tmax(): #Funcion que realiza graficas de Temperatura maxima vs Tiempo, con forme a la variable Estacion. 
    fig , ax = plt.subplots()
    ax.set_ylabel('Temperatura Maxima (°C)')
    ax.set_xlabel('Tiempo (Años)')
    ax.set_title( 'Temperatura(°C) vs Tiempo (Años), Estacion_9' )
    plt.plot(años,Promedio_tmax)
    plt.xlim(1985,2015)
    plt.ylim(28,35)
    plt.savefig('Estacion9_tmax.jpg')
    plt.show

def graficas_tmin(): #Funcion que realiza graficas de Temperatura minima vs Tiempo, con forme a la variable Estacion.
    fig , ax = plt.subplots()
    ax.set_ylabel('Temperatura Minima (°C)')
    ax.set_xlabel('Tiempo (Años)')
    ax.set_title( 'Temperatura(°C) vs Tiempo (Años), Estacion_9' )
    plt.plot(años,Promedio_tmin)
    plt.xlim(1985,2015)
    plt.ylim(20,25)
    plt.savefig('Estacion9_tmin.jpg')
    plt.show

def graficas_tprec(): #Funcion que realiza graficas de Precipitacion vs Tiempo, con forme a la variable Estacion.
    fig , ax = plt.subplots()
    ax.set_ylabel('Precipitacion (mm)')
    ax.set_xlabel('Tiempo (Años)')
    ax.set_title( 'Precipatacion(mm) vs Tiempo (Años), Estacion_9' )
    plt.plot(años,Promedio_prec)
    plt.xlim(1985,2015)
    plt.ylim(3,10)
    plt.savefig('Estacion9_prec.jpg')
    plt.show

a=1984 #Variale que controla el año, usada para calcular los diferentes promedios.
Promedio_tmax=[] #Lista en donde te gurdan los promedios por años de la base tmax.
Promedio_tmin=[] #Lista en donde te gurdan los promedios por años de la base tmin.
Promedio_prec=[] #Lista en donde te gurdan los promedios por años de la base prec.
años= [] #Lista en donde se guardan los años utilizados en el analisis 
años.append(0) #Se guarda un 0 en la ultima posicion utilizada, para tener el mismo tamaño en las listas de promedios 
while a < 2012 : # Ciclo en donde se llenan todas las listas de Promedio y años
    a = a+1
    años.append(a)
    Promedio_tmax.append (abs(Promedio_año ('.\\tmax_to.csv', a)))
    Promedio_tmin.append (abs(Promedio_año ('.\\tmin_to.csv', a)))
    Promedio_prec.append (abs(Promedio_año ('.\\prec_to.csv', a)))

Promedio_tmax.append (complemento('.\\tmax_to.csv')) #Se agrega complemento a los promedios tmax
Promedio_tmin.append (complemento('.\\tmin_to.csv')) #Se agrega complemento a los promedios tmin
Promedio_prec.append (complemento('.\\prec_to.csv')) #Se agrega complemento a los promedios prec


Datos_CSV(Promedio_tmax, Promedio_tmin, Promedio_prec, años)

#Promedio_tmax()
#Promedio_prec
#Promedio_tmin
#graficas_tmax()
#graficas_tmin()
#graficas_tprec()
