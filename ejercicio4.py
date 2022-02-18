#EJERCICIO 4:
#1)datos de entrada:numeros enteros entre 0 y 20.
#2)introducir las cuatro notas,almacenarlas en cuatro variables distintas
#3)sumar las cuatro notas y dividirlas entre cuatro y almacenar ese valor en una variable,la llamare m
#4)Comparar dicho resultado:
#	si m>15 el resultado final es:Alumno con talento
#	si 12<=m<=15 el resultado final es:alumno con capacidad
#	si m<12 el resultado final es:debe reorientarse

#  El codigo en python:

print("introduce las 4 notas entre 0 y 20")
a=int(input("nota:"))
b=int(input("nota:"))
c=int(input("nota:"))
d=int(input("nota:"))
suma_notas=a+b+c+d
media_nota=suma_notas/4
if media_nota>15:
    print("Alumno con talento")
elif 12<=media_nota<=15:
    print("Alumno con capacidad")
else:
    if media_nota<12:
        print("El alumno debe reorientarse")
