import pandas as pd
import csv


def copia_csv():
    
    data=pd.read_csv('TotalesNacionales_T.csv',header=0) 
    aux0=data[["Casos totales","Casos recuperados","Casos activos","Casos nuevos totales"]]
    aux0 = aux0.fillna(0)
    new_data = []
    for i in (range(len(aux0["Casos totales"]))):
        diccionario = {}
        
        aux1=aux0["Casos totales"][i]
        aux2=aux0["Casos recuperados"][i]
        aux3=aux0["Casos activos"][i]
        aux4=aux0["Casos nuevos totales"][i]

        aux1=int(aux1)
        aux2=int(aux2)
        aux3=int(aux3)
        aux4=int(aux4)

        diccionario["Casos totales"] = aux1
        diccionario["Casos recuperados"] = aux2
        diccionario["Casos activos"] = aux3
        diccionario["Casos nuevos totales"] = aux4

        new_data.append(diccionario)
    
    with open('datosc19.csv', 'w') as f:
        w = csv.DictWriter(f, new_data[0].keys())
        w.writeheader()
        for diccionario in new_data:
            w.writerow(diccionario)
    
