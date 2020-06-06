edad = 5
esta_enfermo = True
nombre = 'julia'
# definir si puede salir a la calle
# Booleano: True False
# operadores de comparacion
# > : mayor que
# < : menor que
# == : igualdad
# >= : mayor o igual
# <= : menor o igual
# != : distintos
# encadenar comparaciones
# not : negacion  !
# and : ambas condiciones se tienen que cumplir (cond1) and (cond2)*
# or : es verdadero si cualquiera es verdadero (cond1) or (cond2)

if (edad >= 18) and  (not esta_enfermo):
    print(f'{nombre} puede salir a la calle')
else:
    print(f'{nombre} NO puede salir a la calle!')


