import numpy as np
import matplotlib.pyplot as plt

# Ingresar los datos
datos = list(map(float, input("Ingrese los datos separados por espacios: ").split()))

# Calcular medidas de variabilidad
media = np.mean(datos)
rango = np.max(datos) - np.min(datos)
varianza = np.var(datos, ddof=1)  # ddof=1 para la varianza muestral
desviacion_estandar = np.std(datos, ddof=1)
coef_variacion = (desviacion_estandar / media) * 100
desviacion_media = np.mean(np.abs(datos - media))

# Mostrar resultados
print(f"\nMedia: {media:.2f}")
print(f"Rango: {rango:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")
print(f"Coeficiente de Variación: {coef_variacion:.2f}%")
print(f"Desviación Media: {desviacion_media:.2f}")

# Graficar la distribución de datos
plt.hist(datos, bins=10, color='yellow', alpha=0.7, edgecolor='black', label='Datos')

# Agregar líneas para las medidas de variabilidad
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label='Media')
plt.axvline(media - desviacion_estandar, color='green', linestyle='dashed', linewidth=2, label='-1σ')
plt.axvline(media + desviacion_estandar, color='green', linestyle='dashed', linewidth=2, label='+1σ')

# Etiquetas y título
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de Datos y Medidas de Variabilidad')
plt.legend()
plt.show()
