# Gráfico de dos espectros superpuestos

import matplotlib.pyplot as plt
import numpy as np

# Función para leer el archivo de datos
def leer_datos(filepath):
    # Lee los valores de absorbancia desde un archivo de texto. Se omiten las primeras líneas del espectro
    absorbancia = np.loadtxt(filepath)[:]
    return absorbancia

# Función para graficar los espectros
def graficar_espectros(file1, file2):
    # Leer datos de los archivos
    absorbancia1 = leer_datos(file1)
    absorbancia2 = leer_datos(file2)
    
    plt.rcParams['text.usetex'] = True

    longitud_onda = np.linspace(225, 400, len(absorbancia1))
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(longitud_onda, absorbancia1, color='blue', label=r'Norfloxacino')
    plt.plot(longitud_onda, absorbancia2, color='red', label=r'Sulfametoxazol')
    
    plt.xlabel(r'Longitud de onda (nm)')
    plt.ylabel(r'Absorbancia')
    #plt.title(r'Espectros de Absorción')
    
    plt.xticks(np.arange(225, 401, 25)) 
    plt.yticks(np.arange(0, max(max(absorbancia1), max(absorbancia2)) + 0.2, 0.2))
    
    plt.axvspan(242, 300, color='gray', alpha=0.3, label="Región de superposición")

    plt.legend()
    plt.grid(False)
    plt.show()

# Solicitar dirección archivos
archivo1 = input("Ingrese la ruta del archivo txt de la Sustancia 1: ")
archivo2 = input("Ingrese la ruta del archivo txt de la Sustancia 2: ")

graficar_espectros(archivo1, archivo2)
