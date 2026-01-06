from Inventory import *



while True:

    print("****************************************")
    selector = int(input(f"\n 1.Add books\n 2.Consult books \n 3.update books\n 4.delete books\n 5.add customer\n 6.reports\n 9.Salir\n  ---> "))
    print("****************************************")
    try:
        if selector == 1:
            addBooks()
        elif selector == 2:
            consultbooks()
        elif selector== 3:
            updatebooks()
        elif selector == 4:
            deletebooks()
        elif selector == 5:
            addsales()
        elif selector == 6:
           reports()    
        # elif selector == 7:
        #     guardarCsv()
        # elif selector == 8:
        #     cargarcsv()
        elif selector == 9:
            print("Saliendo ... ")
            break    
        # else:
        #     print("Ingresar solo datos del 1 al 9")
    except ValueError:
            print("Solo SE PERMITEN NUMEROS")


        