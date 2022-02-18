#EJERCICIO 6:
#1)datos de entrada:c=cantidad de componentes,a=nombre del cliente,
  #datos de salida:d=descuento,t=total a pagar sin descuento,p=precio final
#2)comparar el valor de c:
	#si 10000<=c<=20000 implica que d=10
	#si 20001<=c<=40000 implica que d=15 
	#si c>40000 implica que d=2
#3)si a==COMMAQ implica d=d-2
  #si a==BEL implica d=d+1
 #4)porcentaje=100*d 
#5)p=t*porcentaje

#El codigo sería:

c=int(input("cantidad de componentes"))
a=input("nombre del cliente")
if 10000<=c<=20000:
    d=10
elif 20001<=c<=40000:
    d=15
else:
    if c>40000:
        d=20
if a=="COMMAQ":
    d=d-2
else:
    if a=="BEL":
        d=d+1
porcentaje=100*d
precio_sin_descuento=input("Introduzca lo que cuesta")
total_a_pagar=precio_sin_descuento=precio_sin_descuento*porcentaje
