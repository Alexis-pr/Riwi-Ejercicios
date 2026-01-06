Inventario =[]
def agregarProducto():

    while True: # Permite que cada uno de los productos se pidan nuevamente
              
        while True:       
                nombreProducto = input("ingrese el nombre de un producto: ").lower()  #solicita un nombre y lo transforma a minusculas               
                for letra in nombreProducto:
                    if letra in "áéíóú": 
                        print("No se permiten tildes")
                        break 

                    elif not letra.isalnum() and letra != " ":  
                        print("No se permiten caracteres especiales")
                        break 
                else: # se ejecuta solo si el for continua, en este caso se pone para salir del while
                     break # sale del while
       
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
            cantidadProducto = input("Ingrese la cantidad: ")
            if cantidadProducto.isdigit():
                
                cantidadProducto = int(cantidadProducto)
                if cantidadProducto > 0:
                    
                    break
                else:
                    print("---- El cantidad no puede ser negativo o 0 -----\n")
            else:
                print("ingresar numeros sin decimal")
        #se crea un dicionario para pushearlo o ingresarlo dentro del inventario
        guardar(nombreProducto,precioProducto,cantidadProducto)
        break


def guardar(nombre,producto,cantidad):
    producto= {
            "nombre": nombre,
            "precio": producto,
            "cantidad": cantidad
            }
    Inventario.append(producto) # se agrega el diccionario dentro de la lista o array
    print("\n ** ** ** Producto agregado correctamente! ** ** ** \n ")


def mostrarInventario():
    if not Inventario:# veriffica si el inventario esta vacio
        print(" # * # * El inventario esta vacio * # * #")
    else:
        for i,producto in enumerate(Inventario, start = 1):#enumerate recorre una lista y me devuelve su key-value -- :.2findica que solo muestre 2 valores despues del punto
            print(f"- Id - {i} | El nombre del producto es: {producto["nombre"]} | El precio es: {producto["precio"]:.2f} | la cantidad es: {producto['cantidad'] }")
    print("\n")

    
def buscar():
    
    try:
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        else:
            mostrarInventario()
            id_buscar = int(input("Ingrese el ID del producto a buscar: "))
            if 1 <= id_buscar <= len(Inventario):
                producto = Inventario[id_buscar - 1]  #resta 1 para ajustar al indice de la lista
                print(f"El producto encontrado es: {producto['nombre']} | Precio: {producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
            else:
             print("ID de producto no válido.")
    except ValueError:
        print("ID invalido. Por favor ingrese un numero valido.")
            
def actualizar():
    try:
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        elif Inventario:
           
            opción= input("¿Qué desea actualizar? (nombre/precio/cantidad): ").lower()

            mostrarInventario()
            if opción == "nombre":
                id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
                if 1 <= id_actualizar <= len(Inventario):
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").lower()
                    Inventario[id_actualizar - 1]['nombre'] = nuevo_nombre
                    print("Nombre actualizado correctamente.")
                else:
                    print("ID de producto no válido.")
            elif opción == "precio":
                id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
                if 1 <= id_actualizar <= len(Inventario):
                    nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                    Inventario[id_actualizar - 1]['precio'] = nuevo_precio
                    print("Precio actualizado correctamente.")
                else:
                    print("ID de producto no válido.")
            elif opción == "cantidad":
                id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
                if 1 <= id_actualizar <= len(Inventario):
                    nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                    Inventario[id_actualizar - 1]['cantidad'] = nueva_cantidad
                    print("Cantidad actualizada correctamente.")
                else:
                    print("ID de producto no válido.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un valor válido.")  

def eliminar():
    try: 
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        else:
            mostrarInventario()

            eliminar_id = int(input("Ingrese el ID del producto a eliminar: "))
            if 1 <= eliminar_id <= len(Inventario):
                Inventario.pop(eliminar_id - 1)  #resta 1 para ajustar al indice de la lista
                print("Producto eliminado correctamente.")
    except ValueError:
        print("ID invalido. Por favor ingrese un numero valido.")

def calcularEstadistica():
    try:
        if not Inventario:
            print(" # * # * El inventario esta vacio * # * #")
        else:
            total_productos = len(Inventario)
            valor_total_inventario = 0
            for producto in Inventario:
                valor_total_inventario += (producto['precio'] * producto['cantidad'])

            producto_mas_caro =max(Inventario,key = lambda x:x['precio'])
            
            producto_mas_barato = min(Inventario, key=lambda x: x['precio'])    
            
            print(f"Total de productos en el inventario: {total_productos}")
            print(f"Valor total del inventario: {valor_total_inventario:.2f}")
            print(f"Producto más caro: {producto_mas_caro['nombre']} | Precio: {producto_mas_caro['precio']:.2f}")
            print(f"Producto más barato: {producto_mas_barato['nombre']} | Precio: {producto_mas_barato['precio']:.2f}")
            

     
    except ValueError:
        print("Error al calcular estadísticas. Por favor, verifique los datos del inventario.")



def validarProductosCsv(producto):
    # --- Validar nombre ---
    nombre = producto.get('nombre')
    if nombre is None or not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío, ser None ni contener solo espacios.")

    # --- Validar precio ---
    precio = producto.get('precio')
    if precio is None:
        raise ValueError("El precio no puede ser None.")
    if isinstance(precio, str):  # si viene como string
        if precio.strip() == "":
            raise ValueError("El precio no puede estar vacío.")
        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un número válido.")
    if not isinstance(precio, (int, float)):
        raise ValueError("El precio debe ser numérico.")

    # --- Validar cantidad ---
    cantidad = producto.get('cantidad')
    if cantidad is None:
        raise ValueError("La cantidad no puede ser None.")
    if isinstance(cantidad, str):
        if cantidad.strip() == "":
            raise ValueError("La cantidad no puede estar vacía.")
        if not cantidad.isdigit():
            raise ValueError("La cantidad debe ser un número entero.")
        cantidad = int(cantidad)
    if not isinstance(cantidad, int):
        raise ValueError("La cantidad debe ser un entero.")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    # Devolver datos limpios y corregidos
    return {
        "nombre": nombre.strip(),
        "precio": float(precio),
        "cantidad": cantidad
    }


def guardarCsv():

    import csv # permite trabajar con los archivos csv
    import os # permite trabajar con rutas y archivos del sistema operativo

    if not Inventario: # valido si el inventario esta vacio
        print(" # * # * El inventario esta vacio * # * #")
        return 
    
    carpeta = "csv" # nombre de la carpeta donde se guardara el archivo
    ruta_base = os.path.dirname(os.path.abspath(__file__)) #toma el directorio actual y genera el puntero a esa ruta
    ruta_carpeta = os.path.join(ruta_base, carpeta)# obtiene la ruta completa de la carpeta
    ruta_archivo= os.path.join(ruta_carpeta,"inventario.csv")# une la ruta de la carpeta con el nombre del archivo


    if not  os.path.exists(ruta_carpeta):# verifica si la carpeta no existe
        os.mkdir(ruta_carpeta)# crea la carpeta
    

    #existe = os.path.exists(ruta_archivo)
    if os.path.exists(ruta_archivo):# verifica si el archivo ya existe
        print("El archivo inventario.csv ya existe y será sobrescrito.")
        modo = "a"
    else:
        modo = "w"

    # existe = os.path.exists(ruta_archivo)
    # if existe:
        #print("El archivo inventario.csv ya existe y será sobrescrito.")
    # modo = "a" if existe else "w"  #Usando operador ternario
    
    with open(ruta_archivo, mode=modo, newline='') as archivo_csv:# abre el archivo en modo escritura
            campos = ['nombre', 'precio', 'cantidad']# nombres de las columnas del archivo csv
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)# crea un objeto escritor de diccionarios
            if modo == "w":
                escritor.writeheader()# escribe los nombres de las columnas en el archivo

            for producto in Inventario:
                producto_validado = validarProductosCsv(producto) # genera una funcion que valida que los datos en el csv no vengan vacios o comas o algo extraño
                escritor.writerow(producto_validado)
                #AUSPICIADO POR CHATGPT XD
                # nombre = str(producto.get('nombre', '')).strip() # toma el cambo y evita que se escriba sin espacios
                # precio = producto.get('precio')
                # cantidad = producto.get('cantidad')

                # if not nombre: # si no hay nombre, que muestre un error
                #     raise ValueError("El nombre no puede estar vacío ni contener solo espacios.")

                # if precio is None or precio == "" or not isinstance(precio, (int, float)):
                #     raise ValueError("El precio no puede estar vacío y debe ser numérico.")

                # if cantidad is None or cantidad == "" or not isinstance(cantidad, int):
                #     raise ValueError("La cantidad no puede estar vacía y debe ser un número entero.")

                # escritor.writerow({
                #     'nombre': nombre,
                #     'precio': precio,
                #     'cantidad': cantidad
                # })
            
    print("Inventario guardado en inventario.csv correctamente.")
        


