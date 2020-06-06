# definir la funcion
def promedio_general(mat1, mat2, mat3):
    prom = (mat1 + mat2 + mat3) / 3
    return prom

nombre = 'arturo'
calculo1 = 45
quimica = 28
dibujo = 60

promedio = promedio_general(calculo1, quimica, dibujo)

# mostrar mensaje, segun la nota
if promedio >= 51:
    print(f'El estudiante {nombre} APROBÓ el semestre')
else: 
    print(f'El estudiante {nombre} REPROBÓ el semestre')


nombre1 = 'ernesto'
calculo1e = 95
quimicae = 98
dibujoe = 90

promedio2 = promedio_general(calculo1e, quimicae, dibujoe)

if promedio2 >= 51:
    print(f'El estudiante {nombre1} APROBÓ el semestre')
else: 
    print(f'El estudiante {nombre1} REPROBÓ el semestre')