# Este algoritmo se realizaría muy eleganetemente con un tipo TABLA. Sin embargo,
# se realizará con los conocimientos obtenidos hasta ahora.

""" --- Algoritmo 1 - Consulta ---
tipo DÍA
    dominio = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"}
fin DÍA

sucesor_dia(d: DÍA): DÍA
    poscondición
        antiguo(d) = d

        si d = "lunes":
            Resultado = "martes"
        si no si d = "martes":
            Resultado = "miércoles"
        si no si d = "miércoles":
            Resultado = "jueves"
        si no si d = "jueves":
            Resultado = "viernes"
        si no si d = "viernes":
            Resultado = "sábado"
        si no si d = "sábado":
            Resultado = "domingo"
        si no:
            Resultado = "lunes"

fin sucesor_día
 """

# Aquí está la forma más elegante de hacerlo con código

semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
def sucesor_dia(d: str):
    if d.casefold() not in semana:
        raise ValueError("d must be a valid day of the week")

    index = semana.index(d)
    return semana[(index + 1) % 7]

print(sucesor_dia("martes"))