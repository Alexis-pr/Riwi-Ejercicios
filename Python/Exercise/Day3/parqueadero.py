


def parqueadero(self):
    cont = 0

    while cont < self:
        cont+=1

        if self % 2 == 0:
            print(f"Vehículo par registrado")
       

        if cont != 20:
            print(f"Faltan {--cont} cupos")
        else:
            print("capacidad completada")

num= int(input("Ingresar numero:  "))

parqueadero(num)