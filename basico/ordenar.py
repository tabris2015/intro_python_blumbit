lista_precios = [12,43,1,67,23,90,10,7]
print(lista_precios)
# 2 formas de ordenar
# externa crea una nueva lista ordenada en base a la original
precios_ordenado = sorted(lista_precios)
print(precios_ordenado)
# in-place modifica la lista original
lista_precios.sort()
print(lista_precios)

# eliminar el 3er elemento de la lista
a = lista_precios.pop(2) # retornar el valor del elemento

# precios mas caros
lista_caros = [p for p in lista_precios if p > 50]

caros = []
for p in lista_precios:
    if p > 50:
        caros.append(p)
print(lista_caros)