def cargarcsv():
    import csv
    import os

    ruta_base = os.path.dirname(os.path.abspath(__file__))

    carpeta = os.path.join(ruta_base, "csv")# obtiene la ruta completa de la carpeta
    nombre = input("como se llama el archivo (con la extención .csv): ")# nombre del archivo
    ruta = os.path.join(carpeta, nombre)# une la ruta de la carpeta con el nombre del archivo
    ruta_log = os.path.join(carpeta, "filas_invalidas.txt")

    try:
        with open(ruta, mode='r', newline='') as archivo_csv:# abre el archivo en modo lectura          
            with open(ruta_log, mode='w', encoding='utf-8') as archivo_log:
                
                lector = csv.DictReader(archivo_csv)# crea un objeto lector de diccionarios
                #Inventario.clear()  # Limpiar el inventario actual antes de cargar nuevos datos                

                for i,fila in enumerate(lector, start=2): # recorre cada uno de los datos del csv y los asigna a i y fila
                #for fila in lector:# recorre cada fila en el archivo
                    # producto = {# crea un diccionario con los datos de la fila
                    #     'nombre': fila['nombre'],
                    #     'precio': float(fila['precio']),
                    #     'cantidad': int(fila['cantidad'])
                    # }
                    producto = {   # con .get se toma los valores adquiridos por fila y se anexa a un diccionario
                        'nombre' : fila.get('nombre'),
                        'precio' : fila.get('precio'),
                        'cantidad' : fila.get('cantidad')
                    }
                    try:
                        validarProducto = validarProductosCsv(producto) # se utiliza la funcion validar productos antes de cargarlos en el inventario y mostrarlos
                        Inventario.append(validarProducto)# agrega el producto al inventario
                        
                    except ValueError as e:
                        archivo_log.write(f"Fila {i}: {fila} -> Error: {e}\n")
                        print(f"Fila {i} inválida y registrada en el log: {e}")
                        #print(f"Fila {i} inválida y omitida: {e}") # muestra el error en pantalla de los datos ignorados
                

            print(f"Inventario cargado desde {ruta} correctamente.")


    except FileNotFoundError:# si el archivo no existe
        print(f"El archivo no existe.")