# crear una lista de estudiantes
estudiantes = []
n_estudiantes = int(input('ingrese numero de estudiantes: '))
# 3 estudiantes
for i in range(n_estudiantes):
    est = input(f'ingrese nombre del estudiante {i + 1}: ')
    estudiantes.append(est)

print(estudiantes)