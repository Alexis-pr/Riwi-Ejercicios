
#Gimnasio “Solo Leveling Fit” — Motivación + Bono

#se ingresa los días que entreno esta semana
dias = int(input("ingresa el numero de dias a entrenar: "))

#el contador suponiendo que vaya dentro de un ciclo o entrene durante varios meses
cont = 0

# calcular la cantidad de tiempo 
if dias >=2 and dias <= 3:
    print(" Bien, pero puedes dar más")

#se valida 
elif dias >= 4:
    cont = 1
    print(f" ¡Excelente disciplina! gana + {cont} punto de energía ")
else:
    print("No aflojes, tú puedes mejorar")
