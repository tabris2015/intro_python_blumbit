# range(inicio, final, paso)
# inicio inclusivo
# final exclusivo
# paso el salto entre numeros
# inicio = 2 
# final = 6
# range(,,) = 22 18 14 10 6 2  
for n in range(22, 1, -4):
    print(n)


#
frase = 'arriba las manos'
contador_a = 0
for c in frase:
    if c == 'a':
        c = 'A'
        contador_a += 1
    print(c)

print(f'en la frase "{frase}" existen {contador_a} letras "a"')