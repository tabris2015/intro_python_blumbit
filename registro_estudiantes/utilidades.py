lista_materias = ['calculo', 'quimica', 'fisica', 'algebra']

def guardar_estudiantes(lista_estudiantes, nombre_archivo='registro.csv'):
    print('Guardando archivo...')
    with open(nombre_archivo, 'a') as f:
        # para cada estudiante guardar nombre y promedio
        for estudiante in lista_estudiantes:
            # extraer el nombre del estudiante
            nombre = estudiante['nombre']
            promedio = estudiante['promedio']
            f.write(f'{nombre}; {promedio}\n')
    print('Guardado exitoso!')

# uso:
# guardar_estudiantes(lista)      # se usa el valor por defecto de nombre_archivo
# guardar_estudiantes(lista, 'datos.txt') # se usa el valor que se especifica 