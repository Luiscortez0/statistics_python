import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Ingresar los datos
datos = list(map(int, input("Ingrese los datos separados por espacios: ").split()))

# Calcular medidas de tendencia central
media = np.mean(datos)
mediana = np.median(datos)

# Detectar todas las modas
conteo = Counter(datos)
max_frecuencia = max(conteo.values())
modas = [key for key, val in conteo.items() if val == max_frecuencia]

# Mostrar resultados
print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Moda(s): {', '.join(map(str, modas))}")

# Graficar las frecuencias
plt.bar(conteo.keys(), conteo.values(), color='yellow', alpha=0.7, label='Frecuencia')

# Agregar líneas para las medidas de tendencia central
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label='Media')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=2, label='Mediana')
for moda in modas:
    plt.axvline(moda, color='purple', linestyle='dashed', linewidth=2, label='Moda')

# Etiquetas y título
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de Frecuencia')
plt.legend()
plt.show()
