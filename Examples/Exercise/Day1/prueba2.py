print(" Elija la opción 1 para convertir de decimal a binarios \n Elija la opcion2 para convertir de binarios a decimal ")
opcion = int(input("Elegir opción: "))
numero  = int(input("ingresa el numero: "))

binario = ""
conversion = 0

if opcion == 1:

    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    print(binario)
elif opcion == 2:
     
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2

    for i in range(len(binario)):   
        bit = int(binario[-(i+1)])
        conversion = conversion + bit * (2 ** i)

    print(f'La conversión es: ', conversion , ' y su binario es: ', binario)

else:   
    print("ingrese alguna de las dos opciones")