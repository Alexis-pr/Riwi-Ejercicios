# mis dos arrays donde se almacenaran mi información
biblioteca = []
historial = []

#funcion que utilizo para guardar mi información
def guardar(nombreLibro,nombreCategoria,disponibilidad): # toma los parametros que le entran a la funcion
    

    guardar = {
                "nombre" : nombreLibro,
                "categoria" : nombreCategoria,
                "disponible" : disponibilidad           
    }  

    biblioteca.append(guardar) #guardo el diccionario dentro de la lista
    print("✅ Libro agregado correctamente.\n")

# función que utilizo para pedir al usuario mis información sobre la pelicula a guardar
def agregarLibros():

        #ejecuto el while mientras la información es correcta
        while True:
                nombreLibro = input("Ingrese el libro: ").lower() # solicito el valor por el usuario
                if nombreLibro:
                    break
                print("guardado")
                    
        while True: # solicito la categoria por el usuario
            nombreCategoria = input("Ingrese la categoria: ").lower()
            if nombreCategoria:
                print("guardadooo")
                break
            else:
                print("libro esta vacio")
                    
        while True: # ingreso la disponibilidad por teclado como control de version o estado de forma manual
            disponibilidad = input("Ingrese la disponibilidad ( SI O NO ): ").lower()
            # if disponibilidad == "si":
            if disponibilidad  in ("si","no"):
                print("Se puede prestar")
                break
            else:
                print("❌ Valor inválido. Debe escribir exactamente 'si'. Intente de nuevo.")   
      
        guardar(nombreLibro,nombreCategoria, disponibilidad) # le paso los datos a la funcion para generar el guardado
        
       

#función que utilizo para actualizar el estado, pendiendo la disponibilidad del libro a prestar
def estado(libro):
    #verifico el estado
    if libro["disponible"] == "si": # asigno el estado libre, siempre y cuentado su disponibilidad sea SI
         libro["estado"] = "Libre"
    else:
        libro["estado"] = "Prestado" # asigno el estado de prestado siempre y cuando no este disponible
    return libro["estado"]


# la función que utilizo para  generar el prestamo el libro
def prestarLibro():
    print("\n ¿Cual deseas prestar?") 
    print("---------------------------------------------------------------------")
    verLibros() # imprimo los libros disponibles
    if not biblioteca: # en caso de que no tenga datos biblioteca retorno un false
        return
    
    try:
        num =int(input("\nIngrese el numero del libro a prestar: "))
        libro = biblioteca[num - 1] # coloco el -1 ya que si no este iniciaria el conteo en 0
    except:
        print("numero invalido")# en caso de que ingresen un numero fuera del rango de la lista o del contador 
        return    


    if libro["disponible"] =="no": #se consulta la disponibilidad o estado del libro, si esta en no, no hay nada que prestar
        print("el libro no esta disponible o ya se encuentra prestado")
    else:
        libro["disponible"] = "no" # en caso de que el valor este en no, se actualiza el estado
        estado(libro)# actualiza el estado a si -> que sera igual a disponible para prestar
        historial.append(f"Prestado: {libro["nombre"]}") # guarda el libro en el historial
        print(f"Libro prestado correctamente. estado actual: {libro['estado']}")# muestra el estado del lubro prestado

def devolverLibro():
    verLibros()
    if not biblioteca: # se verifica la disponibilidad de la lista de la biblioteca 
        return
    
    try:
        num = int(input("ingresar el numero del libro a devolver: ")) #ingresa  un numero del libro o lista a eliminar
        libro = biblioteca[num - 1] #se le resta 1 al numero ingresado por el usuario para poder buscarlo en el indice
    except:
        print("numero invalido")

    
    if libro["disponible"] == "si":# se busca la disponibilidad y si es exactamente igual a si, pues el libro ya esta prestado
        print("el libro esta disponible, No es necesario devolver nada...")
    else:
        libro["disponible"] = "si" #se valida
        estado(libro) # se actualiza a no
        historial.append(f"Devuelto: {libro['nombre']}")# se duelve el libro y se muestra en consola
        print(f"Libro se ha devuelto exitosamente... \nestado actual: {libro['estado']}")



#funcion que utilizo para mostrar la lista de libros
def verLibros():
    
    if not biblioteca:
        print("  lista de libros vacia  ")
    else:
        
        for i,libro in enumerate(biblioteca, start=1):# se recorre  el libro o la lista monstrando los datos disponibles
            print(f"{i} | Nombre del libro = {libro['nombre']} | Genero = {libro['categoria']} | disponibilidad = {libro['disponible']} | estado_actual = {estado(libro)}")
            

def verHistorial():
    print("este es el historial: ")
    
    if not historial:
        print("NO HAY REGISTROS...... ")
        return
    
    for h in historial:
        print(" ---- --- --- ----" + h) # se recorre el historial mostrando los libros según su estado


# el menu
while True:
    try:
        print("****************************************")
        selector = int(input(
            "\n  1. Agregar Libro\n"
            "  2. Mostrar Libros\n"
            "  3. Prestar Libro\n"
            "  4. Devolver Libro\n"
            "  5. Ver Historial\n"
            "  6. Salir\n  ---> "))
        print("****************************************")

    except ValueError:
        print("Solo se permiten números.")
        continue

    if selector == 1:
        agregarLibros()
    elif selector == 2:
        verLibros()
    elif selector == 3:
        prestarLibro()
    elif selector == 4:
        devolverLibro()
    elif selector == 5:
        verHistorial()
    elif selector == 6:
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese solo números del 1 al 6.")