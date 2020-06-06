pares = []      # lista vacia

# iterar para todos los valores del 0 al 29
for i in range(30):
    # si es par, agregar a la lista
    if i % 2 == 0:          # es par
        pares.append(i)
    
# imprimir los primeros 4 numeros pares
print(pares[:4])

# utilizando lists comprehensions

pares_2 = [i * 3 for i in range(30) if i % 2 == 0]

print(pares_2[:4])