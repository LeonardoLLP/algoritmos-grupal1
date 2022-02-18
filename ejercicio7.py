""" --- Algoritmo consulta ---
Algoritmo coste

Entrada:
    n: ENTERO  # Número de alumnos que van al viaje
    d: ENTERO  # Días de la salida
    para: CADENA  # Si es para todos o individual

Salida: DECIMAL

Precondición
    n > 0
    para = "todos" OR para = "uno"

Variables
    c: DECIMAL <-- 0  # Coste por alumno

Realización
    c += 3.50 * d

    si n <= 25:
        c += 67.30
    si no
        c += 61.00

    si n <= 30
        c += 4.75 * d
    si n <= 35
        c += 4.00 * d
    si no
        c += 3.50 * d

Poscondición
    si para = "todos"
        Resultado = c * n
    si no
        Resultado = c

fin coste
"""
