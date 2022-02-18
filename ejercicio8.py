""" --- Algoritmo - Consulta ---
Algoritmo prima

Entrada:
    d: ENTERO  # Distancia recorrida en kilometros
    n: ENTERO  # Años de antigüedad
    a: ENTERO  # Accidentes
    damage: DECIMAL  # Dinero invertido en accidentes

Salida: DECIMAL

Variables
    p: DECIMAL <-- 0  # Prima

Realización
    si d >= 40_000
        p += 400.00
    si no
        p += 0.01 * d

    si n >= 4
        p += 200.00 + 20.00 * (n-4)

    si damage < 0.20 * p:
        nada
    si no
        si a = 1
            p <-- p/2
        si no si a = 2
            p <-- p/3
        si no si a = 3
            p <-- p/4
        si no
            p = 0

Poscondición
    Resultado = p

fin prima
"""