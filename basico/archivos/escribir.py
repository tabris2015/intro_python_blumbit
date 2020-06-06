lista_verduras = ['papas', 'zanahoria', 'lechuga', 'tomate']

with open('C:\\projects\\python\\basico\\archivos\\compras.txt', 'w') as f:
    for verdura in lista_verduras:
        f.write(verdura)
        f.write(str(123))