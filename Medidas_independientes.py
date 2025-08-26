import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

# --- INGRESO DE DATOS DESDE TECLADO ---
entrada = input("Ingrese los datos separados por coma: ")
datos = [int(x) for x in entrada.split(",")]

# --- CÁLCULOS BÁSICOS ---
n = len(datos)
dato_min = min(datos)
dato_max = max(datos)
rango = dato_max - dato_min

k = round(1 + 3.322 * math.log10(n))  # Número de clases
amplitud = math.ceil(rango / k)

# --- VARIABLES PARA LA TABLA ---
clases = []
limites = []
marcas = []
frecuencias = []
frecuencia_acum = []
relativa = []
relativa_acum = []
porcentaje = []
porcentaje_acum = []

limite_inferior = dato_min
Fi = 0
Hi = 0.0
Pi = 0.0

# --- CONSTRUCCIÓN DE TABLA ---
for i in range(k):
    li = limite_inferior
    ls = li + amplitud - 1
    clase = i + 1
    xi = (li + ls) / 2
    fi = sum(1 for d in datos if li <= d <= ls)
    Fi += fi
    hi = round(fi / n, 4)
    Hi += hi
    pi = round(hi * 100, 2)
    Pi += pi

    clases.append(clase)
    limites.append(f"{li} - {ls}")
    marcas.append(round(xi, 2))
    frecuencias.append(fi)
    frecuencia_acum.append(Fi)
    relativa.append(hi)
    relativa_acum.append(round(Hi, 4))
    porcentaje.append(pi)
    porcentaje_acum.append(round(Pi, 2))

    limite_inferior = ls + 1

# --- MEDIDAS DE TENDENCIA CENTRAL ---
media = round(np.average(marcas, weights=frecuencias), 2)
mediana = statistics.median(datos)
moda = statistics.mode(datos)

# --- MEDIDAS DE VARIABILIDAD ---
varianza = round(np.average([(mc - media)**2 for mc in marcas], weights=frecuencias), 2)
desv_estandar = round(math.sqrt(varianza), 2)
coef_var = round((desv_estandar / media) * 100, 2)

# --- MOSTRAR TABLA DE FRECUENCIAS ---
print(f"\n{'Clase':<7}{'Li-Ls':<10}{'Xi':<8}{'fi':<5}{'Fi':<5}{'hi':<8}{'Hi':<8}{'pi':<8}{'Pi'}")
for i in range(k):
    print(f"{clases[i]:<7}{limites[i]:<10}{marcas[i]:<8}{frecuencias[i]:<5}{frecuencia_acum[i]:<5}"
          f"{relativa[i]:<8}{relativa_acum[i]:<8}{porcentaje[i]:<8}{porcentaje_acum[i]}")

# --- MEDIDAS DE TENDENCIA CENTRAL ---
print("\n--- Medidas de Tendencia Central ---")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# --- MEDIDAS DE VARIABILIDAD ---
print("\n--- Medidas de Variabilidad ---")
print(f"Varianza: {varianza}")
print(f"Desviación estándar: {desv_estandar}")
print(f"Coeficiente de variación: {coef_var}%")

# --- GRÁFICA ---
plt.bar(limites, frecuencias, color='skyblue', edgecolor='black')
plt.xlabel('Clases')
plt.ylabel('Frecuencia')
plt.title('Histograma de Frecuencias')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
