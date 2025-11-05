#ejemplo 1
print("Ejemplo 1")
door = True
if door:
    print("Entre a la casa")
else:
    print("No entre a la casa")

print("Fin del programa \n")

print("--------------------------------")

#Ejercicios 1
print("#Ejercicios 1")

num = int(input("Ingresa la cantidad de productos que deseas: "))

factura =[]

for i in range(num): 
    productos = str(input("Ingresa los productos: "))
    factura.append(productos)
    i +=1


print(factura) 