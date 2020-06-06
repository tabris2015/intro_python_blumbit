lista_compras = ['papa', 'zanahoria', 'lechuga', 'chuleta']

# forma incorrecta
for i in range(len(lista_compras)):
    print(f'no olvides comprar {lista_compras[i]}')

# forma correcta
for item in lista_compras:
    print(f'no olvides comprar {item}')
