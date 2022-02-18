""" --- Algoritmo - Consulta ---
descuento(p: DECIMAL): DECIMAL
# OJO: Solamente calcula descuento. Ambigüedad en el enunciado
    precondición
        p >= 0

    poscondición
        si p > 500
            Resultado = 0.08 * p
        si no si p >= 100
            Resultado = 0.05 * p
        si no
            Resultado = 0

fin descuento
"""

def descuento(p: float):
    if p < 0:
        raise ValueError("Price cannot be below cero.")

    if p > 500:
        return 0.08 * p
    elif p >= 100:
        return 0.05 * p
    else:
        return 0