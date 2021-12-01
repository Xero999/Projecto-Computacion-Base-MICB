import subprocess
import os

def instalador():
    
    aux = os.getcwd()

    print("\nSe encuentra en el directorio: "+aux)
    
    aux2 = subprocess.call('apt list --installed | grep subversion',shell=True)

    if aux2 == 1:
        print('El programa svn no se encuentra instalado')
        print('Desea instalarlo(S/N): ', end=''), 
        aux3= input()
        
        if aux3 == 's':
            subprocess.call("sudo apt install subversion", shell=True)
        elif aux3 == 'n':
            print("Terminando ejecucion")    
            exit()
        elif aux2 != 's' or aux2 != 'n':
            print("Opcion ingresada invalida")
            instalador()
    
    print("Importando Datos")
    subprocess.call("svn export --force https://github.com/MinCiencia/Datos-COVID19/branches/master/output/producto5/TotalesNacionales_T.csv", shell=True)
