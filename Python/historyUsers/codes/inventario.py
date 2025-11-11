

#ingreso de los datos y sus tipos
nombre = input("ingresa el nombre del producto: ")

while True:
    try:
        precio = float(input("Ingresar el precio: "))
        if precio > 0: #Validar que el precio sea un número positivo
            break #Si se cumple, sale del bucle dandole continuidad al código
        else: 
            print("------\n El precio debe ser un número positivo\n --------")
    except ValueError:
        print("Escribir un valor válido para este campo")

while True:
    try:
        cantidad = int(input("ingrese la cantidad a comprar: "))
        if cantidad > 0: #Validar que el precio sea un número positivo
            break #Si se cumple, sale del bucle dandole continuidad al código
        else: 
            print("------\n El precio debe ser un número positivo\n --------")
    except ValueError:
        print("Escribir un valor válido para este campo")

costo_total = precio * cantidad

print("----------------------")
print(" ----- La Factura es ------")
print("----------------------")
print(f'Nombre del producto : {nombre} | Precio unitario : {precio} | Cantidad : {cantidad} | Costo total calculado : {costo_total}')