edad = int(input("Ingrese su edad "))

if edad <= 0:
    print("Edad invalida")

elif edad < 5:
    print("Su entrada es gratis")

elif edad >= 5 and edad <= 11:
    print("Su entrada tiene un valor de 5000")

elif edad >= 12 and edad <= 59:
    print("Su entrada tiene un valor de 8000")

else:
    print("Su entrada tiene un valor de 4000 (descuento adulto mayor)")


