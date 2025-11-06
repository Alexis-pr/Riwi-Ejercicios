
# se muestra las constantes

chocolate = 4000
vainilla = 3500
topping = 1000

#se pide el sabor del helado
sabor = input("ingrese un sabor de helado, disponibles de \nchocolate \nvainilla \n ¿cual deseas? \n")


#se valida si hay sabor del helado disponibles
if sabor.lower() == "chocolate" or sabor.lower() == "vainilla":

    # se pregunta si desea un topic
    adicion = str(input(" deseas incluir el topic adicional Si o No\n"))

    # se valida y se transforma a minusculas y en caso de que el cliente quiere adiciones
    if adicion.lower() == "si" or adicion == True:

        # se cacula el sabor de helado = chocolate con adiciones
        if sabor.lower() == "chocolate":
            valor_helado = chocolate + topping
            print( f" el valor es: {valor_helado}")

        # se cacula el sabor de helado = vainilla con adiciones
        elif sabor.lower() == "vainilla":
            valor_helado = vainilla + topping
            print( f" el valor es: {valor_helado}")     
                  
    # se calcula en caso de que no desee adiciones con chocolate
    elif adicion.lower() == "no" or adicion == False:
        valor_helado = chocolate
        print(f"El helado va sin adicionales para un total de {valor_helado}")

    # se calcula en caso de que no desee adiciones con chocolate
    elif adicion.lower() == "no" or adicion == False:
        valor_helado = vainilla
        print(f"El helado va sin adicionales para un total de {valor_helado}")

 # por si pide un sabor no disponible       
else:
    print("NO esta disponible ese sabor de helado")



 



