
#Lista o array donde se almacenará la información
Inventario =[]

#Función para agregar productos
def agregarProducto():


    while True: # Permite que cada uno de los productos se pidan nuevamente

        while True:
            
                nombreProducto = input("ingrese el nombre de un producto: ").lower()  #solicita un nombre y lo transforma a minusculas

                    #recorremos cada letra
                for letra in nombreProducto:
                    if letra in "áéíóú": #pregunta si la letra actual que esta recorriendo tiene tilde
                        print("No se permiten tildes")
                        break # En caso de tilde, sale del for y entra al while nuevamente para volver a pedir el nombre

                    elif not letra.isalnum() and letra != " ":  # verifica si hay datos alfanumericos o espacios de lo contrario no acepta nada
                        print("No se permiten caracteres especiales")
                        break # se sale del if

                else: # se ejecuta solo si el for continua, en este caso se pone para salir del while
                     break # sale del while
           


        # while True:
        #precioProducto = float(input("ingrese el precio del producto: ")) #datos flotantes o decimales
        #     if precioProducto > 0: # permite solo numeros mayores a 0, evitando negativos
        #         #precioProducto = round(precioProducto,2) #para evitar muchos desimales despues del punto
        #         break
        #     else:
        #         print("---- El precio no puede ser negativo o 0 -----\n") 
        while True:
            try:
                precioProducto = float(input("ingrese el precio del producto: "))
            
                if precioProducto > 0:
                    break                  
                else:
                    precioProducto = round(precioProducto,2)
            except ValueError:
                print("solo valores numericos")



        while True:
            cantidadProducto = int(input("Ingrese la cantidad: "))
            if cantidadProducto > 0:
                break
            else:
                print("---- El cantidad no puede ser negativo o 0 -----\n")

        #se crea un dicionario para pushearlo o ingresarlo dentro del inventario
        producto= {
        "nombre": nombreProducto,
        "precio": precioProducto,
        "cantidad": cantidadProducto
        }
        Inventario.append(producto) # se agrega el diccionario dentro de la lista o array
        print("\n ** ** ** Producto agregado correctamente! ** ** ** \n ")
        break

#funcion para mostrar el inventario
def mostrarInventario():
    if not Inventario:# veriffica si el inventario esta vacio
        print(" # * # * El inventario esta vacio * # * #")
    else:
        for i,producto in enumerate(Inventario, start = 1):#enumerate recorre una lista y me devuelve su key-value -- :.2findica que solo muestre 2 valores despues del punto
            print(f"{i} | El nombre del producto es {producto["nombre"]} | El valor es {producto["precio"]:.2f} | la cantidad es {producto['cantidad'] }\n   ")


def calcularEstadistica():
    if not Inventario:# confirmamos de nuevo que el inventario no este facio
        print("Inventario Vacio, por favor agregar productos.....")
    else:
       
        total = 0
        for i in Inventario: #recorre 
            total = total + (i["precio"] * i["cantidad"])
           

        print(f"la suma total de la factura es : {total} | ")


# def cerrarPrograma():
#     print("Nos vemos pronto")
#     break
#  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
while True:

    print("****************************************")
    selector = int(input(f"\n  1. Agregar producto\n  2.Mostrar inventario\n  3.Calcular estadísticas\n  4.Salir\n  --->"))
    print("****************************************")
    #try:
    if selector == 1:
        agregarProducto()
    elif selector == 2:
        mostrarInventario()
    elif selector== 3:
        calcularEstadistica()
    elif selector == 4:
        print("Nos vemos pronto")
        break
    else:
        print("Ingresar solo datos del 1 al 4")
    # except ValueError:
    #     print("ISolo SE PERMITEN NUMEROS")
