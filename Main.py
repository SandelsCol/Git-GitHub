import math
a=int(input("Digite A numero"))
b=int(input("Digite B numero"))
c=int(input("Digite C numero"))
d=int(input("Digite D numero"))

lol=b**2-(4*a*c)

Result= a*c
Doble= 2*a
Cuadrado = b**2
razo=math.sqrt(d)

print("El producto entre los numeros a y c es..",Result)
print("El doble del numero a es...",Doble)
print("El cuadrado del numero b es..",Cuadrado)
print("La raiz del numero d es..",razo)

if lol>0:
    x1=(-b+math.sqrt(lol))/2*a
    x2=(-b-math.sqrt(lol))/2*a
    print("Los dos valores son...",x1,x2) 
elif lol==0:
    x3=-b/2*a
    print("El valor de x es de..",x3)
else:
    print("No existe solución a la ecuación cuadrática dentro del dominio de los números reales")





