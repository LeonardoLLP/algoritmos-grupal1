""" --- Algoritmo - Consulta ---
Algoritmo prima

Entrada:
    d: ENTERO  # Distancia recorrida en kilometros
    n: ENTERO  # Años de antigüedad
    a: ENTERO  # Accidentes
    damage: DECIMAL  # Dinero invertido en accidentes

Salida: DECIMAL

Precondición
    a, d, n >= 0
    damage >= 0

Variables
    p: DECIMAL <-- 0  # Prima

Realización
    si d >= 40_000
        p += 400.00
    si no
        p += 0.01 * d

    si n >= 4
        p += 200.00 + 20.00 * (n-4)

    si damage < 0.20 * p
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

def prima(d: int, n: int, a: int, damage: float):
    if a < 0 or d < 0 or n < 0:
        raise ValueError("a, d and n must be greater than or equal to cero")
    if damage < 0:
        raise ValueError("Damage cannot drop below cero.")

    p = 0

    if d >= 40_000:
        p += 400.00
    else:
        p += 0.01 * d

    if n >= 4:
        p += 200.00 + 20.00 * (n-4)

    if damage < 0.20 * p:
        pass
    else:
        if a == 1:
            p /= 2
        elif a == 2:
            p /= 3
        elif a == 3:
            p /= 4
        else:
            p = 0

    return p