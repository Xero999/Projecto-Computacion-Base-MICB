from GitImport import instalador # importe de la funcion que obtiene la base de datos actualizada
from Copia_CSV import copia_csv # importe de la funcion que repara los datos 
import pandas as pd
import subprocess
import csv

def existe_data_inicial():
    aux0=subprocess.call('find TotalesNacionales_T.csv',shell=True)
    return aux0

def existe_data_reparada():
    aux0=subprocess.call('find datosc19.csv',shell=True)
    return aux0

def lector_data():
    aux0=existe_data_inicial()
    aux1=existe_data_reparada()
    if aux1 == 1:
        if aux0 == 1:
            instalador()
        copia_csv()
    data = pd.read_csv('datosc19.csv',header=0) 
    return data

def porcentual(data):

    #columna = "Casos nuevos totales";
    columna = "Casos totales";

    lista_porcentajes= []
    temp = (len(data[columna])-1)
    i = temp - 20 # el numero son la cantidad de dias antes 
    while i < temp:
        
        actual= data[columna][i+1]
        anterior= data[columna][i]

        if anterior == 0:
            lista_porcentajes.append(((anterior-actual)/actual)*-1)

        else:
            porcentual= ((actual-anterior)/anterior)

            lista_porcentajes.append(round(porcentual,4))
        i = i+1
    variaciones= {'porcentajes': lista_porcentajes}
    return variaciones

def calculot(variaciones, data1):
    
    #columna = "Casos nuevos totales";
    columna = "Casos totales";

    print("A cuantos dias a futuro desea realizar el calculo? (͠≖ ͜ʖ͠≖)👌: ", end="")
    d=input()
    d=int(d)

    aux0 = data1[[columna]]
    new_data = []
    
    
    aux1=aux0[columna][len(aux0[columna])-1]
        
    for j in (range(len(variaciones["porcentajes"]))):
        aux3=variaciones["porcentajes"][j]
        new_data.append(aux3)
    
    res=[]
    k=0

    aux2 = len(aux0[columna]) - 20
    while aux2 < len(aux0[columna]):
        diccionario0={}
        dato = aux0[columna][aux2]
        diccionario0["Casos a "+str(d)+" dias a futuro"] = dato
        res.append(diccionario0)
        aux2 = aux2 + 1 

    suma=sum(new_data)
    prom=suma/len(new_data)
    while k < d:
        diccionario0={}
        aux1=int(aux1+(aux1*prom))
        diccionario0["Casos a "+str(d)+" dias a futuro"] = aux1
        res.append(diccionario0)
        k=k+1 

    with open('proyeccionesc19.csv', 'w') as f:
        w = csv.DictWriter(f, res[0].keys())
        w.writeheader()
        for diccionario0 in res:
            w.writerow(diccionario0)
    return res

if __name__ == '__main__':
    data = lector_data()
    variaciones= porcentual(data)# formula = (actual - anterior)/anterior //// en caso de que anterior sea 0 ((anterior - actual)/actual)*-1
    finald=calculot(variaciones, data)
    #print(finald)
    print("✨(っ◔︣◡◔᷅)っc(◕︣◡◕᷅c)✨")