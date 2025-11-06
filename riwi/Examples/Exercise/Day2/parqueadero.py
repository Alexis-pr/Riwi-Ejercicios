
valorTarifa = 2000
multa = 5000

horas = int(input("Cuantas horas te quedaste?"))

if  horas >= 0 and horas < 5:
    total= valorTarifa * horas
    print(" El valor sera de ", total)
else:
    total= (valorTarifa * horas) + multa
    print(" El valor ha superado el valor minimo", total)

