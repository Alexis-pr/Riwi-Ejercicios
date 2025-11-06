

" 1er ejercisio - Panaderia don pancho"

pan = 300
des1 = 10
des2 = 20

cantidad_panes = int(input('Ingresa panes a comprar: '))

total = cantidad_panes * pan

if cantidad_panes >= 20 and cantidad_panes <= 49:
    precio1= total - (total * des1/100)
    print(f'El valor a pagar es: {precio1}')

elif cantidad_panes >= 50:
     precio2= total - (total * des2/100)
     print(f'El valor a pagar es: {precio2}')

elif cantidad_panes < 0:
     print('Cantidad invalida')

else:
     print(f'El valor a pagar es {total}')


