from utilidades import lista_materias
from utilidades import guardar_estudiantes as save
# variables globales
lista_estudiantes = []
# solicitar el numero de estudiantes
# no se esta validando la entrada!! 
n_estudiantes = int(input('Ingrese el numero de estudiantes para registrar: '))
# para cada estudiante guardar datos
for i in range(n_estudiantes):
    print(f'estudiante {i + 1}: ')
    dic_estudiante = {}
    promedio = 0
    # registrar nombre
    nombre = input('Nombre: ')
    # para cada materia registrar la nota
    for materia in lista_materias:
        promedio += int(input(f'nota {materia}'))
    
    # calcular el promedio
    promedio /= len(lista_materias)
    # guardar en el registro del estudiante
    dic_estudiante['nombre'] = nombre
    dic_estudiante['promedio'] = promedio
    # agregar a la lista de estudiantes
    lista_estudiantes.append(dic_estudiante)
# guardar en un archivo
save(lista_estudiantes, 'primeroB.csv')