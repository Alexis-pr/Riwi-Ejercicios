
listadoRecetas =[{
    "nombre" : "Carne",
    "ingredientes" : {},
    "pasos" :   "calentar una sarte, echar la carne y condimentar al gusto"
}]

# creo la funcion para guardar 
def guardarReceta (nombre,ingredientes,pasos): # le paso varios parametros
    guardar ={
        "nombre" : nombre,
        "ingredientes" : ingredientes,
        "pasos" : pasos
    }

    listadoRecetas.append(guardar)
    print("✅ Libro agregado correctamente.\n")



def agregarRecetas():
    ingredientes = {}

    while True:
        nombreReceta = input("Ingrese el nombre de la receta: \n ")
        if nombreReceta:
            break
        print("El nombre no puede estar vacío.") 

    while True:
        agregar = input("¿Desea agregar un ingrediente? (si/no): ").lower()

        if agregar == "si":
            nombreIngrediente = input("Nombre del ingrediente: ").strip()
            cantidadIngrediente = input("Cantidad: ")

            ingredientes[nombreIngrediente] = cantidadIngrediente  # ← se agregan al diccionario a ingredientes
        elif agregar == "no":
            break
    
        else:
            print("Responda solo con 'si' o 'no'.")    


    while True:
        pasos = input("Ingrese los pasos de la receta: \n")
        if pasos:
            break
        print("tienes que escribir el paso a paso de la receta")

    
    # receta={
    #     "nombre" : nombreReceta,
    #     "ingredientes" : ingredientes,
    #     "pasos" : pasos,
    #     " nose" : {}
    # }

    guardarReceta(nombreReceta,ingredientes,pasos)


    

def mostrarReceta():
    if not listadoRecetas:
        print("No hay recetas disponibles")
    else:
        for i, receta in enumerate(listadoRecetas,start=1):
            print(f"- Receta #{i}\n- Nombre de la receta: {receta['nombre']}")
            print("- Ingredientes: ")

            if receta["ingredientes"]:
                for ingrediente, cantidad in receta["ingredientes"].items():
                    print(f" - {ingrediente} : {cantidad}")
            else:
                    print(" Sin ingredientes: ")     

            print("Pasos:")
            print(f"     {receta['pasos']}")
            print("-" * 40)

def eliminarReceta():
    print("*" * 40)
    print("Elije la receta que deseas eliminar")
    print("*" * 40)
    mostrarReceta()
    print("\n")
    if not listadoRecetas:
        print("no hay recetas disponibles")
        return

    for i, receta in enumerate(listadoRecetas, start=1):
        print(f" Receta# {i}\n Nombre de la receta: {receta["nombre"]}")
    
    try:
        opcion = int(input("\nIngrese el número de la receta a eliminar: "))

        if opcion < 1 or opcion > len(listadoRecetas):
            print("❌ Número fuera de rango.")
            return
        
    except:
        print("❌ Debe ingresar un número válido.")
        return

    recetaEliminada = listadoRecetas.pop(opcion - 1)
    print(f"\n🗑️ Receta eliminada: {recetaEliminada['nombre']}.\n")


while True:
    print("\n======= MENU =======")
    print("1. Agregar receta")
    print("2. Mostrar recetas")
    print("3. Elimitar receta")
    print("4. Salir\n")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregarRecetas()
    elif opcion == "2":
        mostrarReceta()
    elif opcion == "3":
        eliminarReceta()
           
    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("❌ Opción no válida.")