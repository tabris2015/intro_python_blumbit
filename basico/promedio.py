lista_materias = ['calculo 1', 'algebra', 'quimica', 'fisica']
dic_estudiante = {}
promedio = 0

estudiante = input('ingrese el nombre del estudiante: ')

for materia in lista_materias:
    # recibir la nota
    nota = int(input(f'ingrese la nota para {materia}: '))
    # guardar la nota
    dic_estudiante[materia] = nota
    promedio += nota

promedio = promedio / len(lista_materias)
dic_estudiante['promedio'] = promedio
print(estudiante, dic_estudiante)


