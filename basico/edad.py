import random
# programa para calcular la edad de la muerte
# leemos la edad actual
edad_str = input('cual es tu edad? ')
if edad_str.isdigit():
    edad = int(edad_str)
    print(f'usted vivirá hasta los {edad + random.randint(15,30)} años')
else:
    print('ingresa un numero entero válido')