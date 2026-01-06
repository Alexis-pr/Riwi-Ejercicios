
inventario = []
ventas = []
def agregar():

    try:
        id = int(input("agregar id: "))
        nombreLibro =  input("nombre libro: ")
        autor = input("nombre autor: ")
        cantidad = int(input(" cantidad Libro: "))
        precio = float(input(" precio:  \n"))


        guardar(id,nombreLibro,autor,cantidad,precio)

    except:
        print("genera fallo")    



def guardar(id,nombre,autor,cantidad,precio):

    vari ={
        "id" : id,
        "nombreLibro" : nombre,
        "autor" : autor,
        "cantidad" : cantidad,
        "precio" : precio
    }

    inventario.append(vari)

def mostrar():
    if not inventario:
        print("esa vaina esta vacia")
    else:
        for i in inventario:
            

            print(f"el id del libro es: {i["id"]}")
            print(f"el libro es: {i["nombreLibro"]}")
            print(f"el autor es: {i["autor"]}")
            print(f"el cantidad es: {i["cantidad"]}")
            print(f"el precio es: {i["precio"]}\n")

def eliminar():
    if not inventario:
        print("esta mierda esta sola")
    else:
        dele= int(input("que id desea borrar"))
         
        for i,st in enumerate(inventario):
            if st["id"] == dele:
                inventario.pop(i)
                print("eliminado")
                break
                
        else:
            print("esa monda no existe")

def actualizar():

    if not inventario:
        print("esta mierda esta sola")
    else:

        ad = input("ingrese el id a actualizar: ")

        for i in inventario: 
            if str(i["id"]) == ad:
                opcion = input("ingrese que desea actualizar: ").lower()
            
                if opcion == "nombreLibro":

                    nueva = input("ingrese el nuevo valor: ")
                    i["nombreLibro"] = nueva
                    print("-- actualizado --")

                elif opcion == "autor":

                    nueva = input("ingrese el nuevo valor: ")
                    i["autor"] = nueva
                    print("-- actualizado --")

                elif opcion == "cantidad":

                    nueva = int(input("ingresa la nueva cantidad: "))
                    i["cantidad"] = nueva
                    print("-- actualizado --")

                elif opcion == inventario["precio"]:

                    nueva = float(input("ingresar el nuevo valor: "))
                    i["precio"] = nueva
                    print("-- actualizado --")

                else:
                    print("no existe")       
                break
        else:
            print("XD")   


def  agregar():

    cliente = input("ingrese nombre del cliente: ")
    cont = input("cuantos quiere comprar: ")
    descu =0

    if












# agregar()
# mostrar()
# eliminar()
# actualizar()
# mostrar()