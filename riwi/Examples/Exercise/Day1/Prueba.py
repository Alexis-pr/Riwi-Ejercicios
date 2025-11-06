
num = int(input(" ingresa un numero: "))

"""
if num %2 ==0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es Impar")
"""

for i in range(num):
    for k in range(i):
        if k % 2 == 0:
            print("El numero ingresado es par", k)
        else:
            print("El numero ingresado es Impar", k)



