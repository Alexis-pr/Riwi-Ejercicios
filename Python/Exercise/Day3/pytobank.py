
def ahorro():
    cont = 0
    meta = 1000000
    for i in range(6):
        num = int(input("Ingresar valor a guardar: "))
        cont = cont + num
        i+=1
        if cont != meta:
            print(f"Aun te falta: {meta - cont }" )
        else:
            print(f"Meta alcanzada en el mes: {i} ")
            break
        
ahorro()
