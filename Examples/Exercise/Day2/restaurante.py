
# Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

menu = 12000
iva = 0.08

bebida = input("Deseas una bebida? \n")

if bebida.lower() == "si" or bebida == True:
    subtotal = menu + 3000 
    total = subtotal+(subtotal * iva)
    print(" el valor con iva incluido es: ", total)
else:

    total = menu + (menu * iva)
    print("intento raro" , total)



