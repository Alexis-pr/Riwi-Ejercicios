
#5. Librería “El Saber” — Descuento estudiante + cupón

libro = 25000
descu_estu= 0.15
cupon = "LIBRO10"

persona = input("Eres estudiante? SI o NO \n")

""" if persona.lower() == "si" or persona == True:
    res = libro - (libro * descu_estu)
    print(res)
else:
    res = libro
    print(res) """
    


if persona.lower() == "si" or persona == True:
    res = libro - (libro * descu_estu)

    cupon_des = input("Si tienes algún cupon escribelo... \n")

    if cupon_des == cupon:
        total = res - (res *0.10) 
        print(f"El valor a pagar es: {total}")
    else:
         print("Cupon invalido")
         print("Valor a pagar es:" , res)

else:
    res = libro
    print(res)






