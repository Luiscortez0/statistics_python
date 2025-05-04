def op_media(*n: int) -> float:
    """
        Function that receives an "N" amount of integer 
        values and returns the average.

        Usage:
        op_media(1, 2, 3)

        Output:
        2.0
    """
    suma = sum(n)
    promedio = suma / len(n)
    return promedio


def op_mediana(*n: int) -> float:
    """
        Function that receives an "N" amount of integer 
        values and returns the arithmetic median.

        Usage:
        op_mediana(4, 2, 7, 1, 5, 6, 3)

        Output:
        4
    """
    l_o = sorted(n)
    if len(l_o) % 2 == 0:
        mediana = (l_o[int(len(l_o)/2) - 1] + l_o[int(len(l_o)/2)]) / 2
    else:
        mediana = l_o[int(len(l_o)/2)]
    return mediana


def op_moda(*n: int) -> int:
    """
        Function that receives an "N" amount of integer 
        values and returns the arithmetic mode.

        Usage:
        op_moda(5, 8, 9, 6, 4, 5, 5, 9, 9, 9, 9, 9)

        Output:
        9
    """
    variablemoda = None
    variablecantidad = 0
    for numero in n:
        cantidad_actual = n.count(numero)
        if cantidad_actual > variablecantidad:
            variablecantidad = cantidad_actual
            variablemoda = numero
    return variablemoda


def op_frecuencia(*n: int) -> dict:
    """
        Function that receives an "N" amount of integer 
        values and returns the frequency of each one.

        Usage:
        op_frecuencia(5, 8, 9, 6, 4, 5, 5, 9, 9, 9, 9, 9)

        Output:
        {5: 3, 8: 1, 9: 6, 6: 1, 4: 1}
    """
    frecuencias = {}
    for numero in n:
        frecuencias[numero] = frecuencias.get(numero, 0) + 1
    return frecuencias

# Pruebas
print("Media:", op_media(1, 2, 3))
print("Mediana:", op_mediana(4, 2, 7, 1, 5, 6, 3))
print("Moda:", op_moda(5, 8, 9, 6, 4, 5, 5, 9, 9, 9, 9, 9))
print("Frecuencia:", op_frecuencia(5, 8, 9, 6, 4, 5, 5, 9, 9, 9, 9, 9))
