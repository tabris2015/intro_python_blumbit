salud = 60

while salud > 0:
    print(f'Estas sano. Salud: {salud}')
    salud = salud - 1       # decremento en 1

    if salud == 2:
        print('ya estas debil')
        break

print('Moriste!')