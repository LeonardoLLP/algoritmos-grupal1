""" --- Algoritmo - Consulta ---
Algoritmo descuento_warner

Entrada:
    p: DECIMAL  # Precio original
    n: ENTERO   # Número de niños que tiene la familia

Salida: DECIMAL

precondición
    p > 0
    n >= 0

poscondición
    si n < 2
        Resultado = 0
    si no si n = 2
        Resultado = 0.10 * p
    si no si n = 3
        Resultado = 0.15 * p
    si no
        Resultado = (0.18 + (n - 4)/100) * p

fin descuento_warner
"""

def descuento_warner(p: float, n: int):
    if p <= 0:
        raise ValueError("Price can't less or equal to cero.")
    if n < 0:
        raise ValueError("Number of children can't be negative")

    if n < 2:
        return 0
    elif n == 2:
        return 0.10 * p
    elif n == 3:
        return 0.15 * p
    else:
        return (0.18 + (n - 4)/100) * p