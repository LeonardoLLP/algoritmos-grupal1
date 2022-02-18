""" --- Algoritmo - Consulta ---
Algoritmo descuento_warner

Entrada:
    p: DECIMAL  # Precio original
    n: ENTERO   # Número de niños que tiene la familia

Salida: DECIMAL

precondición
    p, n > 0

poscondición
    si n = 1
        Resultado = 0
    si no si n = 2
        Resultado = 0.10 * p
    si no si n = 3
        Resultado = 0.15 * p
    si no
        Resultado = (0.18 + (n - 4)/100) * p

fin descuento_warner
"""