

print("Escribe la cantidad de productos que deseas\nPara salir precionar 0\n")

def ventas():
    lista = []
    
    while True:
        
        precio = float(input("ingresa el precio del item: "))

        lista.append(precio)
        
        """ if precio == 0:    
            break
        
        if precio >= 100000:
            print("venta destacada") """
        
        print(lista)


    
            


ventas()